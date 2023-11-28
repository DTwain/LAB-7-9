from DOMAIN.event import event_class
from DOMAIN.person import person_class
from DOMAIN.VALIDARI.validare_persoana import valid_person
from DOMAIN.VALIDARI.validare_event import valid_event
from CONTROLLERS.event_controler import event_controler
from CONTROLLERS.person_controler import person_controler
from CONTROLLERS.report_controler import raport_controler
from REPOSITORIES.repo_evenimente import repo_events
from REPOSITORIES.repo_persoane import repo_people
from UI.run_console import UI

from DOMAIN.VALIDARI.validation_exceptions import vid_city_exception
from DOMAIN.VALIDARI.validation_exceptions import vid_house_number_exception

if __name__ == '__main__':
    r_events = repo_events
    r_people = repo_people

    person_validator = valid_person
    event_validator = valid_event

    pers_controler = person_controler(r_people, person_validator)
    ev_controler = event_controler(r_events, event_validator)
    #rrr_controler = raport_controler(r_people, r_events)

    event_1 = event_class("1", "12/2/2020", "120", "Concertul lui travis Scott")
    event_2 = event_class("2", "29/2/2022", "200", "Serbarea clasei a 3 - a")
    
    event_validator.event_validation(event_1)
    try:
        event_validator.event_validation(event_2)
        assert False
    except Exception as ex:
        print(ex)
        assert True

    pers_controler.add_person("1", "Popescu Niculae", "ROmania", "Tulcea", "Zorilor", "122")
    pers_controler.add_person("2", "Pecsar Miruna", "Zimbabue", "NEW MAN", "LUMINII", "122A")
    pers_controler.afisare_persoane()

    pers = pers_controler.update_person("2", "Pecsar Miruna", "ROmania", "SUCEAVA", "Zorilor", "122")
    print(f"{pers} \n")

    pers_controler.remove_person("2")
    pers_controler.afisare_persoane()
    print("ceva")

    person_1 = person_class("1", "Popescu Niculae", "ROmania", "Tulcea", "Zorilor", "122")
    person_2 = person_class("3", "Predoae Vasile", "Romania", "", "Independentei", "")

    pers_controler.add_event_to_person("1", "1")
    pers_controler.add_event_to_person("1", "2")
    print("------------------\n")
    pers_controler.afisare_persoane()
    print("------------------\n")
    print("evenimentele persoanei cu id-ul 1 sunt: ")
    rrr_controler.first_raport("1")
    print("------------------\n")
    person_validator.person_validation(person_1)
    try:
        person_validator.person_validation(person_2)
        assert False
    except vid_city_exception:
        print("trebuie recitit_orasul")
    except vid_house_number_exception:
        print("trebuie recitit numarul casei")
    ui = UI(r_events, r_people)
    ui.run_C()