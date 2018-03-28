from dao.userDao import UserDAO

class ChatMembersDAO:
    def __init__(self):
        #[chat id, member id, primery key(chatid, memberid)]
        #John's chat w/ sam and kelly
        CM1 = [0, 117, [0, 117]]
        CM2 = [0, 34, [0, 34]]
        CM3 = [0, 87, [0, 87]]
        #Kelly's chat with John
        CM4 = [1, 87, [1, 87]]
        CM5 = [1, 117, [1, 117]]
        #Halsey's chat with john, sam, kelly
        CM6 = [2, 10, [2, 10]]
        CM7 = [2, 117, [2, 117]]
        CM8 = [2, 34, [2, 34]]
        CM9 = [2, 87, [2, 87]]

        self.data = []
        self.data.append(CM1)
        self.data.append(CM2)
        self.data.append(CM3)
        self.data.append(CM4)
        self.data.append(CM5)
        self.data.append(CM6)
        self.data.append(CM7)
        self.data.append(CM8)
        self.data.append(CM9)

    def getAllChatsAndMembers(self):
        dao = UserDAO()
        result = []
        chatId = -1
        chatMembers = []
        for r in self.data:
            if chatId != r[0]:
                chatId = r[0]
                for r2 in self.data:
                    if chatId == r2[0]:
                        memberId = r2[1]
                        chatMembers.append(dao.getUserById(memberId))
                result.append([chatId, chatMembers])
                chatMembers = []
        if result == []:
            return None
        return result

    def getAllChatMembersByChatID(self, chat_id):
        dao = UserDAO()
        result = []
        chatMembers = []
        for r in self.data:
            if chat_id == r[0]:
                memberId = r[1]
                chatMembers.append(dao.getUserById(memberId))
        result.append(chat_id)
        result.append(chatMembers)
        if chatMembers == []:
            return None
        return result

    # def getContactListByUserID(self, id):
    #     dao = UserDAO()
    #     result = []
    #     ownerId = id
    #     contacts = []
    #     for r in self.data:
    #         if ownerId == r[1]:
    #             contactId = r[2]
    #             contacts.append(dao.getUserById(contactId))
    #     result.append(ownerId)
    #     result.append(contacts)
    #     if contacts == []:
    #         return None
    #     return result