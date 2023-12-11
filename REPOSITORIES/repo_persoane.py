from MY_CUSTOM_EXCEPTIONS.repo_custom_exception import dublicated_id_exception, inexistent_person_id_exception, no_person_to_delete_exception
from DOMAIN.DTO import DTO_for_second_report
class repo_people:
    """
    Clasa care se ocupa de repository-ul de persoane.

    Attributes:
    __repo_people (dict): Un dictionar care contine persoanele si key-urile reprezinta ID-urile persoanelor.

    Methods:
    add_person_to_rep(person): Adauga o persoana in repository.
    remove_person(id): Sterge o persoana din repository.
    update_person(updated_person, id): Updateaza o persoana din repository.
    get_person_through_id(person_id): Returneaza o persoana corespunzatoare unui id, din repository.
    get_list_of_DTO_objs(): Returneaza o lista de obiecte DTO pentru raportul 2.
    get_all(): Returneaza o lista cu toate persoanele din repository.
    get_all_ids(): Returneaza o lista cu toate id-urile persoanelor din repository.
    size(): Returneaza numarul de persoane din repository.
    output(): Afiseaza persoanele din repository.
    """
    def __init__(self):
        self.__repo_people = {}

    def add_person_to_rep(self, person):
        if person.get_person_id() not in self.__repo_people:
            self.__repo_people[person.get_person_id()] = person
        else:
            raise dublicated_id_exception(person.get_person_id())

    def remove_person(self, id):
        if len(self.__repo_people) == 0:
            raise no_person_to_delete_exception()
        if id not in self.__repo_people:
            raise inexistent_person_id_exception(id)
        removed_person = self.__repo_people[id]
        removed_person.remove_any_connections_with_person_id()
        del self.__repo_people[id]
        return removed_person
        
    def update_person(self, updated_person, id):
        """
        updated_person (person_class): Un obiect de tip person_class.
        id (str): Un string care reprezinta ID-ul persoanei.
        """
        if id not in self.__repo_people:
            raise inexistent_person_id_exception(id)
        preupdate_person = self.__repo_people[id]
        self.__repo_people[id] = updated_person
        return preupdate_person
    
    def get_person_through_id(self, person_id):
        if person_id not in self.__repo_people:
            raise inexistent_person_id_exception(person_id)
        return self.__repo_people[person_id]

    def get_list_of_DTO_objs(self):
        list_with_number_of_events_person_joined = []
        for person_id in self.__repo_people:
            person = repo_people.get_person_through_id(self, person_id)
            DTO_id_person_number_of_events = DTO_for_second_report(person.get_person_id(), person.get_number_of_events_person_joined())
            list_with_number_of_events_person_joined.append(DTO_id_person_number_of_events)
        return list_with_number_of_events_person_joined

    def get_all(self):
        return [self.__repo_people[person_id] for person_id in self.__repo_people]
    
    def get_all_ids(self):
        return [str(key) for key in self.__repo_people.keys()]
    
    def __len__(self):
        return len(self.__repo_people)
    
    def output(self):
        for key, values in self.__repo_people.items():
            print(f"{values}\n")
            