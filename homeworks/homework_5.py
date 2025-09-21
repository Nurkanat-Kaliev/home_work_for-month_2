def check_admin(status):
    def functions(func):
        def wrapper(*args):
            balance = 0
            if status == "admin":
                print(f"Access allowed for {status}")
                balance += 500
                print(f"Balance filled on {balance}$")

            else:
                print(f"Access denied for {status}")
                print("balance remained unchanged")

            return func(*args)
        return wrapper
    return functions

@check_admin("arzy")
def alien():
    print("the user is banned")

@check_admin("admin")
def welcome():
    print("Got the access")

alien()
welcome()


