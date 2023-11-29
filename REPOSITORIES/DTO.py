class DTO_for_second_report:
    def __init__(self, id_person, number_of_events):
        self.__id_person = id_person
        self.__number_of_events = number_of_events
    
    def get_person_id(self):
        return self.__id_person
    
    def get_number_of_events(self):
        return int(self.__number_of_events)
    
