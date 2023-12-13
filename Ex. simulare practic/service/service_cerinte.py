class service_cerinte:
    def __init__(self, repo):
        self.__repo = repo

    def cautare(self, str_dupa_care_se_cauta):
        toti_robotii = self.__repo.get_all()
        rezultat = []
        for robot in toti_robotii:
            if str_dupa_care_se_cauta in robot.get_robot_descriere():
                rezultat.append(robot.get_robot_id())
        if len(rezultat) == 0: 
            return None
        for ind in range(len(rezultat)):
            rezultat[ind] = self.__repo.get_robot_by_id(rezultat[ind])
        rezultat.sort(key=lambda x:x.get_robot_battery())
        rezultat_as_str = ""
        for robot in rezultat:
            rezultat_as_str += str(robot.get_robot_id()) + ", "
        return rezultat_as_str[:-2]

    def cerinta_2(self, x_start, y_start):
        x_start, y_start = int(x_start), int(y_start)
        copie_x, copie_y = int(x_start), int(y_start)
        toti_robotii = self.__repo.get_all()
        for robot in toti_robotii:
            x_start, y_start = int(copie_x), int(copie_y)
            rezultat = str(robot.get_robot_id())  + ": "
            comenzi = robot.get_robot_comenzi()
            baterie = int(robot.get_robot_battery())
            for comanda in comenzi:
                if baterie <= 9 and str(comanda) in ("up", "down", "left", "right"):
                    break
                if str(comanda) == "up":
                    y_start += 1
                    baterie -= 10 
                elif str(comanda) == "down":
                    y_start -= 1
                    baterie -= 10
                elif str(comanda) == "left":
                    x_start -= 1
                    baterie -= 10
                elif str(comanda) == "right":
                    x_start += 1
                    baterie -= 10
                elif str(comanda) == "halt":
                    baterie += 5

            rezultat += "<" + str(x_start) + "," + str(y_start) + "> " + str(baterie)
            yield rezultat

    

 
                


    