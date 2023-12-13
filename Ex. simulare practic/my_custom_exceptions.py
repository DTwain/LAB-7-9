class already_in_repo(Exception):
    def __init__(self, id):
        self.__msg = f"Robotul cu id- ul < {id} > este deja adaugat"

    def __str__(self):
        return self.__msg
    
class inexistent_robot(Exception):
    def __init__(self, id):
        self.__msg = f"Robotul cu id- ul < {id} > nu exista"

    def __str__(self):
        return self.__msg
