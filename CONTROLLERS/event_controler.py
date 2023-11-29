from DOMAIN.event import event_class

class event_controler:
    def __init__(self, repo_events, event_validator) -> None:
        self.__repository_events = repo_events
        self.__event_validator = event_validator

    def add_event(self, id, date, duration, description):
        event_obj = event_class(id, date, duration, description)
        self.__event_validator.event_validation(event_obj)
        self.__repository_events.add_event(event_obj)
        return event_obj
    
    def remove_event(self, id):

        removed_event = self.__repository_events.delete_event(id)
        return removed_event
    
    def update_event(self, id, date, duration, description):
        updated_event = event_class(id, date, duration, description)
        self.__event_validator.event_validation(updated_event)
        old_event = self.__repository_events.update_event(updated_event, id)
        return old_event
    
    def find_event_by_id(self, event_id):
        return self.__repository_events.get_event_through_id(event_id)
    
    
