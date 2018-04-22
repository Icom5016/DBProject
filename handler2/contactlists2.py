from flask import jsonify, request
from dao2.contactlistDao2 import ContactListDAO
from handler2.users2 import UserHandler

class ContactListHandler:
    def getAllContactList(self):
        dao = ContactListDAO()
        result = dao.getAllContactList()
        mapped_result = []
        for r in result:
            mapped_result.append(self.mapToContactListDict(r))
        return jsonify(ContactLists=mapped_result)

    def getContactListByID(self, clist_id):
        dao = ContactListDAO()
        result = dao.getContactListByID(clist_id)
        if result == None:
            return jsonify(Error="NOT FOUND"), 404
        else :
            mapped = self.mapToContactListDict(result)
            return jsonify(User=mapped)

    def getContactListByUserId(self, user_id):
        dao = ContactListDAO()
        result = dao.getContactListByUserID(user_id)
        if result == None:
            return jsonify(Error="NOT FOUND"), 404
        else :
            mapped = self.mapToContactListDict(result)
            return jsonify(User=mapped)

    def mapToContactListDict(self, row):
        result = {}
        result["clist_id"] = row[0]
        result["person_id"] = row[1]
        result["contacts"] = row[2]
        return result

    # def getSingleContactByUserId(self, user_id):
    #     handler = UserHandler()
    #     dao = ContactListDAO()
    #     result = dao.getSingleContactByUserID(user_id)
    #     if result == None:
    #         return jsonify(Error="NOT FOUND"), 404
    #     else :
    #         mapped = handler.mapToUserDict(result)
    #         return jsonify(User=mapped)
