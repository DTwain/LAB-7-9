from DOMAIN.VALIDARI.validare_persoana import valid_person
from DOMAIN.VALIDARI.validare_event import valid_event
from CONTROLLERS.event_controler import event_controler
from CONTROLLERS.person_controler import person_controler
from CONTROLLERS.report_controler import report_controler
from REPOSITORIES.repo_file_persoane import repo_file_people
from REPOSITORIES.repo_file_evenimente import repo_file_event
from UI.run_console import UI

#sterse dupa
from REPOSITORIES.repo_evenimente import repo_events
from REPOSITORIES.repo_persoane import repo_people
from DOMAIN.person_event import person_event_class
import random
from UTILS.generators import date_generator, string_generator, event_duration_generator

from TESTS.combine_all_tests import test_suite

if __name__ == '__main__':
    r_events = repo_file_event("DATA_BASE/evenimente.txt")
    r_people = repo_file_people("DATA_BASE/persoane.txt")


    person_validator = valid_person()
    event_validator = valid_event()

    shared_person_event_class = person_event_class()

    ev_controler = event_controler(r_events, event_validator, r_people, shared_person_event_class)
    pers_controler = person_controler(r_people, person_validator, shared_person_event_class)
    rrr_controler = report_controler(r_people, r_events, shared_person_event_class)

    test_suite()
    ui = UI(ev_controler, pers_controler, rrr_controler)
    ui.run_C()

    # random.seed(10)
    # for _ in range(15):
    #     print(date_generator())

    # print("-------------------------")
    # for _ in range(15):
    #     print(string_generator(5))

    # print("-------------------------")
    # for _ in range(15):
    #     print(event_duration_generator())

    # ev_controler.output_events()
    # print("------------------------------------------------")
    # pers_controler.output_people()

    

    
    