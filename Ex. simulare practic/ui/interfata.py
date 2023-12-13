class ui:
    def __init__(self, service_cerinte):
        self.__service_cerite = service_cerinte
    
    def run_c(self):
        print("Alegeti o cerinta: \n")
        print("< 1 > Afiseaza roboti care au in descriere substringul citit de la tastatura")
        print("< 2 > Robotul va pleca de la doua coordonate dintr-un reper de coordonate xOy si va urma un set de instructiuni")
        cerinta = input("cerinta = ")
        if cerinta == '1':
            string_dupa_care_se_cauta = input("Introduceti stringul: ")
            cerinta_1 = self.__service_cerite.cautare(string_dupa_care_se_cauta)
            if cerinta_1 == None:
                print("Nu s-a gasit substringul in descrierile robotilor")
            else:
                print(cerinta_1)

        elif cerinta == '2':
            print("introduceti coordonatele:")
            x = input("x= ")
            y = input("y= ")
            cerinta_2 = self.__service_cerite.cerinta_2(x, y)
            for rezultat in cerinta_2:
                print(rezultat)
            
