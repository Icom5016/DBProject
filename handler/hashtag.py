from flask import jsonify, request
from dao.hashtagDao import HashtagDAO

class HashtagHandler:
    def getAllHashtag(self):
        dao = HashtagDAO()
        result = dao.getAllHashtag()
        mapped_result = []
        for r in result:
            mapped_result.append(self.mapToHashtagDict(r))
        return jsonify(Hashtag=mapped_result)

    def getHashtagById(self, hashtag_id):
        dao = HashtagDAO()
        result = dao.getHashtagById(hashtag_id)
        if result == None:
            return jsonify(Error="NOT FOUND"), 404
        else :
            mapped = self.mapToHashtagDict(result)
            return jsonify(Hashtag=mapped)

    def mapToHashtagDict(self, row):
        result = {}
        result["hashtag_id"] = row[0]
        result["text"] = row[1]
        result["frequency"] = row[2]
        return result

    def getTextByHashtagId(self, hashtag_id):
        dao = HashtagDAO()
        result = dao.getTextByHashtagId(hashtag_id)
        if result == None:
            return jsonify(Error="NOT FOUND"), 404
        else :
            mapped = self.mapToTextDict(result)
            return jsonify(Hashtag=mapped)

    def mapToTextDict(self, row):
        result = {}
        result["text"] = row
        return result

    def getFrequencyByHashtagId(self, hashtag_id):
        dao = HashtagDAO()
        result = dao.getFrequencyByHashtagId(hashtag_id)
        if result == None:
            return jsonify(Error="NOT FOUND"), 404
        else :
            mapped = self.mapToFrequencyDict(result)
            return jsonify(Hashtag=mapped)

    def getFrequencyByHashtagText(self, hashtag_text):
        dao = HashtagDAO()
        result = dao.getFrequencyByHashtagText(hashtag_text)
        if result == None:
            return jsonify(Error="NOT FOUND"), 404
        else :
            mapped = self.mapToFrequencyDict(result)
            return jsonify(Hashtag=mapped)

    def mapToFrequencyDict(self, row):
        result = {}
        result["frequency"] = row
        return result