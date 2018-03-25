from flask import jsonify, request
from dao.messageDao import MsgDAO

class MsgHandler:
    def getAllMsg(self):
        dao = MsgDAO()
        result = dao.getAllMsg()
        mapped_result = []
        for r in result:
            mapped_result.append(self.mapToMsgDict(r))
        return jsonify(Message=mapped_result)

    def getMsgById(self, msg_id):
        dao = MsgDAO()
        result = dao.getMsgById(msg_id)
        if result == None:
            return jsonify(Error="NOT FOUND"), 404
        else :
            mapped = self.mapToMsgDict(result)
            return jsonify(Message=mapped)

    def mapToMsgDict(self, row):
        result = {}
        result["msg_id"] = row[0]
        result["text"] = row[1]
        result["likes"] = row[2]
        result["dislikes"] = row[3]
        result["user_id"] = row[4]
        result["chat_id"] = row[5]
        return result

    def getAuthorByMsgId(self, msg_id):
        dao = MsgDAO()
        #Dummy
        # result = ["117", "John"]
        # if result == None:
        #     return jsonify(Error="NOT FOUND"), 404
        # else :
        #     mapped = self.mapToAuthorDict(result)
        #     return jsonify(Author=mapped)
        #Correct
        result = dao.getAuthorByMsgId(msg_id)
        if result == None:
            return jsonify(Error="NOT FOUND"), 404
        else :
            mapped = self.mapToAuthorDict(result)
            return jsonify(Author=mapped)

    def mapToAuthorDict(self, row):
        result = {}
        result["user_id"] = row[0]
        result["first_name"] = row[1]
        result["second_name"] = row[2]
        result["email"] = row[3]
        result["phone"] = row[4]
        #Before loop
        # result = {}
        # result["user_id"] = row[0]
        # result["first_name"] = row[1]
        return result

    def getTextByMsgId(self, msg_id):
        dao = MsgDAO()
        result = dao.getTextByMsgID(msg_id)
        if result == None:
            return jsonify(Error="NOT FOUND"), 404
        else :
            mapped = self.mapToTextDict(result)
            return jsonify(Message=mapped)

    def mapToTextDict(self, row):
        result = {}
        result["text"] = row #row[0] hace que solo devuelva the first char of the message
        return result

    def getLikesByMsgId(self, msg_id):
        dao = MsgDAO()
        result = dao.getLikesByMsgID(msg_id)
        if result == None:
            return jsonify(Error="NOT FOUND"), 404
        else :
            mapped = self.mapToLikesDict(result)
            return jsonify(Message=mapped)

    def getDislikesByMsgId(self, msg_id):
        dao = MsgDAO()
        result = dao.getDislikesByMsgID(msg_id)
        if result == None:
            return jsonify(Error="NOT FOUND"), 404
        else :
            mapped = self.mapToDislikesDict(result)
            return jsonify(Message=mapped)

    def mapToLikesDict(self, row):
        result = {}
        result["likes"] = row #hmmmmm
        return result

    def mapToDislikesDict(self, row):
        result = {}
        result["dislikes"] = row #hmmmmm
        return result