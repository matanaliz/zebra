#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import vk_auth
import json
import urllib.parse
import urllib.request


class Singleton(type):
    instance = None

    def __call__(cls, *args, **kw):
        if not cls.instance:
            cls.instance = super(Singleton, cls).__call__(*args, **kw)
        return cls.instance


class VkApi(metaclass=Singleton):
    def __init__(self):
        self.client_id = 4936810
        self.scope = ["offline", "audio"]
        self.token = ""
        self.current_user_id = -1

    def call_api(self, method, params):
        params.append(("access_token", self.token))
        params = urllib.parse.urlencode(params)
        url = "https://api.vk.com/method/%s?%s" % (method, params)
        data = urllib.request.urlopen(url).read().decode("utf-8")
        return json.loads(data)["response"]

    def audio_get_count(self, user_id):
        params = [("owner_id", user_id)]
        return self.call_api("audio.getCount", params)

    def audio_get(self, user_id, count):
        params = [ ("owner_id", user_id), ("album_id", 0), ("count", count), ("need_user", 0) ]
        return self.call_api("audio.get", params)

    def login(self, user):
        self.token, self.current_user_id = vk_auth.auth(user, self.client_id, self.scope)
        user.user_id = self.current_user_id

    def isLogedIn(self):
        if self.token == "":
            return False
        return True
