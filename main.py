import pyfiglet


def make_greeting(name):
    return f"Hello, {name}!"


print(pyfiglet.figlet_format(make_greeting("Viki")))
