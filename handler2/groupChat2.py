from flask import jsonify, request
from dao2.groupchatDao2 import GroupChatDAO
from dao2.chatMembersDao2 import ChatMembersDAO
from dao2.userDao2 import UserDAO

class GroupChatHandler():
    def getAllChats(self):
        dao = GroupChatDAO()
        result = dao.getAllChats()
        mapped_result = []
        for r in result:
            mapped_result.append(self.mapToGroupChatDict(r))
        return jsonify(Chats = mapped_result)

    def getGroupChatById(self, gchat_id):
        dao = GroupChatDAO()
        result = dao.getGroupChatById(gchat_id)
        if result == None:
            return jsonify(Error="NOT FOUND"), 404
        else:
            mapped_result = self.mapToGroupChatDict(result)
            return jsonify(ChatsById=mapped_result)

    def getAllGroupChatByOwnerId(self, owner_id):
        dao = GroupChatDAO()
        result = []
        result.append(dao.getAllGroupChatsByOwnerId(owner_id))
        mapped_result = []
        for r in result:
            mapped_result.append(self.mapToGroupChatDict(r))
        return jsonify(ChatsByOwner=mapped_result)

    def getGroupChatsByOwnerIdAndName(self, owner_id, gchat_name):
        dao = GroupChatDAO()
        result = []
        result.append(dao.getAllChatsByOwnerIdAndName(owner_id, gchat_name))
        mapped_result = []
        for r in result:
            mapped_result.append(self.mapToGroupChatDict(r))
        return jsonify(ChatsByOwnerAndName = mapped_result)

    def getGroupChatsByName(self, gchat_name):
        dao = GroupChatDAO()
        result = []
        result.append(dao.getAllChatsByName(gchat_name))
        mapped_result = []
        for r in result:
            mapped_result.append(self.mapToGroupChatDict(r))
        return jsonify(ChatsByName = mapped_result)

    def mapToGroupChatDict(self, row):
        result = {}
        result["gchat_id"] = row[0]
        result["gchat_name"] = row[1]
        result["person_id"] =row[2]
        return result

    def getAllChatsAndMembers(self):
        dao = ChatMembersDAO()
        result = dao.getAllChatsAndMembers()
        mapped_result = []
        for r in result:
            mapped_result.append(self.mapToChatAndMembersDict(r))
        return jsonify(ChatsAndMembers=mapped_result)

    def getChatMembersByChatID(self, gchat_id):
        dao = ChatMembersDAO()
        result = dao.getAllChatMembersByChatID(gchat_id)
        if result == None:
            return jsonify(Error="NOT FOUND"), 404
        else :
            mapped = self.mapToChatAndMembersDict(result)
            return jsonify(ChatAndMembers=mapped)

    def mapToChatAndMembersDict(self, row):
        result = {}
        result["gchat_id"] = row[0]
        result["members"] = row[1]
        return result

    def getOwnerOfChat(self, gc_id):
        dao1 = GroupChatDAO()
        u_id = dao1.getOwnerOfChat(gc_id)
        dao2 = UserDAO()
        result = dao2.getUserById(u_id)
        if result == None:
            return jsonify(Error="NOT FOUND"), 404
        else:
            mapped = self.mapToUserDict(result)
            return jsonify(Owner=mapped)

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
