from flask import jsonify, request
from dao.replyDao import ReplyDAO
from handler.messages import MsgHandler

class ReplyHandler:
    def getOriginalByReplyId(self, reply_id):
        dao = ReplyDAO()
        msg_handler = MsgHandler()
        result = dao.getOriginalByReplyId(reply_id)
        if result == None:
            return jsonify(Error="NOT FOUND"), 404
        else:
            mapped = msg_handler.mapToMsgDict(result)
            return jsonify(Original=mapped)

    def getRepliesByOriginalId(self, original_id):
        dao = ReplyDAO()
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
        dao = ReplyDAO()
        msg_handler = MsgHandler()
        result = dao.getAllReplies()
        if result == None:
            return jsonify(Error="NOT FOUND"), 404
        else:
            mapped_result = []
            for r in result:
                mapped_result.append(msg_handler.mapToMsgDict(r))
            return jsonify(Replies=mapped_result)