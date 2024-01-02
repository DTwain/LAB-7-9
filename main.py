from DOMAIN.VALIDARI.validare_persoana import valid_person
from DOMAIN.VALIDARI.validare_event import valid_event
from CONTROLLERS.event_controler import event_controler
from CONTROLLERS.person_controler import person_controler
from CONTROLLERS.report_controler import report_controler
from REPOSITORIES.repo_file_persoane import repo_file_people
from REPOSITORIES.repo_file_evenimente import repo_file_event
from UI.run_console import UI
from DOMAIN.person_event import person_event_class
from TESTS.combine_all_tests import test_suite

from UTILS.sort import shell_sort, bubble_sort

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
