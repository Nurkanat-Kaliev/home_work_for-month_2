# def check_admin(status):
#     def decorator(func):
#         def wrapper(*args):
#             balance = 0
#             if status == "admin":
#                 print(f"Access allowed for {status}")
#                 balance += 500
#                 print(f"Balance filled on {balance}$")
#                 return func(*args)
#
#
#             else:
#                 print(f"Access denied for {status}")
#                 print("balance remained unchanged")
#
#         return wrapper
#     return decorator
#
# @check_admin("arzy")
# def alien():
#     print("the user is banned")
#
# @check_admin("admin")
# def welcome():
#     print("Got the access")
#
# alien()
# welcome()
#
#




class User:
    def __init__(self,role,login):
        self.role = role
        self.login = login

admin = User("admin", "Kanat")
alien = User("Arzu", "Obanai")

def check_admin(obj_user):
    def decorator(func):
        def wrapper(*args):
                if obj_user.role == "admin":
                    print(f"Access allowed for {obj_user.login}")
                    return func(*args)
                else:
                    print(f"access denied for {obj_user.login}")

        return wrapper
    return decorator

@check_admin(admin)
def allowed():
    print("U can go")

@check_admin(alien)
def not_allowed():
    print("U cant go")
#
# allowed()
# not_allowed()


