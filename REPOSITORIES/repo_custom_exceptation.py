class repo_custom_exceptation(Exception):
    def __init__(self, error_message):
        self.__mesaj = error_message

    def __str__(self):
        return self.__mesaj
    
class dublicated_id_exception(repo_custom_exceptation):
    def __init__(self, id):
        super().__init__(f"ERROR: Id-ul exista deja in lista de persoane! < {id} >")

    
class inexistent_id_exception(repo_custom_exceptation):
    def __init__(self, id):
        super().__init__(f"EROOR: Id-ul nu exista in lista de persoane! < {id} >")