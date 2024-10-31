from auth import login, logout, register
from chats import create_new_chat,show_my_chats,show_all_chats,join_chat_by_id


def show_auth_menu():
    print("""
    1. Login
    2. Register
    3. Exit
    """)
    choice = input("Enter your choice: ")
    if choice == "1":
        user = login()
        if user:
            print(f"Welcome to main menu, {user[0]}")
            return show_main_menu()
        else:
            print("Invalid phone or password")
            return show_auth_menu()
    elif choice == "2":
        if register():
            print("Please login")
            return show_auth_menu()
        else:
            print("Something went wrong while registering")
    elif choice == "3":
        print("Good bye")
    else:
        print("Invalid choice")
    show_auth_menu()


def show_main_menu():
    print("""
    1. Create new chat
    2. Show all chats
    3. Join chat by ID
    4. Show my chats
    5. Logout
    """)

    choice = input("Enter your choice: ")
    if choice == "1":
        chat = create_new_chat()
        print(f"New group is created with ID: {chat.group_id}, NAME: {chat.name}, PASS: {chat.password}")
    elif choice == "2":
        show_all_chats()
    elif choice == "3":
        join_chat_by_id()
    elif choice == "4":
        show_my_chats()
    elif choice == "5":
        logout()
        return show_auth_menu()
    return show_main_menu()



if __name__ == "__main__":
    from file_manager import users_manager, chat_manager, message_manager

    users_manager.write_headers(headers=['full_name', 'phone', 'password', 'created_at', 'is_active'])
    message_manager.write_headers(headers=['sender_phone_number', 'full_name', 'group_id', 'created_at'])
    chat_manager.write_headers(headers=['phone_number', 'group_id', 'password', 'name', 'created_at'])
    show_auth_menu()
