from DOMAIN.VALIDARI.validare_persoana import valid_person
from DOMAIN.VALIDARI.validare_event import valid_event
from CONTROLLERS.event_controler import event_controler
from CONTROLLERS.person_controler import person_controler
from CONTROLLERS.report_controler import report_controler
from REPOSITORIES.repo_file_persoane import repo_file_people
from REPOSITORIES.repo_file_evenimente import repo_file_event
from UI.run_console import UI

from TESTS.combine_all_tests import test_suite
if __name__ == '__main__':
    r_events = repo_file_event("D:/INFO 2/FP lab/LAB 7-9/DATA_BASE/evenimente.txt")
    r_people = repo_file_people("D:/INFO 2/FP lab/LAB 7-9/DATA_BASE/persoane.txt")

    person_validator = valid_person()
    event_validator = valid_event()

    ev_controler = event_controler(r_events, event_validator)
    pers_controler = person_controler(r_people, person_validator, ev_controler)
    rrr_controler = report_controler(r_people, r_events)


    test_suite()
    ui = UI(ev_controler, pers_controler, rrr_controler)
    ui.run_C()

    
    