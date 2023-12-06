from DOMAIN.VALIDARI.validare_persoana import valid_person
from DOMAIN.VALIDARI.validare_event import valid_event
from CONTROLLERS.event_controler import event_controler
from CONTROLLERS.person_controler import person_controler
from CONTROLLERS.report_controler import report_controler
from REPOSITORIES.repo_evenimente import repo_events
from REPOSITORIES.repo_persoane import repo_people
from UI.run_console import UI

from TESTS.combine_all_tests import test_suite
if __name__ == '__main__':
    r_events = repo_events()
    r_people = repo_people()

    person_validator = valid_person()
    event_validator = valid_event()

    ev_controler = event_controler(r_events, event_validator)
    pers_controler = person_controler(r_people, person_validator, ev_controler)
    rrr_controler = report_controler(r_people, r_events)


    test_suite()
    ui = UI(ev_controler, pers_controler, rrr_controler)
    ui.run_C()

    # event_1 = event_class("1", "12/2/2020", "120", "Concertul lui travis Scott")
    # event_2 = event_class("2", "28/2/2022", "200", "Serbarea clasei a 3 - a")

    # ev_controler.add_event("1", "12/2/2020", "120", "Kylie Jenner s-a despartit de Travis Scott")
    # ev_controler.add_event("2", "28/2/2022", "200", "Serbarea clasei a 3 - a")
    # ev_controler.add_event("3", "12/2/2021", "300", "Balul Bobocilor")
    
    # event_validator.event_validation(event_1)
    # try:
    #     event_validator.event_validation(event_2)
    #     assert False
    # except Exception as ex:
    #     print(ex)
    #     assert True

    # pers_controler.add_person("1", "Popescu Niculae", "ROmania", "Tulcea", "Zorilor", "122")
    # pers_controler.add_person("2", "Pecsar Miruna", "Zimbabue", "NEW MAN", "LUMINII", "122A")
    # pers_controler.output_people()

    # pers = pers_controler.update_person("2", "Pecsar Miruna", "ROmania", "SUCEAVA", "Zorilor", "122")
    # print(f"{pers} \n")

    # print("ceva")

    # person_1 = person_class("1", "Popescu Niculae", "ROmania", "Tulcea", "Zorilor", "122")
    # person_2 = person_class("3", "Predoae Vasile", "Romania", "", "Independentei", "")


    # pers_controler.output_people()
    # pers_controler.add_event_to_person("1", "1")
    # pers_controler.add_event_to_person("1", "2")
    # pers_controler.add_event_to_person("2", "1")
    # pers_controler.add_event_to_person("2","2")
    # pers_controler.add_event_to_person("2", "3")
    # pers_controler.output_people()
    # print("----------------")
    # #pers_controler.add_event_to_person("1", "3")
    # sorted_list = rrr_controler.first_raport("1")
    # for elem in sorted_list:
    #     print(elem)
    # print("----------------")

    # print("-----------------------------")
    # report_2_rezult = rrr_controler.second_raport()
    # for person in report_2_rezult:
    #     print(person)
    # print("-----------------------------")
    # person_validator.person_validation(person_1)
    # try:
    #     person_validator.person_validation(person_2)
    #     assert False
    # except vid_city_exception:
    #     print("trebuie recitit_orasul")
    # except vid_house_number_exception:
    #     print("trebuie recitit numarul casei")
    # pers_controler.output_people()

    # print("------------------------------------------------------")
    # ev_controler.output_events()
    # print("------------------------------------------------------")

    # rezultat_raport_3 = rrr_controler.third_report()
    # print("1-1-1-1-1-1-1-1-1-1-1-1-1-1-1-1-1-1-1-1-1")
    # for dto in rezultat_raport_3:
    #     print(dto)
    # print("1-1-1-1-1-1-1-1-1-1-1-1-1-1-1-1-1-1-1-1-1")
    
    