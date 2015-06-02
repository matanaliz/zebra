#!/usr/bin/env python
# -*- coding: UTF-8 -*-


class VkAudio:
    def __init__(self):
        self.lyrics_id = -1
        self.owner_id = -1
        self.aid = -1
        self.title = ""
        self.artist = ""
        self.duration = -1
        self.genre = -1
        self.url = ""

    def load(self, parsed_json):
        if ("lyrics_id" in parsed_json):
            self.lyrics_id = parsed_json["lyrics_id"]
        self.owner_id = parsed_json["owner_id"]
        self.aid = parsed_json["aid"]
        self.title = parsed_json["title"]
        self.artist = parsed_json["artist"]
        self.duration = parsed_json["duration"]
        if ("genre_id" in parsed_json):
            self.genre = parsed_json["genre_id"]
        self.url = parsed_json["url"]

    @staticmethod
    def parse(json):
        result = []
        count = len(json)
        for i in range(1, count):
            audio = VkAudio()
            audio.load(json[i])
            result.append(audio)
        return result
