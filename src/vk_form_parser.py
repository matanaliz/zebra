#!/usr/bin/env python
# -*- coding: UTF-8 -*-

from html.parser import HTMLParser


class VkFormParser(HTMLParser):
    def __init__(self):
        HTMLParser.__init__(self)
        self.url = None
        self.params = {}
        self.inside_form = False
        self.method = "get"

    def handle_starttag(self, tag, attrs):
        tag = tag.lower()
        if tag == "form":
            self.inside_form = True
        if not self.inside_form:
            return
        attrs = dict((name.lower(), value) for name, value in attrs)
        if tag == "form":
            self.url = attrs["action"]
            if "method" in attrs:
                self.method = attrs["method"].upper()
        elif tag == "input" and "type" in attrs and "name" in attrs:
            if attrs["type"] in ["hidden", "text", "password"]:
                self.params[attrs["name"]] = attrs["value"] if "value" in attrs else ""

    def handle_endtag(self, tag):
        tag = tag.lower()
        if tag == "form":
            self.inside_form = False
