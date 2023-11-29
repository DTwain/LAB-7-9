from REPOSITORIES.repo_custom_exceptation import dublicated_id_exception 
from REPOSITORIES.repo_custom_exceptation import inexistent_id_exception
from REPOSITORIES.DTO import DTO_for_second_report
class repo_people:
    def __init__(self):
        self.__repo_people = {}

    def add_person_to_rep(self, person):
        if person.get_person_id() not in self.__repo_people:
            self.__repo_people[person.get_person_id()] = person
        else:
            raise dublicated_id_exception(id)

    def remove_person(self, id):
        if id not in self.__repo_people:
            raise inexistent_id_exception(id)
        removed_person = self.__repo_people[id]
        del self.__repo_people[id]
        return removed_person
        
    def update_person(self, updated_person, id):
        if id not in self.__repo_people:
            raise inexistent_id_exception(id)
        preupdate_person = self.__repo_people[id]
        self.__repo_people[id] = updated_person
        return preupdate_person
    
    def get_person_through_id(self, person_id):
        if person_id not in self.__repo_people:
            raise inexistent_id_exception(person_id)
        return self.__repo_people[person_id]

    def get_list_of_DTO_objs(self):
        list_with_number_of_events_person_joined = []
        for person_id in self.__repo_people:
            person = repo_people.get_person_through_id(self, person_id)
            DTO_id_person_number_of_events = DTO_for_second_report(person.get_person_id(), person.number_of_event_added())
            list_with_number_of_events_person_joined.append(DTO_id_person_number_of_events)
        return list_with_number_of_events_person_joined

    
    def size(self):
        return len(self.__repo_people)
    
    def output(self):
        for key, values in self.__repo_people.items():
            print(f"{key} : {values}")
        print("\n")
            