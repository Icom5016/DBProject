from flask import jsonify, request
from dao.groupchatDAO import gcDAO

class groupchatHandler:

    def mapToGroupchatDict(self, row):
        result = {}
        result["gcid"] = row[0]
        result["gcname"] = row[1]
        result["gcowner"] =row[2]
        return result

    def getAllChats(self):
        dao = gcDAO
        result = gcDAO.getAllChats()
        mapped_result = []
        for r in result:
            mapped_result.append(self.mapToGroupchatDict(r))
        return jsonify(Chats = mapped_result)

    def getGroupChatById(self, gcid):
        dao = gcDAO
        result = gcDAO.getChatById(gcid)
        if result == None:
            return jsonify(Error="NOT FOUND"), 404
        else:
            mapped_result = self.mapToGroupchatDict(result)
            return jsonify(ChatsById=mapped_result)

    def getGroupChatByOwnerId(self, gcownerid):
        dao = gcDAO
        result = gcDAO.getAllChatsByOwnerId(gcownerid)
        mapped_result = []
        for r in result:
            mapped_result.append(self.mapToGroupchatDict(r))
        return jsonify(ChatsByOwner=mapped_result)

    def getGroupChatsByOwnerIdAndName(self, gcownerid, gcname):
        dao = gcDAO
        result = gcDAO.getAllChatsByOwnerIdAndName(gcownerid, gcname)
        mapped_result = []
        for r in result:
            mapped_result.append(self.mapToGroupchatDict(r))
        return jsonify(ChatsByOwnerAndName = mapped_result)

    def getGroupChatsByName(self, gcname):
        dao = gcDAO
        result = gcDAO.getAllChatsByName(gcname)
        mapped_result = []
        for r in result:
            mapped_result.append(self.mapToGroupchatDict(r))
        return jsonify(ChatsByName = mapped_result)