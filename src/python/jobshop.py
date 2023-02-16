from json import load, dumps
from typing import TypedDict, Optional
from util import generate_unique_color

class Task(TypedDict):
    name: str
    machine: str
    start: int
    duration: int
    color: Optional[str]

class Jobshop:
    def __init__(self, filepath:str) -> None:
        self._machines:set[str] = set()
        self._tasks:list[Task] = list()
        
        with open(filepath) as file_data:
            data = load(file_data)
            machine_colors:dict[str, str] = dict()
            self._tasks.extend(data["tasks"])
            
            for task in self._tasks:
                if task["machine"] in self._machines:
                    machine = task["machine"]
                    color = machine_colors[machine]
                    task.update({"color": color})
                else:
                    machine = task["machine"]
                    color = generate_unique_color([color for color in machine_colors.values()])
                    self._machines.add(machine)
                    task.update({"color": color})
                    machine_colors.update({machine: color})

    def __str__(self) -> str:
        return dumps(self._tasks, indent=4)

    def get_machines(self) -> set[str]:
        return self._machines

    def get_tasks(self) -> list[Task]:
        return self._tasks
