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
        self.__event_controler.inc_number_of_people_joined_to_event(event_id)
        person_obj.add_event_to_person(event_id)
        self.__repo_person.update_person(person_obj, person_obj.get_person_id())
    
    def find_person_by_id(self, person_id):
        return self.__repo_person.get_person_through_id(person_id)
    
    def find_people_using_key_words(self, list_of_key_words):
        people = self.__repo_person.get_all()
        for person in people:
            person_id = person.get_person_id().lower()
            person_name = person.get_person_name().lower()
            person_country = person.get_country().lower()
            person_city = person.get_city().lower()
            person_street = person.get_street().lower()
            person_number_of_the_house = person.get_number_of_the_house().lower()
            for key_word in list_of_key_words:
                key_word = key_word.lower()
                if key_word == person_id or key_word in person_name or key_word in person_country or key_word in person_city or key_word in person_street or key_word == person_number_of_the_house:
                    yield person
                    break
            # what is yield? https://stackoverflow.com/questions/231767/what-does-the-yield-keyword-do
    
    def output_people(self):
        self.__repo_person.output()
    



    