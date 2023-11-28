from REPOSITORIES.repo_custom_exceptation import dublicated_id_exception 
from REPOSITORIES.repo_custom_exceptation import inexistent_id_exception
class repo_events:
    def __init__(self):
        self.__events = {}

    def add_event(self, event):
        if event.get_id_event() in self.__events:
            raise dublicated_id_exception(event.get_id_event())
        self.__events[event.get_id_event()] = event

    def delete_event(self, id):
        if id not in self.__events:
            raise inexistent_id_exception(id)
        event_sters = self.__events[id]
        del self.__events[id]
        return event_sters
    
    def update_event(self, event, id):
        if id not in self.__events:
            raise inexistent_id_exception(id)
        old_event = self.__events[id]
        self.__events[id] = event
        return old_event

    def __len__(self):
        return len(self.__events)
    

