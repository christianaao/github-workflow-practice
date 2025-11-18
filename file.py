def print_hello():
    """
    Return
        hello world
    """
    print("hello world")


print_hello()


class User:
    """
    Arg
        name
    Return
        user dict
    """

    def __init__(self, name):
        self.name = name

    def state_name(self):
        print(self.name)


def create_user():
    user1 = User(input("What is your name? "))
    user1.state_name()
    print(type(user1))


create_user()
