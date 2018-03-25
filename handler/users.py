from flask import jsonify, request
from dao.userDao import UserDAO

class UserHandler:
    def getAllUser(self):
        dao = UserDAO()
        result = dao.getAllUser()
        mapped_result = []
        for r in result:
            mapped_result.append(self.mapToUserDict(r))
        return jsonify(User=mapped_result)

    def getUserById(self, id):
        dao = UserDAO()
        result = dao.getUserById(id)
        if result == None:
            return jsonify(Error="NOT FOUND"), 404
        else :
            mapped = self.mapToUserDict(result)
            return jsonify(User=mapped)

    def mapToUserDict(self, row):
        result = {}
        result["user_id"] = row[0]
        result["first_name"] = row[1]
        result["last_name"] = row[2]
        result["email"] = row[3]
        result["phone"] = row[4]
        return result

    def getFNameByUserId(self, id):
        print("DEBUG - users: getName")
        dao = UserDAO()
        result = dao.getFNameByUserId(id)
        if result == None:
            return jsonify(Error="NOT FOUND"), 404
        else :
            mapped = self.mapToFNameDict(result)
            return jsonify(FirstName=mapped)

    def mapToFNameDict(self, row):
        print("DEBUG - users: MapToDict")
        result = {}
        result["first_name"] = row
        return result

    def getLNameByUserId(self, id):
        dao = UserDAO()
        result = dao.getLNameByUserId(id)
        if result == None:
            return jsonify(Error="NOT FOUND"), 404
        else :
            mapped = self.mapToLNameDict(result)
            return jsonify(LastName=mapped)

    def mapToLNameDict(self, row):
        result = {}
        result["last_name"] = row
        return result

    def getEmailByUserId(self, id):
        dao = UserDAO()
        result = dao.getEmailByUserId(id)
        if result == None:
            return jsonify(Error="NOT FOUND"), 404
        else :
            mapped = self.mapToEmailDict(result)
            return jsonify(Email=mapped)

    def mapToEmailDict(self, row):
        result = {}
        result["email"] = row
        return result

    def getPhoneByUserId(self, id):
        dao = UserDAO()
        result = dao.getPhoneByUserId(id)
        if result == None:
            return jsonify(Error="NOT FOUND"), 404
        else :
            mapped = self.mapToPhoneDict(result)
            return jsonify(Phone=mapped)

    def mapToPhoneDict(self, row):
        result = {}
        result["phone"] = row
        return result