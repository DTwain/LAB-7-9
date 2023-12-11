from DOMAIN.address import address_class
from DOMAIN.person_event import person_event_class
class person_class(address_class):
    def __init__(self, id, name, country, city, street, number, shared_person_event_class):
        self.__id = id
        self.__name = name
        address_class.__init__(self, country, city, street, number)
        self.shared_person_event_class = shared_person_event_class

    def get_person_id(self):
        return self.__id
    
    def get_person_name(self):
        return self.__name
    
    def set_person_name(self, new_name):
        self.__name = new_name

    def add_person_to_event(self, event_id):
        self.shared_person_event_class.add_person_to_event(self.__id, event_id)

    def remove_any_connections_with_person_id(self):
        self.shared_person_event_class.remove_person_id_from_all_lists(self.__id)

    def get_number_of_events_person_joined(self):
        return self.shared_person_event_class.get_number_of_events_person_joined(self.__id)
    
    def get_event_ids_that_corespond_to_person_id(self):
        return self.shared_person_event_class.get_event_ids_that_corespond_to_person_id(self.__id)

    def get_list_of_events_ids_that_person_joined(self):
        return self.shared_person_event_class.get_list_of_events_ids_that_person_joined(self.__id)
    
    def __eq__(self, other) -> bool:
        return self.__id == other.__id
    
    def __str__(self):
        address_info = address_class.__str__(self)
        number_of_events_person_joined = self.shared_person_event_class.get_number_of_events_person_joined(self.__id)
        return "ID:        " + self.__id + "\nNume:      " + self.__name + "\n" + address_info + "\nNr. evenimente: " + str(number_of_events_person_joined)
    

    