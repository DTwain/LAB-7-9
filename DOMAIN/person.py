from DOMAIN.address import address_class
class person_class(address_class):
    def __init__(self, id, name, country, city, street, number):
        self.__id = id
        self.__name = name
        address_class.__init__(self, country, city, street, number)
        self.__events = []

    def add_event_to_person(self, id_event):
        self.__events.append(id_event)

    def get_person_id(self):
        return self.__id
    
    def get_person_name(self):
        return self.__name
    
    def get_events(self):
        return self.__events

    def __str__(self):
        address_info = super().__str__()
        return self.__id + " | " + self.__name + " | " + address_info + " | " + str(self.__events)

    