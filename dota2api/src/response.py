"""Response template, this is used so we can pass the response as an object"""

import parse

class Dota2Response(object):
    """Generic response used when we don't parse"""
    def __init__(self, response, url):
        self.url = url
        self.resp = response

class Dota2MatchDetails(object):
    """This is used to package up the response"""
    def __init__(self, response, url):
        self.url = url
        if 'players' in response
            self.resp = parse.hero_id(response)
            self.resp = parse.item_id(response)
        else:
            pass
