class repo_custom_exception(Exception):
    def __init__(self, error_message):
        self.__mesaj = error_message

    def __str__(self):
        return self.__mesaj
    
class dublicated_id_exception(repo_custom_exception):
    def __init__(self, id):
        super().__init__(f"ERROR: Id-ul exista deja in lista de persoane! < {id} >")

class inexistent_event_id_exception(repo_custom_exception):
    def __init__(self, id):
        super().__init__(f"EROOR: Id-ul evenimentului nu exista! < {id} >")

class inexistent_person_id_exception(repo_custom_exception):
    def __init__(self, id):
        super().__init__(f"EROOR: Id-ul persoanei nu exista! < {id} >")

class person_added_twice_to_event(repo_custom_exception):
    def __init__(self, id):
        super().__init__(f"EROOR: Persoana a mai fost introdusa odata la eveniment! < {id} >")

class no_other_event_to_add_to_person(repo_custom_exception):
    def __init__(self, id):
        super().__init__(f"EROOR: Nu se mai poate adauga un eveniment la persoana cu id-ul < {id} > ")

class no_event_to_delete_exception(repo_custom_exception):
    def __init__(self):
        super().__init__("EROOR: Nu exista evenimente adaugate!!")

class no_person_to_delete_exception(repo_custom_exception):
    def __init__(self):
        super().__init__("EROOR: Nu exista persone adaugate!!")