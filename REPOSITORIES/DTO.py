class DTO_for_second_report:
    def __init__(self, id_person, number_of_events):
        self.__id_person = id_person
        self.__number_of_events = number_of_events
    
    def get_person_id(self):
        return self.__id_person
    
    def get_number_of_events(self):
        return int(self.__number_of_events)
    

class DTO_for_third_report:
    def __init__(self, id_event, number_of_people):
        self.__id_event = id_event
        self.__number_of_people = number_of_people
    
    def get_event_id(self):
        return self.__id_event
    
    def get_number_of_people(self):
        return self.__number_of_people
    
    def __str__(self) -> str:
        return self.__id_event + " | " + str(self.__number_of_people)
    
