from flask import jsonify
from dao.hashtag import HashtagDAO
from dictionaryMapping import *


class HashtagHandler:

    def getTrendingHashtag(self):
        dao = HashtagDAO()
        result = dao.getTrendingHashtag()
        if not result:
            return jsonify(Error="Not found"), 404
        mapped_result = []
        for r in result:
            mapped_result.append(mapTrendingTopicToDict(r))
        return jsonify(mapped_result)

