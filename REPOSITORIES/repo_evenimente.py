from MY_CUSTOM_EXCEPTIONS.repo_custom_exception import dublicated_id_exception, inexistent_id_exception
from DOMAIN.DTO import DTO_for_third_report
class repo_events:
    """
    Clasa care se ocupa de repository-ul de evenimente.

    Attributes:
    - __repo_events (dict): Un dictionar care contine evenimentele si key-urile reprezinta ID-urile evenimentelor.

    METODE
    - add_event(event): Adauga un eveniment in repository.
    - delete_event(id): Sterge un eveniment din repository.
    - update_event(event, id): Updateaza un eveniment din repository.
    - get_event_through_id(event_id): Returneaza un eveniment corespunzator unui id, din repository.
    - get_events_that_corespond_to_id(id_list): Returneaza o lista cu evenimentele corespunzatoare unor id-uri, din repository.
    - get_list_of_DTO_obj_for_third_report(): Returneaza o lista de obiecte DTO pentru raportul 3.
    - get_all(): Returneaza o lista cu toate evenimentele din repository.
    - get_all_ids(): Returneaza o lista cu toate id-urile evenimentelor din repository.
    - __len__(): Returneaza numarul de evenimente din repository.
    - output(): Afiseaza evenimentele din repository.
    """
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
        Returneaza o lista cu evenimentele corespunzatoare unor id-uri, din repository.

        Args:
        - id_list (list): A list of event IDs.

        Returns:
        - event_list (list): A list of event objects that correspond to the given IDs.
        """
        event_list = []
        for event_id in id_list:
            event = repo_events.get_event_through_id(self, event_id)
            event_list.append(event)
        return event_list
    
    def get_list_of_DTO_obj_for_third_report(self):
        """
        Returneaza o lista de obiecte DTO pentru raportul 3.

        Returns:
        - list_of_DTO_obj_for_third_report (list): A list of DTO objects for the third report.
        """
        list_of_DTO_obj_for_third_report = []
        for event_id in self.__repo_events:
            event = repo_events.get_event_through_id(self, event_id)
            DTO_obj = DTO_for_third_report(event.get_event_id(), event.get_number_of_people_joined())
            list_of_DTO_obj_for_third_report.append(DTO_obj)
        return list_of_DTO_obj_for_third_report

    def get_all(self):
        """
        Returneaza o lista cu toate evenimentele din repository.

        Returns:
        - all_events (list): A list of all event objects in the repository.
        """
        return [self.__repo_events[event_id] for event_id in self.__repo_events]
    
    def get_all_ids(self):
        """
        Returneaza o lista cu toate id-urile evenimentelor din repository.

        Returns:
        - all_ids (list): A list of all event IDs in the repository.
        """
        return list(self.__repo_events.keys())

    def __len__(self):
        """
        Returnea numarul de evenimente din repository.

        Returns:
        - length (int): The number of events in the repository.
        """
        return len(self.__repo_events)
    
    def output(self):
        """
        Afiseaza evenimentele din repository.
        """
        for key, values in self.__repo_events.items():
            print(f"{values}\n")
    

