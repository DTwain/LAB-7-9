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
        self.__event_validator.event_validation_for_update(updated_event)
        default_event = self.__repository_events.get_event_through_id(id)
        if updated_event.get_event_date() != "":
            default_event.set_event_date(updated_event.get_event_date())
        if updated_event.get_event_duration() != "":
            default_event.set_event_duration(updated_event.get_event_duration())
        if updated_event.get_event_description() != "":
            default_event.set_event_description(updated_event.get_event_description())
        old_event = self.__repository_events.update_event(default_event, id)
        return old_event
    
    def find_event_by_id(self, event_id):
        return self.__repository_events.get_event_through_id(event_id)
    
    def find_events_using_key_words(self, list_of_key_values):
        events = self.__repository_events.get_all()
        for event in events:
            event_id = event.get_event_id().lower()
            event_date = event.get_event_date().lower()
            event_duration = event.get_event_duration().lower()
            event_description = event.get_event_description().lower()
            for key_value in list_of_key_values:
                key_value = key_value.lower()
                if key_value == event_id or key_value in event_date or key_value in event_duration or key_value in event_description:
                    yield event
                    break
                
    def inc_number_of_people_joined_to_event(self, event_id):
        event = self.__repository_events.get_event_through_id(event_id)
        event.inc_number_of_participants()
        self.__repository_events.update_event(event, event_id)
    
    def output_events(self):
        self.__repository_events.output()

    
