class FileNotFoundPS(Exception):
    print("Errno 20: File not found!!")

class NoneTypeErrorPS(Exception):
    print("The command cannot None!!")

class EnetErrorPS(Exception):
    print("The [name, path] enet is error!!")