from REPOSITORIES.repo_custom_exceptation import dublicated_id_exception 
from REPOSITORIES.repo_custom_exceptation import inexistent_id_exception
class repo_events:
    def __init__(self):
        self.__repo_events = {}

    def add_event(self, event):
        if event.get_event_id() in self.__repo_events:
            raise dublicated_id_exception(event.get_event_id())
        self.__repo_events[event.get_event_id()] = event

    def delete_event(self, id):
        if id not in self.__repo_events:
            raise inexistent_id_exception(id)
        event_sters = self.__repo_events[id]
        del self.__repo_events[id]
        return event_sters
    
    def update_event(self, event, id):
        if id not in self.__repo_events:
            raise inexistent_id_exception(id)
        old_event = self.__repo_events[id]
        self.__repo_events[id] = event
        return old_event

    def get_event_through_id(self, event_id):
        if event_id not in self.__repo_events:
            raise inexistent_id_exception(event_id)
        return self.__repo_events[event_id]
    
    def get_events_that_corespond_to_id(self, id_list):
        """
        id_list = lista cu id-urile evenimentelor la care participa o persoana
        return: va returna o lista cu toate obiectele de tip eveniment care corespund id - urilor
        """
        event_list = []
        for event_id in id_list:
            event = repo_events.get_event_through_id(self, event_id)
            event_list.append(event)
        return event_list
    
    def __len__(self):
        return len(self.__repo_events)
    

