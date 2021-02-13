from person import Person
from utils import add
name = "Jamil"
name2 = "Jamila"


def hello(name: str):
    print(name.upper())


def hello2(name: str):
    print(name.upper())


def alexMethod():
    p = Person("Alex")
    print(p)


if __name__ == '__main__':
    # TODO: Fix Bug
    # TODO: Implement Test
    print("PYCHARM IS AWESOME")
    print("I love you")
    name = "David"
    print("%s" % name)
    print(add(2, 2))
    alexMethod()
