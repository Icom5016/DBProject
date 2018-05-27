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
            mapped_result = []
            for r in result:
                mapped_result.append(self.mapToUserDict(r))
            return jsonify(Contacts=mapped_result)

    def mapToContactListDict(self, row):
        result = {}
        result["clist_id"] = row[0]
        result["person_id"] = row[1]
        result["contacts"] = row[2]
        return result

    def getContactsByUserID(self, user_id):
        dao = ContactListDAO()
        result = dao.getContactsByUserID(user_id)
        mapped_result = []
        for r in result:
            mapped_result.append(self.mapToUserDict(r))
        return jsonify(Users=mapped_result)

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

    # def getSingleContactByUserId(self, user_id):
    #     handler = UserHandler()
    #     dao = ContactListDAO()
    #     result = dao.getSingleContactByUserID(user_id)
    #     if result == None:
    #         return jsonify(Error="NOT FOUND"), 404
    #     else :
    #         mapped = handler.mapToUserDict(result)
#         return jsonify(User=mapped)

    def insertContactList(self, form):
        if len(form) != 1:
            return jsonify(Error="Malformed post request"), 400
        else:
            person_id = form['person_id']
            if person_id:
                dao = ContactListDAO()
                clist_id = dao.insertContactList(person_id)
                result = self.mapToContactListDict([clist_id, person_id, None])
                return jsonify(ContactList=result), 201
            else:
                return jsonify(Error="Unexpected attributes in post request"), 400

    def insertContact(self, form):
        if len(form) != 2:
            return jsonify(Error="Malformed post request"), 400
        else:
            clist_id = form['clist_id']
            person_id = form['person_id']
            if clist_id and person_id:
                dao = ContactListDAO()
                contact_id = dao.insertContact(clist_id, person_id)
                result = self.mapToContact([contact_id, clist_id, person_id])
                return jsonify(Contact=result), 201
            else:
                return jsonify(Error="Unexpected attributes in post request"), 400

    def mapToContactDict(self, row):
        result = {}
        result['contact_id'] = row[0]
        result['clist_id'] = row[1]
        result['person_id'] = row[2]
        return result

    def deleteContactList(self, form):
        if len(form) != 1:
            return jsonify(Error="Malformed post request"), 400
        else:
            clist_id = form['clist_id']
            if clist_id:
                dao = ContactListDAO()
                dao.deleteContactList(clist_id)
                return jsonify(DeleteStatus="OK"), 200

    def deleteContact(self, form):
        if len(form) != 1:
            return jsonify(Error="Malformed post request"), 400
        else:
            contact_id = form['contact_id']
            if contact_id:
                dao = ContactListDAO()
                dao.deleteContact(contact_id)
                return jsonify(DeleteStatus="OK"), 200