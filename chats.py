from datetime import datetime
from file_manager import chat_manager
from auth import get_active_user


class Chat:
    def __init__(self, name, password):
        self.phone_number = get_active_user()[1]
        self.name = name
        self.password = password
        self.group_id = self.get_new_group_id()
        self.created_at = datetime.now()

    @staticmethod
    def get_new_group_id() -> int:
        chats = chat_manager.read()
        if len(chats) == 1:
            return 1
        else:
            return int(chats[-1][1]) + 1

    def get_object_as_list(self):
        return [self.name, self.password]


def create_new_chat():
    name = input("Enter group name: ")
    password = input("Enter group password: ")
    chat = Chat(name, password)
    chat_manager.append(row=chat.get_object_as_list())
    return chat

def show_all_chats():
    chats = chat_manager.read()
    if len(chats) <= 1:
        print("No chats available.")
    else:
        for chat in chats[1:]:
            print(f"Group ID: {chat[1]}, Group Name: {chat[3]}")



def join_chat_by_id():
    chat_id = input("Enter group ID: ")
    password = input("Enter group password: ")

    chats = chat_manager.read()
    for chat in chats[1:]:
        if chat[1] == chat_id and chat[2] == password:
            print(f"Successfully joined chat '{chat[3]}'")
            return True
    print("Invalid group ID or password")
    return False


def show_my_chats():
    active_user = get_active_user()
    if not active_user:
        print("No active user found.")
        return

    my_chats = [chat for chat in chat_manager.read()[1:] if chat[0] == active_user[1]]

    if not my_chats:
        print("You have not created any chats.")
    else:
        for chat in my_chats:
            print(f"Group ID: {chat[1]}, Group Name: {chat[3]}")
