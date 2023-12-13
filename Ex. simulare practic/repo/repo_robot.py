from domain.robot import robot_class
from my_custom_exceptions import already_in_repo, inexistent_robot
class repo_robot:
    def __init__(self):
        self.__roboti = {}

    def add_robot(self, robot):
        if robot.get_robot_id() in self.__roboti:
            raise already_in_repo(robot.get_robot_id())
        self.__roboti[robot.get_robot_id()] = robot

    def get_all(self):
        return [self.__roboti[key] for key in self.__roboti.keys()]
    
    def get_robot_by_id(self, id):
        if str(id) not in self.__roboti:
            raise inexistent_robot(id)
        return self.__roboti[str(id)]
    
    def clear_repo(self):
        keys = self.__repo.keys()
        for key in keys:
            del self.__repo[key]

    
class repo_file_robot(repo_robot):
    def __init__(self, file_path):
        super().__init__()
        self.__file_path = file_path
        self.__load_from_file()

    def __load_from_file(self):
        self.clear_repo()
        try:
            file = open(self.__file_path, "r")
        except IOError:
            return
        
        line = file.readline().strip()
        while line != "":
            line_components = line.split(";")
            comenzi = line_components[3].split(",")
            # 2;33;ana are mere;up,up,down,halt,right,right,up
            # ["2",   "33",   "ana are mere",   "up,up,down,...."]

            robot = robot_class(line_components[0], line_components[1], line_components[2], comenzi)
            self.add_robot(robot)
            line = file.readline().strip()
        file.close()

    def __store_to_file(self):
        try:
            file = open(self.__file_path, "w")
        except IOError:
            return
        
        roboti = self.get_all()
        for robot in roboti:
            id = robot.get_robot_id()
            baterie = robot.get_robot_battery()
            descriere = robot.get_robot_descriere()
            comenzi = robot.get_robot_comenzi()
            robot_as_string = str(id) + ";" + str(baterie) + ";" + str(descriere) + ";"
            for comanda in comenzi:
                robot_as_string += str(comanda) + ","
            file.write(robot_as_string[:-1])
        file.close()

    def get_all(self):
        return super().get_all()
