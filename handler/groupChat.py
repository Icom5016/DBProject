from flask import jsonify, request
from dao.groupchatDao import GroupChatDAO
from dao.chatMembersDao import ChatMembersDAO
from dao.userDao import UserDAO

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
            mapped_result.append(self.mapToAllChatsAndMembersListDict(r))
        return jsonify(ChatsAndMembers=mapped_result)

    def mapToAllChatsAndMembersListDict(self, row):
        result = {}
        result["gchat_id"] = row[0]
        result["chat_name"] = row[1]
        result["members"] = row[2]
        return result

    def getChatMembersByChatID(self, gchat_id):
        dao = ChatMembersDAO()
        result = dao.getAllChatMembersByChatID(gchat_id)
        mapped_result = []
        for r in result:
            mapped_result.append(self.mapToUserDict(r))

        if result == None:
            return jsonify(Error="NOT FOUND"), 404
        return jsonify(Chat_Members=mapped_result)

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
        result["password"] = row[5]
        result["username"] = row[6]
        return result

    def insertToGroupChat(self, form):
        if len(form) != 2:
            return jsonify(Error="Malformed post request"), 400
        else:
            gchat_name = form['gchat_name']
            person_id = form['person_id']
            if gchat_name and person_id:
                dao = GroupChatDAO()
                gchat_id = dao.insertGroupChat(gchat_name, person_id)
                result = self.mapToGroupChatDict(gchat_id, gchat_name, person_id)
                return jsonify(GroupChat=result), 201
            else:
                return jsonify(Error="Unexpected attributes in post request"), 400

    def insertToGroupChat(self, form):
        if len(form) != 2:
            return jsonify(Error="Malformed post request"), 400
        else:
            gchat_id = form['gchat_id']
            person_id = form['person_id']
            if gchat_id and person_id:
                dao = GroupChatDAO()
                member_id = dao.insertMember(gchat_id, person_id)
                result = self.mapToGroupChatDict(member_id, gchat_id, person_id)
                return jsonify(GroupChat=result), 201
            else:
                return jsonify(Error="Unexpected attributes in post request"), 400

