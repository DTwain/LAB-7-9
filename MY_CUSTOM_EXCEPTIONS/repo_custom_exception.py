class repo_custom_exception(Exception):
    def __init__(self, error_message):
        self.__mesaj = error_message

    def __str__(self):
        return self.__mesaj
    
class dublicated_id_exception(repo_custom_exception):
    def __init__(self, id):
        super().__init__(f"ERROR: Id-ul exista deja in lista de persoane! < {id} >")

    
class inexistent_id_exception(repo_custom_exception):
    def __init__(self, id):
        super().__init__(f"EROOR: Id-ul nu exista! < {id} >")

class event_added_twice_to_person(repo_custom_exception):
    def __init__(self, id):
        super().__init__(f"EROOR: Id-ul a mai fost introdus odata! < {id} >")

class no_other_event_to_add_to_person(repo_custom_exception):
    def __init__(self):
        super().__init__(f"EROOR: Nu se mai poate adauga un eveniment la o persoana ")