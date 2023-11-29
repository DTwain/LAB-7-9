from DOMAIN.person import person_class

class person_controler:
    def __init__(self, repo_pers, pers_validator, event_controler):
        self.__repo_person = repo_pers
        self.__person_validator = pers_validator
        self.__event_controler = event_controler

    def add_person(self, id, name, country, city, street, number_of_the_house):
        person_obj = person_class(id, name, country, city, street, number_of_the_house)
        self.__person_validator.person_validation(person_obj)
        self.__repo_person.add_person_to_rep(person_obj)
        return person_obj
    
    def remove_person(self, id):
        removed_person  = self.__repo_person.remove_person(id)
        return removed_person
    
    def update_person(self, id, name, country, city, street, number_of_the_house):
        new_person_obj = person_class(id, name, country, city, street, number_of_the_house)
        self.__person_validator.person_validation(new_person_obj)
        preupdate_person = self.__repo_person.update_person(new_person_obj, id)
        return preupdate_person
    
    def add_event_to_person(self, person_id, event_id):
        if self.__event_controler.find_event_by_id(event_id):
            pass
        person_obj = self.__repo_person.get_person_through_id(person_id)
        person_obj.add_event_to_person(event_id)
        self.__repo_person.update_person(person_obj, person_obj.get_person_id())
    
    def find_person_by_id(self, person_id):
        return self.__repo_person.get_person_through_id(person_id)
    
    def afisare_persoane(self):
        self.__repo_person.output()
    



    