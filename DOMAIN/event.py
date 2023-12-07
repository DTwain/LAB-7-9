class event_class:
    def __init__(self, id, date, duration, description):
        self.__id = id
        self.__date = date
        self.__duration = duration
        self.__description = description
        self.__number_of_people_joined = 0

    def get_event_id(self):
        return self.__id
    
    def get_event_date(self):
        return self.__date
    
    def get_event_duration(self):
        return self.__duration
    
    def get_event_description(self):
        return self.__description
    
    def get_number_of_people_joined(self):
        return self.__number_of_people_joined
    
    def inc_number_of_participants(self):
        self.__number_of_people_joined += 1

    def set_event_date(self, new_date):
        self.__date = new_date
    
    def set_event_duration(self, new_duration):
        self.__duration = new_duration
    
    def set_event_description(self, new_description):
        self.__description = new_description

    def set_number_of_people_joined(self, value):
        self.__number_of_people_joined = value

    def __eq__(self, obj) -> bool:
        return self.__id == obj.__id 
        
    def __str__(self):
        return "ID:          " + self.__id + "\nData:        " + self.__date + "\nDurata:      " + self.__duration + " minute\nDescriere:   " + self.__description + "\nNr. persoane inscrise:    " + str(self.__number_of_people_joined)
    

    