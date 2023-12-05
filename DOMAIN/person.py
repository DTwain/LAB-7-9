from DOMAIN.address import address_class
class person_class(address_class):
    def __init__(self, id, name, country, city, street, number):
        self.__id = id
        self.__name = name
        super().__init__(country, city, street, number)
        self.__joined_events = []

    def get_person_id(self):
        return self.__id
    
    def get_person_name(self):
        return self.__name
    
    def get_events_id(self):
        return self.__joined_events
    
    def set_person_name(self, new_name):
        self.__name = new_name

    def add_event_to_person(self, id_event):
        self.__joined_events.append(id_event)

    def number_of_events_added(self):
        return len(self.__joined_events)

    def __str__(self):
        address_info = super().__str__()
        joined_events_as_str = "[" + ", ".join(map(str, self.__joined_events)) + "]"
        return "ID:        " + self.__id + "\nName:      " + self.__name + "\n" + address_info + "\nID - urile ev. la care participa: " + joined_events_as_str

    