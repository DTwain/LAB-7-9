from MY_CUSTOM_EXCEPTIONS.repo_custom_exception import person_added_twice_to_event
class person_event_class:
    def __init__(self):
        self.__personID_to_list_of_events = {}
        self.__eventID_to_list_of_people = {}

    def add_person_to_event(self, person_id, event_id):
        if person_id not in self.__personID_to_list_of_events:
            self.__personID_to_list_of_events[person_id] = []
        if event_id not in self.__eventID_to_list_of_people:
            self.__eventID_to_list_of_people[event_id] = []
        if person_id not in self.__eventID_to_list_of_people[event_id]:
            self.__eventID_to_list_of_people[event_id].append(person_id)
        else:
            raise person_added_twice_to_event(person_id)
        
        self.__personID_to_list_of_events[person_id].append(event_id) 

    def remove_person_id_from_all_lists(self, person_id):
        for event_id in self.__eventID_to_list_of_people:
            if person_id in self.__eventID_to_list_of_people[event_id]:
                self.__eventID_to_list_of_people[event_id].remove(person_id)
        if person_id in self.__personID_to_list_of_events:
            del self.__personID_to_list_of_events[person_id]

    def remove_event_id_from_all_lists(self, event_id):
        for person_id in self.__personID_to_list_of_events:
            if event_id in self.__personID_to_list_of_events[person_id]:
                self.__personID_to_list_of_events[person_id].remove(event_id)
        if event_id in self.__eventID_to_list_of_people:
            del self.__eventID_to_list_of_people[event_id]

    def get_number_of_people_joined_to_event(self, event_id):
        if event_id not in self.__eventID_to_list_of_people:
            return 0
        return len (self.__eventID_to_list_of_people[event_id])
    
    def get_number_of_events_person_joined(self, person_id):
        if person_id not in self.__personID_to_list_of_events:
            return 0
        return len(self.__personID_to_list_of_events[person_id])
    
    def get_event_ids_that_corespond_to_person_id(self, person_id):
        return self.__personID_to_list_of_events[person_id]
    
    def get_list_of_people_ids_that_joined_event(self, event_id):
        list_of_people_ids_as_string = ""
        if event_id in self.__eventID_to_list_of_people:
            for person_id in self.__eventID_to_list_of_people[event_id]:
                list_of_people_ids_as_string += person_id + ", "
            return list_of_people_ids_as_string[:-2]
        return ""
    
    def get_list_of_events_ids_that_person_joined(self, person_id):
        list_of_events_ids_as_string = ""
        if person_id in self.__personID_to_list_of_events:
            for event_id in self.__personID_to_list_of_events[person_id]:
                list_of_events_ids_as_string += event_id + ", "
            return list_of_events_ids_as_string[:-2]
        return ""
    
    def output_person_id_to_list_of_events_id(self):
        for key, values in self.__personID_to_list_of_events.items():
            print(f"person_id : {key} : {values}")
    
    def output_event_id_to_list_of_people_id(self):
        for key, values in self.__eventID_to_list_of_people.items():
            print(f"event_id : {key} : {values}")
    
