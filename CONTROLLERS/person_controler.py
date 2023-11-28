from DOMAIN.person import person_class

class person_controler:
    def __init__(self, repo_pers, pers_validator):
        self.__repo_person = repo_pers
        self.__person_validator = pers_validator

    def add_person(self, id, name, country, city, street, number_of_the_house):
        person_obj = person_class(id, name, country, city, street, number_of_the_house)
        self.__person_validator.person_validation(person_obj)
        self.__repo_person.add_person_to_rep(person_obj, id)
        return person_obj
    
    def add_event_to_person(self, id_person, id_event):
        """
        TREBUIE VERIFICAT NEAPARAT DACA EXISTA ID-UL PERSOANEI SI ID-UL EVENIMENTULUI
        TREBUIE VERIFICAT NEAPARAT DACA ID-UL EVENIMENTULUI NU EXISTA DEJA IN LISTA DE EVENIMENTE A PERSOANEI
        CUM VERIFICAM DACA ID-UL EVENIMENTULUI EXISTA IN LISTA DE EVENIMENTE A PERSOANEI?
        """
        self.__repo_person.add_event_to_entity(id_person, id_event)

    def remove_person(self, id):
        removed_person  = self.__repo_person.remove_person(id)
        return removed_person
    
    def update_person(self, id, name, country, city, street, number_of_the_house):
        new_person_obj = person_class(id, name, country, city, street, number_of_the_house)
        self.__person_validator.person_validation(new_person_obj)
        preupdate_person = self.__repo_person.update_person(new_person_obj, id)
        return preupdate_person
    
    def afisare_persoane(self):
        self.__repo_person.output()
    



    