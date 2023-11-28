class raport_controler:
    def __init__(self, repo_events, repo_people):
        self.__repo_events = repo_events
        self.__repo_people = repo_people
    
    def first_raport(self, person_id):
        events_list_of_person = self.__repo_people.get_events_of_person(person_id)
        print(f"The events of the person with id " + person_id + " are: {events_list_of_person}")
