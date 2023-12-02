import math
class raport_controler:
    def __init__(self, repo_people, repo_events):
        self.__repo_events = repo_events
        self.__repo_people = repo_people
    
    def first_raport(self, person_id):
        """
        Lista de evenimente la care participă o persoană ordonat alfabetic după descriere
        """
        person = self.__repo_people.get_person_through_id(person_id)
        events_indentificator = person.get_events_id() # lista id-urilor la care participa persoana cu person_id
        event_list = self.__repo_events.get_events_that_corespond_to_id(events_indentificator)
        sorted_event_list = sorted(event_list, key = lambda event: event.get_event_description())
        return sorted_event_list
    
    def second_raport(self):
        """
        Persoane participante la cele mai multe evenimente
        """
        list_with_DTO_objs = self.__repo_people.get_list_of_DTO_objs()
        # lista cu obiecte DTO din DTO.py   VEZI DTO.py
        max_number_of_events_joined = 0
        for DTO_OBJ in list_with_DTO_objs:
            if DTO_OBJ.get_number_of_events() > max_number_of_events_joined:
                max_number_of_events_joined = DTO_OBJ.get_number_of_events()
        
        for DTO_OBJ in list_with_DTO_objs[:]:
            if DTO_OBJ.get_number_of_events() != max_number_of_events_joined:
                list_with_DTO_objs.remove(DTO_OBJ)

        list_of_people_with_max_number_of_events = []
        for DTO_OBJ in list_with_DTO_objs:
            person_id = DTO_OBJ.get_person_id()
            person = self.__repo_people.get_person_through_id(person_id)
            list_of_people_with_max_number_of_events.append(person)

        return list_of_people_with_max_number_of_events
    
    def third_report(self):
        list_with_dto_objs_for_third_report = self.__repo_events.get_list_of_DTO_obj_for_third_report()
        sorted_list_of_dto_obj = sorted(list_with_dto_objs_for_third_report, key = lambda dto_obj : dto_obj.get_number_of_people(), reverse = True )
        twenty_percent_of_events = math.ceil(0.2 * len(sorted_list_of_dto_obj))
        list_of_twenty_percent_of_events = sorted_list_of_dto_obj[:twenty_percent_of_events]
        return list_of_twenty_percent_of_events 
        # max_number_of_events_person_joined va stoca numarul maxim de 






        


        
    

         