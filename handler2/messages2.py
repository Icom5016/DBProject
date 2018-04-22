from flask import jsonify, request
from dao2.messageDao2 import MsgDAO
# from dao.likesDao import LikesDAO
# from dao.dislikesDao import DislikesDAO
from dao2.userDao2 import UserDAO

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
        result["date"] = row[4]
        #result["time"] = row[5]
        result["person_id"] = row[6]
        result["gchat_id"] = row[7]
        return result

    def getAuthorByMsgId(self, msg_id):
        dao = MsgDAO()
        result_id = dao.getAuthorByMsgId(msg_id)
        if result_id == None:
            return jsonify(Error="NOT FOUND"), 404
        userDao = UserDAO()
        result = userDao.getUserById(result_id[0])
        mapped = self.mapToAuthorDict(result)
        return jsonify(Author=mapped)

    def mapToAuthorDict(self, row):
        result = {}
        result["user_id"] = row[0]
        result["first_name"] = row[1]
        result["last_name"] = row[2]
        result["email"] = row[3]
        result["phone"] = row[4]
        result["password"] = row[5]
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
        result["text"] = row
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
        result["likes"] = row
        return result

    def mapToDislikesDict(self, row):
        result = {}
        result["dislikes"] = row
        return result

    def getTimeByMsgId(self, msg_id):
        dao = MsgDAO()
        result = dao.getTimeByMsgID(msg_id)
        if result == None:
            return jsonify(Error="NOT FOUND"), 404
        else :
            mapped = self.mapToTimeDict(result)
            return jsonify(Time=mapped)

    def mapToTimeDict(self, row):
        result = {}
        result["time"] = row
        return result

    def getDateByMsgId(self, msg_id):
        dao = MsgDAO()
        result = dao.getDateByMsgID(msg_id)
        if result == None:
            return jsonify(Error="NOT FOUND"), 404
        else :
            mapped = self.mapToDateDict(result)
            return jsonify(Date=mapped)

    def mapToDateDict(self, row):
        result = {}
        result["date"] = row
        return result

    def getMessagesByChatId(self, gc_id):
        dao = MsgDAO()
        result = dao.getMessagesByChatId(gc_id)
        if len(result) == 0:
            return jsonify(Error="NOT FOUND"), 404
        mapped_result = []
        for r in result:
            mapped_result.append(self.mapToMsgDict(r))
        return jsonify(Messages=mapped_result)

    def getMessagesFromAUserInChat(self, gc_id, user_id):
        dao = MsgDAO()
        result = dao.getMessagesByChatIdAndUserId(gc_id, user_id)
        if result == None:
            return jsonify(Error="NOT FOUND"), 404
        mapped_result = []
        for r in result:
            mapped_result.append(self.mapToMsgDict(r))
        return jsonify(Messages=mapped_result)

    # def getUsersWhoLikeMessages(self, msg_id):
    #     dao1 = LikesDAO()
    #     result = dao1.getUsersWhoLikeMessage(msg_id)
    #     if len(result) == 0:
    #         return jsonify(Error="NOT FOUND"), 404
    #     dao2 = UserDAO()
    #     mapped_result = []
    #     for r in result:
    #         mapped_result.append(self.mapToUserDict(dao2.getUserById(r)))
    #     return jsonify(Users=mapped_result)
    #
    # def getMessagesLikedByUser(self, u_id):
    #     dao = LikesDAO()
    #     result = dao.getMessagesLikedByUser(u_id)
    #     if len(result) == 0:
    #         return jsonify(Error="NOT FOUND"), 404
    #     dao2 = MsgDAO()
    #     mapped_result = []
    #     for r in result:
    #         mapped_result.append(self.mapToMsgDict(dao2.getMsgById(r)))
    #     return jsonify(Messages=mapped_result)
    #
    # def getUsersWhoDislikeMessages(self, msg_id):
    #     dao1 = DislikesDAO()
    #     result = dao1.getUsersWhoDislikeMessage(msg_id)
    #     if len(result) == 0:
    #         return jsonify(Error="NOT FOUND"), 404
    #     dao2 = UserDAO()
    #     mapped_result = []
    #     for r in result:
    #         mapped_result.append(self.mapToUserDict(dao2.getUserById(r)))
    #     return jsonify(Users=mapped_result)
    #
    # def getMessagesDislikedByUser(self, u_id):
    #     dao = DislikesDAO()
    #     result = dao.getMessagesDislikedByUser(u_id)
    #     if len(result) == 0:
    #         return jsonify(Error="NOT FOUND"), 404
    #     dao2 = MsgDAO()
    #     mapped_result = []
    #     for r in result:
    #         mapped_result.append(self.mapToMsgDict(dao2.getMsgById(r)))
    #     return jsonify(Messages=mapped_result)

    def mapToUserDict(self, row):
        result = {}
        result["user_id"] = row[0]
        result["first_name"] = row[1]
        result["last_name"] = row[2]
        result["email"] = row[3]
        result["phone"] = row[4]
        result["username"] = row[5]
        result["password"] = row[6]
        return result

    def getOriginalByReplyId(self, reply_id):
        dao = MsgDAO()
        msg_handler = MsgHandler()
        result = dao.getOriginalByReplyId(reply_id)
        if result == None:
            return jsonify(Error="NOT FOUND"), 404
        else:
            mapped = msg_handler.mapToMsgDict(result)
            return jsonify(Original=mapped)

    def getRepliesByOriginalId(self, original_id):
        dao = MsgDAO()
        msg_handler = MsgHandler()
        result = dao.getRepliesByOriginalId(original_id)
        if result == None:
            return jsonify(Error="NOT FOUND"), 404
        else:
            mapped_result = []
            for r in result:
                mapped_result.append(msg_handler.mapToMsgDict(r))
            return jsonify(Replies=mapped_result)

    def getAllReplies(self):
        dao = MsgDAO()
        msg_handler = MsgHandler()
        result = dao.getAllReplies()
        if result == None:
            return jsonify(Error="NOT FOUND"), 404
        else:
            mapped_result = []
            for r in result:
                mapped_result.append(msg_handler.mapToMsgDict(r))
            return jsonify(Replies=mapped_result)