from DOMAIN.event import event_class
from DOMAIN.person import person_class
from REPOSITORIES.repo_evenimente import repo_events
from REPOSITORIES.repo_persoane import repo_people
class UI:
    def __init__(self, controler_ev, controler_per):
        """
        controler_ev = Service-ul pentru evenimente 
        controler_persoana = Service-ul pentru persoane
        """
        self.__controler_events = controler_ev
        self.__controler_people = controler_per

    def run_C(self):
        pass
    pass
    
