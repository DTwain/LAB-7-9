class event_class:
    def __init__(self, id, date, duration, description):
        self.__id = id
        self.__date = date
        self.__duration = duration
        self.__description = description

    def get_event_id(self):
        return self.__id
    
    def get_event_date(self):
        return self.__date
    
    def get_event_duration(self):
        return self.__duration
    
    def get_event_description(self):
        return self.__description
    
    def __str__(self):
        return self.__id + " | " + self.__date + " | " + self.__duration + " | " + self.__description
    

    