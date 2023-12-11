from REPOSITORIES.repo_persoane import repo_people
from DOMAIN.person import person_class
from DOMAIN.person_event import person_event_class
class repo_file_people(repo_people):
    def __init__(self, file_name):
        super().__init__()
        self.__shared_person_event_class = person_event_class()
        self.__file_name = file_name
        self.__load_from_file()

    def __load_from_file(self):
        try:
            file = open(self.__file_name, "r")
        except IOError:
            return
        
        line = file.readline().strip()
        while line != "":
            line_elements = line.split(";")
            person = person_class(line_elements[0], line_elements[1], line_elements[2], line_elements[3], line_elements[4], line_elements[5], self.__shared_person_event_class)
            if len(line_elements) > 6:
                events_id = line_elements[6].split(',')
                for event_id in events_id:
                    person.add_person_to_event(event_id)
            super().add_person_to_rep(person)
            line = file.readline().strip()
        file.close()

    def __store_to_file(self):
        try:
            file = open(self.__file_name, "w")
        except IOError:
            return
        list_of_people = super().get_all()
        for person in list_of_people:
            person_as_string = person.get_person_id() + ';' + person.get_person_name()
            person_as_string += ';' + person.get_country() + ';' + person.get_city() + ";" + person.get_street() + ";"
            person_as_string += person.get_number_of_the_house()
            if str(person.get_list_of_events_ids_that_person_joined()) != '':
                person_as_string += ";" + str(person.get_list_of_events_ids_that_person_joined()) + '\n'
            file.write(person_as_string)
        file.close()

    def add_person_to_rep(self, person):
        super().add_person_to_rep(person)
        self.__store_to_file()
    
    def remove_person(self, id):
        erased_person = super().remove_person(id)
        self.__store_to_file()
        return erased_person
    
    def update_person(self, new_person, new_person_id):
        old_person = super().update_person(new_person, new_person_id)
        self.__store_to_file()
        return old_person
    
    def get_person_through_id(self, person_id):
        return super().get_person_through_id(person_id)
    
    def get_list_of_DTO_objs(self):
        return super().get_list_of_DTO_objs()
    
    def get_all(self):
        return super().get_all()
    
    def get_all_ids(self):
        return super().get_all_ids()
    
    def size(self):
        return super().size()
    
    def output(self):
        return super().output()


    