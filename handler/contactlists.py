from flask import jsonify, request
from dao.contactlistDao import ContactListDAO
from handler.users import UserHandler

class ContactListHandler:
    def getAllContactList(self):
        dao = ContactListDAO()
        result = dao.getAllContactList()
        mapped_result = []
        for r in result:
            mapped_result.append(self.mapToContactListDict(r))
        return jsonify(ContactLists=mapped_result)

    def getContactListByUserId(self, id):
        dao = ContactListDAO()
        result = dao.getContactListByUserID(id)
        if result == None:
            return jsonify(Error="NOT FOUND"), 404
        else :
            mapped = self.mapToContactListDict(result)
            return jsonify(User=mapped)

    def mapToContactListDict(self, row):
        result = {}
        result["owner_id"] = row[0]
        result["contacts"] = row[1]
        return result

    def getSingleContactByUserId(self, id):
        handler = UserHandler()
        dao = ContactListDAO()
        result = dao.getSingleContactByUserID(id)
        if result == None:
            return jsonify(Error="NOT FOUND"), 404
        else :
            mapped = handler.mapToUserDict(result)
            return jsonify(User=mapped)
