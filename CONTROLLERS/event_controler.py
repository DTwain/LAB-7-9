from DOMAIN.event import event_class
from MY_CUSTOM_EXCEPTIONS.repo_custom_exception import no_other_event_to_add_to_person
from UTILS.generators import id_generator, date_generator, event_duration_generator, string_generator
class event_controler:
    """
    Controller class for managing events.
    """

    def __init__(self, repo_events, event_validator, repo_people, shared_person_event_class) -> None:
        """
        Initializes the event controller.

        Args:
            repo_events (EventRepository): The event repository.
            event_validator (EventValidator): The event validator.
        """
        self.__repository_events = repo_events
        self.__event_validator = event_validator
        self.__repository_people = repo_people
        self.shared_person_event_class = shared_person_event_class

    def add_event(self, id, date, duration, description):
        """
        Adds a new event.

        Args:
            id (str): The event ID.
            date (str): The event date.
            duration (str): The event duration.
            description (str): The event description.

        Returns:
            event_class: The added event object.
        """
        id = str(id)
        event_obj = event_class(id, date, duration, description, self.shared_person_event_class)
        self.__event_validator.event_validation(event_obj)
        self.__repository_events.add_event(event_obj)
        return event_obj
    
    def remove_event(self, id):
        """
        Removes an event.

        Args:
            id (str): The event ID.

        Returns:
            event_class: The removed event object.
        """
        removed_event = self.__repository_events.delete_event(id)
        return removed_event
    
    def update_event(self, id, date, duration, description):
        """
        Updates an event.

        Args:
            id (int): The event ID.
            date (str): The updated event date.
            duration (str): The updated event duration.
            description (str): The updated event description.

        Returns:
            event_class: The old event object before the update.
        """
        updated_event = event_class(id, date, duration, description, self.shared_person_event_class)
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
        """
        Finds an event by ID.

        Args:
            event_id (str): The event ID.

        Returns:
            event_class: The found event object.
        """
        return self.__repository_events.get_event_through_id(event_id)
    
    def find_events_using_key_words(self, list_of_key_values):
        """
        Finds events using key words.

        Args:
            list_of_key_values (list): The list of key words.

        Yields:
            event_class: The found event objects.
        """
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
                
    def controler_add_person_to_event(self, person_id, event_id):
        event = self.__repository_events.get_event_through_id(event_id)
        person = self.__repository_people.get_person_through_id(person_id)
        if person.get_number_of_events_person_joined() == len(self.__repository_events):
            raise no_other_event_to_add_to_person(person_id)
        event.add_person_to_event(person_id)

    def __len__(self):
        return len(self.__repository_events)
    
    def add_events_with_random_data(self, nr):
        for _ in range(nr):
            event = event_class(id_generator(), date_generator(), event_duration_generator(), string_generator(), self.shared_person_event_class)
            try:
                self.__event_validator.event_validation(event)
                self.__repository_events.add_event(event)
            except Exception:
                pass


    def output_events(self):
        """
        Outputs all events.
        """
        self.__repository_events.output()

    
