from json import load, dumps
from typing import TypedDict
from util import generate_unique_color
from textwrap import dedent

class Task(TypedDict):
    name: str
    machine: str
    start: int
    duration: int

class Machine(TypedDict):
    name: str
    color: str

class Jobshop:
    def __init__(self, filepath:str) -> None:
        self._machines:list[Machine] = list()
        self._tasks:list[Task] = list()
        
        with open(filepath) as file_data:
            data = load(file_data)
            machine_colors:dict[str, str] = dict()
            machine_names:set[str] = set()

            for task in data["tasks"]:
                self._tasks.append(task)
                machine_name = task["machine"]

                if machine_name not in machine_names:
                    color = generate_unique_color([color for color in machine_colors.values()])
                    self._machines.append({"name": machine_name, "color": color})
                    machine_names.add(machine_name)
                    machine_colors.update({machine_name: color})

    def __str__(self) -> str:
        tasks = dumps(self._tasks, indent=4)
        machines = dumps(self._machines, indent=4)
        return dedent(
            """\
            Tasks:{0}
            Machines:{1}
            """).format(tasks, machines)

    def get_machines(self) -> list[Machine]:
        return self._machines

    def get_tasks(self) -> list[Task]:
        return self._tasks
