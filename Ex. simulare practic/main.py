from repo.repo_robot import repo_file_robot
from service.service_cerinte import service_cerinte
from ui.interfata import ui

repo = repo_file_robot("database/roboti.txt")

serv_cerinte = service_cerinte(repo)

inter = ui(serv_cerinte)
inter.run_c()


