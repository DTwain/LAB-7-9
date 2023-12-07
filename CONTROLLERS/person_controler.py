from DOMAIN.person import person_class
from MY_CUSTOM_EXCEPTIONS.repo_custom_exception import event_added_twice_to_person, no_other_event_to_add_to_person
class person_controler:
    """
    Controller class for managing person objects.
    """

    def __init__(self, repo_pers, pers_validator, event_controler):
        """
        Initialize a person_controler object.

        Parameters:
        - repo_pers (Repository): The repository for person objects.
        - pers_validator (Validator): The validator for person objects.
        - event_controler (EventController): The controller for event objects.
        """
        self.__repo_person = repo_pers
        self.__person_validator = pers_validator
        self.__event_controler = event_controler

    def add_person(self, id, name, country, city, street, number_of_the_house):
        """
        Add a person to the repository.

        Parameters:
        - id (str): The ID of the person.
        - name (str): The name of the person.
        - country (str): The country of the person.
        - city (str): The city of the person.
        - street (str): The street of the person.
        - number_of_the_house (str): The number of the house of the person.

        Returns:
        - person_obj (Person): The added person object.
        """
        person_obj = person_class(id, name, country, city, street, number_of_the_house)
        self.__person_validator.person_validation(person_obj)
        self.__repo_person.add_person_to_rep(person_obj)
        return person_obj
    
    def remove_person(self, id):
        """
        Remove a person from the repository.

        Parameters:
        - id (str): The ID of the person to be removed.

        Returns:
        - removed_person (Person): The removed person object.
        """
        removed_person  = self.__repo_person.remove_person(id)
        return removed_person
    
    def update_person(self, id, name, country, city, street, number_of_the_house):
        """
        Update a person in the repository.

        Parameters:
        - id (str): The ID of the person to be updated.
        - name (str): The new name of the person.
        - country (str): The new country of the person.
        - city (str): The new city of the person.
        - street (str): The new street of the person.
        - number_of_the_house (str): The new number of the house of the person.

        Returns:
        - preupdate_person (Person): The person object before the update.
        """
        new_person_obj = person_class(id, name, country, city, street, number_of_the_house)
        self.__person_validator.person_validation_for_update(new_person_obj)
        default_person = self.__repo_person.get_person_through_id(id)
        if new_person_obj.get_person_name() != "":
            default_person.set_person_name(new_person_obj.get_person_name())
        if new_person_obj.get_country() != "":
            default_person.set_country(new_person_obj.get_country())
        if new_person_obj.get_city() != "":
            default_person.set_city(new_person_obj.get_city())
        if new_person_obj.get_street() != "":
            default_person.set_street(new_person_obj.get_street())
        if new_person_obj.get_number_of_the_house() != "":
            default_person.set_number_of_the_house(new_person_obj.get_number_of_the_house())
        preupdate_person = self.__repo_person.update_person(default_person, id)
        return preupdate_person
    
    def add_event_to_person(self, person_id, event_id):
        """
        Add an event to a person.

        Parameters:
        - person_id (int): The ID of the person.
        - event_id (int): The ID of the event to be added.

        Returns:
        - None
        """
        if self.__event_controler.find_event_by_id(event_id):
            pass
        person_obj = self.__repo_person.get_person_through_id(person_id)
        all_ids_of_events_person_obj_joined = person_obj.get_events_id()
        if len(all_ids_of_events_person_obj_joined) == len(self.__event_controler):
            raise no_other_event_to_add_to_person
        if event_id in all_ids_of_events_person_obj_joined:
            raise event_added_twice_to_person(event_id)
        self.__event_controler.inc_number_of_people_joined_to_event(event_id)
        person_obj.add_event_to_person(event_id)
        self.__repo_person.update_person(person_obj, person_obj.get_person_id())
    
    def find_person_by_id(self, person_id):
        """
        Find a person by ID.

        Parameters:
        - person_id (int): The ID of the person to be found.

        Returns:
        - person (Person): The found person object.
        """
        return self.__repo_person.get_person_through_id(person_id)
    
    def find_people_using_key_words(self, list_of_key_words):
        """
        Find people using a list of key words.

        Parameters:
        - list_of_key_words (list): The list of key words to search for.

        Yields:
        - person (Person): The found person object.
        """
        people = self.__repo_person.get_all()
        for person in people:
            person_id = person.get_person_id().lower()
            person_name = person.get_person_name().lower()
            person_country = person.get_country().lower()
            person_city = person.get_city().lower()
            person_street = person.get_street().lower()
            person_number_of_the_house = person.get_number_of_the_house().lower()
            for key_word in list_of_key_words:
                key_word = key_word.lower()
                if key_word == person_id or key_word in person_name or key_word in person_country or key_word in person_city or key_word in person_street or key_word == person_number_of_the_house:
                    yield person
                    break
    
    def output_people(self):
        """
        Output all people in the repository.

        Returns:
        - None
        """
        self.__repo_person.output()
    



    