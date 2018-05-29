from flask import jsonify, request
from dao.messageDao import MsgDAO
# from dao.likesDao import LikesDAO
# from dao.dislikesDao import DislikesDAO
from dao.userDao import UserDAO
from dao.hashtagDao import HashtagDAO

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

    def getAllMsgByUserId(self, user_id):
        dao = MsgDAO()
        result = dao.getAllMsgByUserId(user_id)
        mapped_result = []
        for r in result:
            mapped_result.append(self.mapToMsgDict(r))
        return jsonify(Message=mapped_result)

    def mapToMsgDict(self, row):
        result = {}
        result["msg_id"] = row[0]
        result["text"] = row[1]
        result["likes"] = row[2]
        result["dislikes"] = row[3]
        result["date"] = row[4]
        time = "%s:%s:%s" % (row[5].hour, row[5].minute, row[5].second)
        result["time"] = time
        result["person_id"] = row[6]
        result["gchat_id"] = row[7]
        result["username"] = row[8]
        return result

    def getAuthorByMsgId(self, msg_id):
        dao = MsgDAO()
        result_id = dao.getAuthorByMsgId(msg_id)
        if result_id == None:
            return jsonify(Error="NOT FOUND"), 404
        userDao = UserDAO()
        result = userDao.getUserById(result_id[0])
        mapped = self.mapToUserDict(result)
        return jsonify(Author=mapped)

    def getAllLikeUsersByMsgID(self, msg_id):
        dao = MsgDAO()
        result = dao.getAllLikeUsersByMsgID(msg_id)
        if result == None:
            return jsonify(Error="NOT FOUND"), 404
        else:
            mapped_result = []
            for r in result:
                mapped_result.append(self.mapToUserDict(r))
            return jsonify(UsersThatLike=mapped_result)

    def getAllDislikeUsersByMsgID(self, msg_id):
        dao = MsgDAO()
        result = dao.getAllDislikeUsersByMsgID(msg_id)
        if result == None:
            return jsonify(Error="NOT FOUND"), 404
        else:
            mapped_result = []
            for r in result:
                mapped_result.append(self.mapToUserDict(r))
            return jsonify(UsersThatDislike=mapped_result)

    def mapToUserDict(self, row):
        result = {}
        result["user_id"] = row[0]
        result["first_name"] = row[1]
        result["last_name"] = row[2]
        result["email"] = row[3]
        result["phone"] = row[4]
        result["password"] = row[5]
        result["username"] = row[6]
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
        if result == None:
            return jsonify(Error="NOT FOUND"), 404
        mapped_result = []
        for r in result:
            mapped_result.append(self.mapToMsgDict(r))
        return jsonify(Messages=mapped_result)

    def getMessagesByChatIdAndUserId(self, gchat_id, user_id):
        dao = MsgDAO()
        result = dao.getMessagesByChatIdAndUserId(gchat_id, user_id)
        if result == None:
            return jsonify(Error="NOT FOUND"), 404
        mapped_result = []
        for r in result:
            mapped_result.append(self.mapToMsgDict(r))
        return jsonify(Messages=mapped_result)

    def getUsersWhoLikeMessages(self, msg_id):
        dao1 = MsgDAO()
        result = dao1.getAllLikeUsersByMsgID(msg_id)
        if not result:
            return jsonify(Error="NOT FOUND"), 404
        dao2 = UserDAO()
        mapped_result = []
        for r in result:
            mapped_result.append(self.mapToUserDict(r))
        return jsonify(Users=mapped_result)

    def getUsersWhoDislikeMessages(self, msg_id):
        dao1 = MsgDAO()
        result = dao1.getAllDislikeUsersByMsgID(msg_id)
        if not result:
            return jsonify(Error="NOT FOUND"), 404
        dao2 = UserDAO()
        mapped_result = []
        for r in result:
            mapped_result.append(self.mapToUserDict(r))
        return jsonify(Users=mapped_result)

    #########NOT YET IMPLEMENTED
    #
    #def getMessagesDislikedByUser(self, u_id):
    #    dao = MsgDAO()
    #    result = dao.getMessagesDislikedByUser(u_id)
    #    if len(result) == 0:
    #        return jsonify(Error="NOT FOUND"), 404
    #    dao = MsgDAO()
    #    mapped_result = []
    #    for r in result:
    #        mapped_result.append(self.mapToMsgDict(dao.getMsgById(r)))
    #    return jsonify(Messages=mapped_result)
    #
    #def getMessagesLikedByUser(self, u_id):
    #    dao = MsgDAO()
    #    result = dao.getMessagesLikedByUser(u_id)
    #    if len(result) == 0:
    #        return jsonify(Error="NOT FOUND"), 404
    #    dao = MsgDAO()
    #    mapped_result = []
    #    for r in result:
    #        mapped_result.append(self.mapToMsgDict(dao.getMsgById(r)))
    #    return jsonify(Messages=mapped_result)


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
        result = dao.getRepliesByOriginalId(original_id)
        if result == None:
            return jsonify(Error="NOT FOUND"), 404
        else:
            mapped_result = []
            for r in result:
                mapped_result.append(self.mapToMsgDict(r))
            return jsonify(Replies=mapped_result)

    def getAllReplies(self):
        dao = MsgDAO()
        result = dao.getAllReplies()
        if result == None:
            return jsonify(Error="NOT FOUND"), 404
        else:
            mapped_result = []
            for r in result:
                mapped_result.append(self.mapToMsgDict(r))
            return jsonify(Replies=mapped_result)

    def insertMsg(self, form):
        if len(form) != 4:
            return jsonify(Error="Malformed post request"), 400
        else:
            text = form['text']
            person_id = form['person_id']
            gchat_id = form['gchat_id']
            username = form['username']
            hashtags = [i for i in text.split() if i.startswith("#")]
            if text and person_id and gchat_id and username:
                dao = MsgDAO()
                msg = dao.insertMsg(text, 0, 0, person_id, gchat_id, username)
                result = self.mapToMsgDict(msg)
                if hashtags:
                    dao = HashtagDAO()
                    for h in hashtags:
                        dao.insertHashtag(h[1:], result['msg_id'])
                return jsonify(Message=result), 201
            else:
                return jsonify(Error="Unexpected attributes in post request"), 400

    def insertReply(self, form):
        if len(form) != 2:
            return jsonify(Error="Malformed post request"), 400
        else:
            original_id = form['original_id']
            msg_id = form['msg_id']
            if original_id and msg_id:
                dao = MsgDAO()
                reply_id = dao.insertReply(original_id, msg_id)
                result = self.mapToReplyDict([reply_id, original_id, msg_id])
                return jsonify(Reply=result), 201
            else:
                return jsonify(Error="Unexpected attributes in post request"), 400

    def mapToReplyDict(self, row):
        result = {}
        result["reply_id"] = row[0]
        result["original_id"] = row[1]
        result["msg_id"] = row[2]
        return result

    def deleteMsg(self, form):
        if len(form) != 1:
            return jsonify(Error="Malformed post request"), 400
        else:
            msg_id = form['msg_id']
            if msg_id:
                dao = MsgDAO()
                dao.deleteMsg(msg_id)
                return jsonify(DeleteStatus="OK"), 200

    def deleteReply(self, form):
        if len(form) != 1:
            return jsonify(Error="Malformed post request"), 400
        else:
            reply_id = form['reply_id']
            if reply_id:
                dao = MsgDAO()
                msg_id = dao.deleteReply(reply_id)
                dao.deleteMsg(msg_id)
                return jsonify(DeleteStatus="OK"), 200

    def updateLikes(self, form):
        if len(form) != 4:
            return jsonify(Error="Malformed post request"), 400
        else:
            likes = form['likes']
            dislikes = form['dislikes']
            person_id = form['person_id']
            msg_id = form['msg_id']
            if likes is not None and dislikes is not None and person_id and msg_id:
                dao = MsgDAO()
                react = dao.getReactByMsgAndUserID(msg_id, person_id)
                # If users hasn't reacted yet to message
                if not react:
                    react_id = dao.insertReact(likes, dislikes, person_id, msg_id)
                    dao.updateReactCount(1, 0, msg_id)
                    return jsonify(React=self.mapToReact([react_id, likes, dislikes, person_id, msg_id]))
                else:
                    # User already liked message, set liked to false
                    if react[1] == True:
                        react_id = dao.updateReact(not likes, dislikes, person_id, msg_id)
                        dao.updateReactCount(-1, 0, msg_id)
                        return jsonify(React=self.mapToReact(react))
                    # User had disliked message, set like to true and dislike to false
                    elif react[2] == True:
                        react_id = dao.updateReact(likes, dislikes, person_id, msg_id)
                        dao.updateReactCount(1, -1, msg_id)
                        return jsonify(React=self.mapToReact([react_id, likes, dislikes, person_id, msg_id]))
                    else:
                        react_id = dao.updateReact(likes, dislikes, person_id, msg_id)
                        dao.updateReactCount(1, 0, msg_id)
                        return jsonify(React=self.mapToReact([react_id, likes, dislikes, person_id, msg_id]))
            else:
                return jsonify(Error="Unexpected attributes in post request"), 400

    def updateDisikes(self, form):
        if len(form) != 4:
            return jsonify(Error="Malformed post request"), 400
        else:
            likes = form['likes']
            dislikes = form['dislikes']
            person_id = form['person_id']
            msg_id = form['msg_id']
            if likes is not None and dislikes is not None and person_id and msg_id:
                dao = MsgDAO()
                react = dao.getReactByMsgAndUserID(msg_id, person_id)
                # If users hasn't reacted yet to message
                if not react:
                    react_id = dao.insertReact(likes, dislikes, person_id, msg_id)
                    dao.updateReactCount(0, 1, msg_id)
                    return jsonify(React=self.mapToReact([react_id, likes, dislikes, person_id, msg_id]))
                else:
                    # User already disliked message, set dislike to false
                    if react[2] == True:
                        react_id = dao.updateReact(likes, not dislikes, person_id, msg_id)
                        dao.updateReactCount(0, -1, msg_id)
                        return jsonify(React=self.mapToReact(react))
                    # User had liked message, set dislike to true and like to false
                    elif react[1] == True:
                        react_id = dao.updateReact(likes, dislikes, person_id, msg_id)
                        dao.updateReactCount(-1, 1, msg_id)
                        return jsonify(React=self.mapToReact([react_id, likes, dislikes, person_id, msg_id]))
                    else:
                        react_id = dao.updateReactCount(likes, dislikes, person_id, msg_id)
                        dao.updateReactCount(0, 1, msg_id)
                        return jsonify(React=self.mapToReact([react_id, likes, dislikes, person_id, msg_id]))
            else:
                return jsonify(Error="Unexpected attributes in post request"), 400

    def mapToReact(self, row):
        result = {}
        result['react_id'] = row[0]
        result['likes'] = row[1]
        result['dislikes'] = row[2]
        result['person_id'] = row[3]
        result['msg_id'] = row[4]
        return result