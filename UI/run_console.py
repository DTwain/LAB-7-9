from DOMAIN.VALIDARI.validari_UI import option_exist, option_for_report_exist
from MY_CUSTOM_EXCEPTIONS.ui_custom_exception import invalid_option, invalid_option_for_report
from MY_CUSTOM_EXCEPTIONS.validation_exceptions import invalid_day, invalid_month, invalid_year, invalid_date_character, multiple_dots_in_event_duration, invalid_event_duration_character, comma_not_supported_in_float_values, date_incomplete, person_validation_exception, vid_name_exception, vid_country_exception, vid_city_exception, vid_street_exception, vid_house_number_exception, vid_date_of_event, vid_description_of_event, vid_duration_of_event, vid_event_id_exception, vid_person_id_exception
from MY_CUSTOM_EXCEPTIONS.repo_custom_exception import repo_custom_exception, dublicated_id_exception, inexistent_id_exception

class UI:
    def __init__(self, controler_ev, controler_per, controlor_report):
        """
        controler_ev = Service-ul pentru evenimente 
        controler_persoana = Service-ul pentru persoane
        """
        self.__controler_events = controler_ev
        self.__controler_people = controler_per
        self.__controler_report = controlor_report

    def __main_menu(self):
        print("Alegeti operatie pe care doriti sa o efectuati:")
        print("< 1 >    Adauga < eveniment >")
        print("< 2 >    Adauga < persoana >")
        print("< 3 >    Sterge < eveniment >")
        print("< 4 >    Sterge < persoana >")
        print("< 5 >    Modifica < eveniment >")
        print("< 6 >    Modifica < persoana >")
        print("< 7 >    Cauta < eveniment >")
        print("< 8 >    Cauta < persoana >")
        print("< 9 >    Inscrie < persoana > la < eveniment >")
        print("< 10 >   Rapoarte < evenimente > | < persoane >")

    def __sub_menu_for_reports(self):
        print("Alegeti un raport:")
        print("     A. Lista de evenimente la care participă o persoană ordonat alfabetic după descriere")
        print("     B. Persoane participante la cele mai multe evenimente")
        print(f"     C. Primele 20{"% e"}venimente cu cei mai mulți participanți (descriere, număr participanți)")
    def __read_event_id(self):
        return input("Recititi ID-ul eventului: ")
    def __read_event_date(self):
        return input("Recititi data eventului: ")
    def __read_event_duration(self):
        return input("Recititi durata eventului: ")
    def __read_event_description(self):
        return input("Recititi descrierea eventului: ")
    def __read_person_name(self):
        return input("Recititi numele persoanei: ")
    def __read_person_id(self):
        return input("Recititi ID-ul persoanei: ")
    def __read_person_address_country(self):
        return input("Recititi tara de origine a persoanei: ")
    def __read_person_address_city(self):
        return input("Recititi orasul de origine a persoanei: ")
    def __read_person_address_street(self):
        return input("Recititi strada pe care locuieste persoana: ")
    def __read_person_address_house_number(self):
        return input("Recititi numarul casei unde locuieste persoana: ")
    
    def __read_option(self):
        while True:
            try:
                option = input("\nOptiunea dumneavoastra este: ").strip()
                print("\n")
                option_exist(option)
                return option
            except invalid_option as ex:
                print(ex)
        

    def __read_option_for_reports(self):
        while True:
            try:
                option = input("Optiunea dumneavoastra pentru raport este: ").strip()
                option_for_report_exist(option)
                return option
            except invalid_option_for_report as ex:
                print(ex)
        
    def __add_event(self):
        print("Adaugati datele evenimentului: ")
        event_id = input("     ID-ul eventului:     ")
        event_date = input("     Data eventului:      ")
        event_duration = input("     Dati durata eventului:  ")
        event_description = input("     Descrierea eventului:   ")
        add_opp_fail = True
        while add_opp_fail:
            try:
                self.__controler_events.add_event(event_id, event_date, event_duration, event_description)
                print("Adaugare realizata cu succes\n")
                add_opp_fail = False
            except (vid_event_id_exception, dublicated_id_exception) as ex:
                print(ex) 
                event_id = self.__read_event_id()
            except (vid_date_of_event, date_incomplete, invalid_day, invalid_month, invalid_year) as ex:
                print(ex)
                event_date = self.__read_event_date()
            except (vid_duration_of_event, invalid_event_duration_character, comma_not_supported_in_float_values, multiple_dots_in_event_duration) as ex:
                print(ex)
                event_duration = self.__read_event_duration()
            except vid_description_of_event as ex:
                print(ex)
                event_description = self.__read_event_description()

    def __add_person(self):
        print("Adaugati datele persoanei:")
        person_id = input("     ID-ul persoanei: ")
        person_name = input("     Numele persoanei:")
        print("     Adresa persoanei:")
        country = input("            Tara: ")
        city = input("            Oras: ")
        street = input("            Strada: ")
        number = input("            Numarul casei: ")
        add_opp_fail = True
        while add_opp_fail:
            try:
                self.__controler_people.add_person(person_id, person_name, country, city, street, number)
                print("Adaugare realizata cu succes\n")
                add_opp_fail = False
            except (vid_person_id_exception, dublicated_id_exception) as ex: 
                print(ex)
                person_id = self.__read_person_id()
            except vid_name_exception as ex:
                print(ex)
                person_name = self.__read_person_name()
            except vid_country_exception as ex:
                print(ex)
                country = self.__read_person_address_country()
            except vid_city_exception as ex:
                print(ex)
                city = self.__read_person_address_city()
            except vid_street_exception as ex:
                print(ex)
                street = self.__read_person_address_street()
            except vid_house_number_exception as ex:
                print(ex)
                number = self.__read_person_address_house_number()
    def __remove_person(self):
        print("ALEGETI UN ID DE PERSOANA, PENTRU A STERGE PERSOANA:\n")
        self.__controler_people.output_people()
        person_id = input("ID-ul persoanei: ")
        rem_opp_fail = True
        while rem_opp_fail:
            try:
                self.__controler_people.remove_person(person_id)
                print("Stergere realizata cu succes\n")
                rem_opp_fail = False
            except inexistent_id_exception as ex:
                print(ex)
                person_id = self.__read_person_id()
    
    def __remove_event(self):
        print("ALEGETI UN ID DE EVENT, PENTRU A STERGE EVENTUL:\n")
        self.__controler_events.output_events()
        event_id = input("ID-ul eventului: ")
        rem_opp_fail = True
        while rem_opp_fail:
            try:
                self.__controler_event.remove_event(event_id)
                print("Stergere realizata cu succes\n")
                rem_opp_fail = False
            except inexistent_id_exception as ex:
                print(ex)
                event_id = self.__read_person_id()

    def __update_person(self):
        print("ALEGETI UN ID DE PERSOANA, PENTRU A MODIFICA PERSOANA AFERNTA:\n")
        self.__controler_people.output_people()
        person_id = input("ID-ul persoanei: ")
        person_name = input("     Numele persoanei:")
        print("     Adresa persoanei:")
        country = input("            Tara: ")
        city = input("            Oras: ")
        street = input("            Strada: ")
        number = input("            Numarul casei: ")
        update_opp_fail = True
        while update_opp_fail:
            try:
                self.__controler_people.update_person(person_id, person_name, country, city, street, number)
                print("Modificare realizata cu succes\n")
                update_opp_fail = False
            except (vid_person_id_exception, dublicated_id_exception, inexistent_id_exception) as ex:
                print(ex)
                person_id = self.__read_person_id()

    def __update_event(self):
        print("ALEGETI UN ID DE EVENT, PENTRU A MODIFICA EVENTUL AFERNT:\n")
        self.__controler_events.output_events()
        print("\nAdaugati datele evenimentului: ")
        event_id = input("     ID-ul eventului:     ")
        event_date = input("     Data eventului:      ")
        event_duration = input("     Dati durata eventului:  ")
        event_description = input("     Descrierea eventului:   ")
        update_opp_fail = True
        while update_opp_fail:
            try:
                self.__controler_events.update_event(event_id, event_date, event_duration, event_description)
                print("Modificare realizata cu succes\n")
                update_opp_fail = False
            except (vid_event_id_exception, dublicated_id_exception, inexistent_id_exception) as ex:
                print(ex)
                event_id = self.__read_event_id()
            except (date_incomplete, invalid_day, invalid_month, invalid_year, invalid_date_character) as ex:
                print(ex)
                event_date = self.__read_event_date()
            except (invalid_event_duration_character, comma_not_supported_in_float_values, multiple_dots_in_event_duration) as ex:
                print(ex)
                event_duration = self.__read_event_duration()
    
    def __find_people_using_key_words(self):
        self.__controler_people.output_people()
        print("TUTORIAL:")
        print("VOM FOLOSI UN MECANISM DE CAUTARE A PERSOANELOR FILOSIND KEY - VALUES:")
        print("VALORILE CHEIE POT FI SCRISE PE MAI MULTE LINII.")
        print("DACA SE DORESTE FOLOSIREA UNEI PROPOZITII SAU A UNUI CUMUL DE CUVINTE DREPT KEY_WORD")
        print("ATUNCI ELE SE VOR SCRIE PE ACEEASI LINIE!!\n")
        print("TERMINAREA CITIRII VALORILOR CHEIE SE VA PUTEA REALIZA PRIN INTRODUCEREA PE O LINIE NOUA A CUVANTULUI << end >>\n")
        lines_of_key_words = []
        key_word = input("key_word = ")
        while True:
            if key_word.lower() == "end":
                break
            lines_of_key_words.append(key_word)
            key_word = input("key_word = ")
        
        generator = self.__controler_people.find_people_using_key_words(lines_of_key_words)
        
        for person in generator:
            print(person)

        # try:
        #     while True:
        #         person = next(generator)
        #         print(person)
        # except StopIteration:
        #     assert True
    
    def __find_event_using_key_words(self):
        print("TUTORIAL:")
        print("VOM FOLOSI UN MECANISM DE CAUTARE A EVENIMENTELOR FILOSIND KEY - VALUES:")
        print("VALORILE CHEIE POT FI SCRISE PE MAI MULTE LINII.")
        print("DACA SE DORESTE FOLOSIREA UNEI PROPOZITII SAU A UNUI CUMUL DE CUVINTE DREPT KEY_WORD")
        print("ATUNCI ELE SE VOR SCRIE PE ACEEASI LINIE!!\n")
        print("TERMINAREA CITIRII VALORILOR CHEIE SE VA PUTEA REALIZA PRIN INTRODUCEREA PE O LINIE NOUA A CUVANTULUI << end >>\n")
        lines_of_key_words = []
        key_word = input("key_word = ")
        while True:
            if key_word.lower() == "end":
                break
            lines_of_key_words.append(key_word)
            key_word = input("key_word = ")
        
        generator = self.__controler_events.find_events_using_key_words(lines_of_key_words)
        
        try:
            while True:
                event = next(generator)
                print(event)
        except StopIteration:
            assert True
    
    def __add_person_to_event(self):
        print("ALEGETI UN ID DE PERSOANA SI UN ID DE EVENT, PENTRU A INSCRIE PERSOANA LA EVENT:\n")
        self.__controler_people.output_people()
        self.__controler_events.output_events()
        person_id = input("ID-ul persoanei: ")
        event_id = input("ID-ul eventului: ")
        add_opp_fail = True
        while True:
            try:
                self.__controler_people.add_event_to_person(person_id, event_id)
                print("Inscriere realizata cu succes\n")
                add_opp_fail = False
            except (inexistent_id_exception, repo_custom_exception) as ex:
                print(ex)
                person_id = self.__read_person_id()
                event_id = self.__read_event_id()
            except vid_person_id_exception as ex:
                print(ex)
                person_id = self.__read_person_id()
            except vid_event_id_exception as ex:
                print(ex)
                event_id = self.__read_event_id()
        
    def __report_one(self):
        person_id = input("ID-ul persoanei: ")
        try:
            sorted_event_list = self.__controler_report.first_report(person_id)
        except repo_custom_exception as ex:
            print(ex)
            return 
        
        for event in sorted_event_list:
            print(f"{event}\n")
    
    def __report_two(self):
        try:
            people_with_max_joined_events = self.__controler_report.second_report()
        except repo_custom_exception as ex:
            print(ex)
            return
        
        for person in people_with_max_joined_events:
            print(f"{person}\n")

    def __report_three(self):
        try:
            first_20_percent_of_events_with_max_participants = self.__controler_report.third_report()
        except repo_custom_exception as ex:
            print(ex)
            return 
        
        for person in first_20_percent_of_events_with_max_participants:
            print(f"{person}\n")


    def run_C(self):
        self.__main_menu()
        while True:
            option = self.__read_option()
            if option == '1':
                self.__add_event()
            elif option == '2':
                self.__add_person()
            elif option == '3':
                self.__remove_event()
            elif option == '4':
                self.__remove_person()
            elif option == '5':
                self.__update_event()
            elif option == '6':
                self.__update_person()
            elif option == '7':
                self.__find_event_using_key_words()
            elif option == '8':
                self.__find_people_using_key_words()
            elif option == '9':
                self.__add_person_to_event()
            elif option == '10':
                self.__sub_menu_for_reports()
                while True:
                    option = self.__read_option_for_reports()
                    if option.upper() == 'A':
                        self.__report_one()
                    elif option.upper() == 'B':
                        self.__report_two()
                    elif option.upper() == 'C':
                        self.__report_three()
                    continue_stop = input("\nMai doriti un raport? < DA > / < NU >: ").strip()
                    if continue_stop.upper() == "DA":
                        continue
                    elif continue_stop.upper() == "NU":
                        break

            option = input("\nDoriti sa mai efectuati o alta operatie? < DA > / < NU >: ").strip()
            if option.upper() == "NU":
                break
            elif option.upper() == "DA":
                pass
            else:
                print("Optiune invalida")
                break
        
