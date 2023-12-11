from DOMAIN.person_event import person_event_class
class event_class:
    def __init__(self, id, date, duration, description, shared_person_event_class):
        self.__id = id
        self.__date = date
        self.__duration = duration
        self.__description = description
        self.shared_person_event_class = shared_person_event_class

    def get_event_id(self):
        return self.__id
    
    def get_event_date(self):
        return self.__date
    
    def get_event_duration(self):
        return self.__duration
    
    def get_event_description(self):
        return self.__description
    
    def set_event_date(self, new_date):
        self.__date = new_date
    
    def set_event_duration(self, new_duration):
        self.__duration = new_duration
    
    def set_event_description(self, new_description):
        self.__description = new_description

    def add_person_to_event(self, person_id):
        self.shared_person_event_class.add_person_to_event(person_id, self.__id)
    
    def remove_any_connections_with_event_id(self):
        self.shared_person_event_class.remove_event_id_from_all_lists(self.__id)

    def get_number_of_people_joined_to_event(self):
        return self.shared_person_event_class.get_number_of_people_joined_to_event(self.__id)
    
    def get_list_of_people_ids_that_joined_event(self):
        return self.shared_person_event_class.get_list_of_people_ids_that_joined_event(self.__id)
    
    def __eq__(self, obj) -> bool:
        return self.__id == obj.__id 
        
    def __str__(self):
        number_of_people_joined_to_event = self.shared_person_event_class.get_number_of_people_joined_to_event(self.__id)
        return "ID:           " + self.__id + "\nData:         " + self.__date + "\nDurata:       " + self.__duration + " minute\nDescriere:    " + self.__description + "\nNr. persoane: " + str(number_of_people_joined_to_event)
    

    