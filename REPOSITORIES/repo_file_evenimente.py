from REPOSITORIES.repo_evenimente import repo_events
from DOMAIN.event import event_class
class repo_file_event(repo_events):
    def __init__(self, file_name):
        super().__init__()
        self.__file_name = file_name
        self.__load_from_file()

    def __load_from_file(self):
        try:
            file = open(self.__file_name, "r")
        except IOError:
            return
        
        line = file.readline().strip()
        while line != "":
            line_elements = line.split(";")
            person = event_class(line_elements[0], line_elements[1], line_elements[2], line_elements[3])
            super().add_event(person)
            line = file.readline().strip()
        file.close()

    def __store_to_file(self):
        try:
            file = open(self.__file_name, "w")
        except IOError:
            return
        list_of_all_events = super().get_all()
        for event in list_of_all_events:
            event_as_string = event.get_event_id() + ';' + event.get_event_date()
            event_as_string += ';' + event.get_event_duration() + ';' + event.get_event_description()
            event_as_string += '\n'
            file.write(event_as_string)
        file.close()
        
    def add_event(self, event):
        repo_events.add_event(self, event)
        self.__store_to_file()

    def delete_event(self, id):
        erased_event = repo_events.delete_event(self, id)
        self.__store_fo_file()
        return erased_event

    def update_event(self, event, id):
        preupdated_event = repo_events.update_event(self, event, id)
        self.__store_to_file()
        return preupdated_event
    
    def get_event_through_id(self, id):
        return super().get_event_through_id(id)
    
    def get_events_that_corespond_to_id(self, list_of_ids):
        return super().get_events_that_corespond_to_id(list_of_ids)

    def get_list_of_DTO_obj_for_third_report(self):
        return super().get_list_of_DTO_obj_for_third_report()
    
    def get_all_ids(self):
        return super().get_all_ids()
    
    def __len__(self):
        return super().__len__()
    
    def output(self):
        super().output()


    
    


            