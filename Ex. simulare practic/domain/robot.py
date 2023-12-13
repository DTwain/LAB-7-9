class robot_class:
    def __init__(self, id, baterie, descriere, comenzi):
        self.__id = id
        self.__baterie = baterie
        self.__descriere = descriere
        self.__comenzi = comenzi

    def get_robot_id(self):
        return self.__id
    
    def get_robot_battery(self):
        return self.__baterie
    
    def get_robot_descriere(self):
        return self.__descriere
    
    def get_robot_comenzi(self):
        return self.__comenzi
    
    def __str__(self) -> str:
        comenzi_as_str = ""
        for comanda in self.__comenzi:
            comenzi_as_str += comanda + ", "
        comenzi_as_str = comenzi_as_str[:-2]
        return "id: " + self.__id + "\nbaterie: " + self.__baterie + "\ndescriere: " + self.__descriere + "\ncomenzi: " + comenzi_as_str
    