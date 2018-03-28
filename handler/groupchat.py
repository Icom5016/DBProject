from flask import jsonify, request
from dao.groupChatDao import GroupChatDAO
from dao.chatMembersDao import ChatMembersDAO

class GroupChatHandler():
    def getAllChats(self):
        dao = GroupChatDAO()
        result = dao.getAllChats()
        mapped_result = []
        for r in result:
            mapped_result.append(self.mapToGroupChatDict(r))
        return jsonify(Chats = mapped_result)

    def getGroupChatById(self, gcid):
        dao = GroupChatDAO()
        result = dao.getGroupChatById(gcid)
        if result == None:
            return jsonify(Error="NOT FOUND"), 404
        else:
            mapped_result = self.mapToGroupChatDict(result)
            return jsonify(ChatsById=mapped_result)

    def getAllGroupChatByOwnerId(self, gcownerid):
        dao = GroupChatDAO()
        result = dao.getAllGroupChatsByOwnerId(gcownerid)
        mapped_result = []
        for r in result:
            mapped_result.append(self.mapToGroupChatDict(r))
        return jsonify(ChatsByOwner=mapped_result)

    def getGroupChatsByOwnerIdAndName(self, gcownerid, gcname):
        dao = GroupChatDAO()
        result = dao.getAllChatsByOwnerIdAndName(gcownerid, gcname)
        mapped_result = []
        for r in result:
            mapped_result.append(self.mapToGroupChatDict(r))
        return jsonify(ChatsByOwnerAndName = mapped_result)

    def getGroupChatsByName(self, gcname):
        dao = GroupChatDAO()
        result = dao.getAllChatsByName(gcname)
        mapped_result = []
        for r in result:
            mapped_result.append(self.mapToGroupChatDict(r))
        return jsonify(ChatsByName = mapped_result)

    def mapToGroupChatDict(self, row):
        result = {}
        result["gcid"] = row[0]
        result["gcname"] = row[1]
        result["gcowner"] =row[2]
        return result

    def getAllChatsAndMembers(self):
        dao = ChatMembersDAO()
        result = dao.getAllChatsAndMembers()
        mapped_result = []
        for r in result:
            mapped_result.append(self.mapToChatAndMembersDict(r))
        return jsonify(ChatsAndMembers=mapped_result)

    def getChatMembersByChatID(self, chat_id):
        dao = ChatMembersDAO()
        result = dao.getAllChatMembersByChatID(chat_id)
        if result == None:
            return jsonify(Error="NOT FOUND"), 404
        else :
            mapped = self.mapToChatAndMembersDict(result)
            return jsonify(ChatAndMembers=mapped)

    def mapToChatAndMembersDict(self, row):
        result = {}
        result["chat_id"] = row[0]
        result["members"] = row[1]
        return result
