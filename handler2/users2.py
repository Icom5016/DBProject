from flask import jsonify
from dao2.userDao2 import UserDAO
from dao.chatMembersDao import ChatMembersDAO


class UserHandler:
    def getAllUser(self):
        dao = UserDAO()
        result = dao.getAllUser()
        mapped_result = []
        for r in result:
            mapped_result.append(self.mapToUserDict(r))
        return jsonify(User=mapped_result)

    def getUserById(self, user_id):
        dao = UserDAO()
        result = dao.getUserById(user_id)
        if result == None:
            return jsonify(Error="NOT FOUND"), 404
        else:
            mapped = self.mapToUserDict(result)
            return jsonify(User=mapped)

    #####REMVD USRNM ATT
    # def getUserByName(self, username):
    #     dao = UserDAO()
    #     result = dao.getUserByName(username)
    #     if result == None:
    #         return jsonify(Error="NOT FOUND"), 404
    #     else:
    #         mapped = self.mapToUserDict(result)
    #         return jsonify(User=mapped)

    def mapToUserDict(self, row):
        result = {}
        result["user_id"] = row[0]
        result["first_name"] = row[1]
        result["last_name"] = row[2]
        result["email"] = row[3]
        result["phone"] = row[4]
        result["password"] = row[5]
        return result

    def getFNameByUserId(self, user_id):
        dao = UserDAO()
        result = dao.getFNameByUserId(user_id)
        if result == None:
            return jsonify(Error="NOT FOUND"), 404
        else:
            mapped = self.mapToFNameDict(result)
            return jsonify(FirstName=mapped)

    # def getFNameByName(self, username):
    #     dao = UserDAO()
    #     result = dao.getFNameByName(username)
    #     if result == None:
    #         return jsonify(Error="NOT FOUND"), 404
    #     else:
    #         mapped = self.mapToFNameDict(result)
    #         return jsonify(FirstName=mapped)

    def mapToFNameDict(self, row):
        result = {}
        result["first_name"] = row[0]
        return result

    def getLNameByUserId(self, user_id):
        dao = UserDAO()
        result = dao.getLNameByUserId(user_id)
        if result == None:
            return jsonify(Error="NOT FOUND"), 404
        else:
            mapped = self.mapToLNameDict(result)
            return jsonify(LastName=mapped)

    ####REMOVED USERNAME ATTRIBUTE
    # def getLNameByName(self, username):
    #     dao = UserDAO()
    #     result = dao.getLNameByName(username)
    #     if result == None:
    #         return jsonify(Error="NOT FOUND"), 404
    #     else:
    #         mapped = self.mapToLNameDict(result)
    #         return jsonify(LastName=mapped)

    def mapToLNameDict(self, row):
        result = {}
        result["last_name"] = row[0]
        return result

    def getEmailByUserId(self, user_id):
        dao = UserDAO()
        result = dao.getEmailByUserId(user_id)
        if result == None:
            return jsonify(Error="NOT FOUND"), 404
        else:
            mapped = self.mapToEmailDict(result)
            return jsonify(Email=mapped)

    def getEmailByName(self, username):
        dao = UserDAO()
        result = dao.getEmailByName(username)
        if result == None:
            return jsonify(Error="NOT FOUND"), 404
        else:
            mapped = self.mapToEmailDict(result)
            return jsonify(Email=mapped)

    def mapToEmailDict(self, row):
        result = {}
        result["email"] = row[0]
        return result

    def getPhoneByUserId(self, user_id):
        dao = UserDAO()
        result = dao.getPhoneByUserId(user_id)
        if result == None:
            return jsonify(Error="NOT FOUND"), 404
        else:
            mapped = self.mapToPhoneDict(result)
            return jsonify(Phone=mapped)

    ##### RMVD URSNM ATT
    # def getPhoneByName(self, username):
    #     dao = UserDAO()
    #     result = dao.getPhoneByName(username)
    #     if result == None:
    #         return jsonify(Error="NOT FOUND"), 404
    #     else:
    #         mapped = self.mapToPhoneDict(result)
    #         return jsonify(FirstName=mapped)

    def mapToPhoneDict(self, row):
        result = {}
        result["phone"] = row[0]
        return result

    #### REMOVED USERNAME ATTRIBUTE
    # def getUsernameByUserId(self, user_id):
    #     dao = UserDAO()
    #     result = dao.getUsernameByUserId(user_id)
    #     if result == None:
    #         return jsonify(Error="NOT FOUND"), 404
    #     else:
    #         mapped = self.mapToUsernameDict(result)
    #         return jsonify(Username=mapped)
    #
    # def mapToUsernameDict(self, row):
    #     result = {}
    #     result["username"] = row
    #     return result

    def getPasswordByUserId(self, user_id):
        dao = UserDAO()
        result = dao.getPasswordByUserId(user_id)
        if result == None:
            return jsonify(Error="NOT FOUND"), 404
        else:
            mapped = self.mapToPasswordDict(result)
            return jsonify(Password=mapped)

    def mapToPasswordDict(self, row):
        result = {}
        result["password"] = row[0]
        return result

    def getChatsOfUser(self, user_id):
        dao = ChatMembersDAO()
        result = dao.getChatsByUser(user_id)
        if result == None:
            return jsonify(Error="NOT FOUND"), 404
        mapped_result = []
        for r in result:
            mapped_result.append(self.mapToChatsDict(r))
        return jsonify(Groupchats=mapped_result)

    def mapToChatsDict(self, row):
        result = {}
        result["gchat_id"] = row[0]
        result["gchat_name"] = row[1]
        result["owner"] = row[2]
        return result

    def getLikedMsgByUserId(self, user_id):
        dao = UserDAO()
        result = dao.getLikedMsgByUserId(user_id)
        mapped_result = []
        for r in result:
            mapped_result.append(self.mapToMsgDict(r))
        return jsonify(LikedMessages=mapped_result)

    def getDislikedMsgByUserId(self, user_id):
        dao = UserDAO()
        result = dao.getDislikedMsgByUserId(user_id)
        mapped_result = []
        for r in result:
            mapped_result.append(self.mapToMsgDict(r))
        return jsonify(DislikedMessages=mapped_result)

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