#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import http.cookiejar
import urllib.request
import urllib.parse

from vk_form_parser import VkFormParser
from urllib.parse import urlparse

def auth(user, client_id, scope):
    def get_auth_page(client_id, scope):
        return "http://oauth.vk.com/oauth/authorize?" + \
                "redirect_uri=http://oauth.vk.com/blank.html&response_type=token&" + \
                "client_id=%s&scope=%s&display=wap&v=3.0" % (client_id, ",".join(scope))

    def auth_user(user, auth_page, opener):
        response = opener.open(auth_page)
        doc = response.read()
        parser = VkFormParser()
        parser.feed(doc.decode("utf-8"))
        parser.close()
        parser.params["email"] = user.email
        parser.params["pass"] = user.password
        if parser.method == "POST":
            data = urllib.parse.urlencode(parser.params)
            binary_data = data.encode("utf-8")
            response = opener.open(parser.url, binary_data)
        else:
            raise NotImplementedError("Method '%s'" % parser.method)
        return response.read(), response.geturl()

    def gain_access(doc, opener):
        parser = VkFormParser()
        parser.feed(doc.decode("utf-8"))
        parser.close()
        if parser.url is None:
            raise RuntimeError("parser.url == None")
        if parser.method == "POST":
            data = urllib.parse.urlencode(parser.params)
            binary_data = data.encode("utf-8")
            response = opener.open(parser.url, binary_data)
        else:
            raise NotImplementedError("Method '%s'" % parser.method)
        return response.geturl()

    def split_key_value(pair):
        tmp = pair.split("=")
        return tmp[0], tmp[1]

    if not isinstance(scope, list):
        scope = [scope]
    opener = urllib.request.build_opener(
        urllib.request.HTTPCookieProcessor(http.cookiejar.CookieJar()),
        urllib.request.HTTPRedirectHandler()
    )

    doc, url = auth_user(user, get_auth_page(client_id, scope), opener)
    if urlparse(url).path != "/blank.html":
        url = gain_access(doc, opener)
    if urlparse(url).path != "/blank.html":
        raise RuntimeError("failed to gain access: " + url)
    response = dict(split_key_value(pair) for pair in urlparse(url).fragment.split("&"))
    if "access_token" not in response or "user_id" not in response:
        raise RuntimeError("failed to gain access_token or user_id")
    return response["access_token"], response["user_id"]
