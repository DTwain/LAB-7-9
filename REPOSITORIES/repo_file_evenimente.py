from REPOSITORIES.repo_evenimente import repo_events
from DOMAIN.event import event_class
from DOMAIN.person_event import person_event_class
class repo_file_event(repo_events):
    def __init__(self, file_name):
        super().__init__()
        self.__shared_person_event_class = person_event_class()
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
            event = event_class(line_elements[0], line_elements[1], line_elements[2], line_elements[3], self.__shared_person_event_class)
            if len(line_elements) > 4 and line_elements[4] != '':
                people_ids = line_elements[4].split(',')
                for person_id in people_ids:
                    event.add_person_to_event(person_id)
            super().add_event(event)
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
            if str(event.get_list_of_people_ids_that_joined_event() != ''):
                event_as_string += ';' + str(event.get_list_of_people_ids_that_joined_event()) + '\n'
            else:
                event_as_string += '\n'
            file.write(event_as_string)
        file.close()
        
    def add_event(self, event):
        repo_events.add_event(self, event)
        self.__store_to_file()

    def delete_event(self, id):
        erased_event = repo_events.delete_event(self, id)
        self.__store_to_file()
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
    
    def get_shared_person_event_class(self):
        return self.__shared_person_event_class
    
    def __len__(self):
        return super().__len__()
    
    def output(self):
        super().output()


    
    


            