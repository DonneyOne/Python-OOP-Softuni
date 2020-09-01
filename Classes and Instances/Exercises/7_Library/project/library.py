class Library:
    user_records = []
    books_available = {}
    rented_books = {}

    def add_user(self,user):
        if user not in Library.user_records:
            Library.user_records.append(user)
        else:
            return f"User with id = {user.user_id} already registered in the library!"

    def remove_user(self,user):

        if user in Library.user_records:
            Library.user_records.remove(user)
        else:
            return "We could not find such user to remove!"

    def change_username(self,user_id: int, new_username: str):

        for user in Library.user_records:
            if user.user_id == user_id and new_username != user.username:
                user.username = new_username
                return f"Username successfully changed to: {user.username} for user id: {user.user_id}"
            elif user.user_id == user_id and new_username == user.username:
                return "Please check again the provided username - it should be different than the username used so " \
                       "far! "
            else:
                return f"There is no user with id = {user_id}!"


