from REPOSITORIES.repo_custom_exceptation import dublicated_id_exception 
from REPOSITORIES.repo_custom_exceptation import inexistent_id_exception

class repo_people:
    def __init__(self):
        self.__repo_people = {}

    def add_person_to_rep(self, person):
        if person.get_person_id() not in self.__repo_people:
            self.__repo_people[person.get_person_id()] = person
        else:
            raise dublicated_id_exception(id)
        
    def add_event_to_entity(self, id_person, id_event):
        if id_person not in self.__repo_people:
            raise inexistent_id_exception(id_person)
        person = self.__repo_people[id_person]
        person.add_event_to_person(id_event)

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
    
    def size(self):
        return len(self.__repo_people)
    
    def get_events_of_person(self, id):
        if id not in self.__repo_people:
            raise inexistent_id_exception(id)
        person = self.__repo_people[id]
        return person.get_events()
    def output(self):
        for key, values in self.__repo_people.items():
            print(f"{key} : {values}")
        print("\n")
            