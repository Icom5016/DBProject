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
        chat_members = []
        for r in self.data:
            if chatId != r[0]:
                chatId = r[0]
                for r2 in self.data:
                    if chatId == r2[0]:
                        memberId = r2[1]
                        chat_members.append(dao.getUserById(memberId))
                result.append([chatId, chat_members])
                chat_members = []
        if result == []:
            return None
        return result

    def getAllChatMembersByChatID(self, gchat_id):
        dao = UserDAO()
        result = []
        chat_members = []
        for r in self.data:
            if gchat_id == r[0]:
                member_id = r[1]
                chat_members.append(dao.getUserById(member_id))
        result.append(gchat_id)
        result.append(chat_members)
        if chat_members == []:
            return None
        return result