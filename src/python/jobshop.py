from json import load, dumps
from typing import TypedDict
from util import generate_unique_color
from textwrap import dedent

class Task(TypedDict):
    name: str
    machine: str
    start: int
    duration: int
    job: str

class Machine(TypedDict):
    name: str

class Job(TypedDict):
    name: str
    color: str

class Jobshop:
    def __init__(self, filepath:str) -> None:
        self._machines:list[Machine] = list()
        self._tasks:list[Task] = list()
        self._jobs:list[Job] = list()
        
        with open(filepath) as file_data:
            data = load(file_data)
            job_colors:dict[str, str] = dict()
            machine_names:set[str] = set()
            job_names:set[str] = set()

            for task in data["tasks"]:
                self._tasks.append(task)
                machine_name = task["machine"]
                job_name = task["job"]

                if job_name not in job_names:
                    color = generate_unique_color([color for color in job_colors.values()])
                    self._jobs.append({"name": job_name, "color": color})
                    job_names.add(job_name)
                    job_colors.update({job_name: color})

                if machine_name not in machine_names:
                    self._machines.append({"name": machine_name})
                    machine_names.add(machine_name)


    def __str__(self) -> str:
        jobs:dict[str, list[Task]] = dict()
        for job in self._jobs:
            job_name = job["name"]
            for task in self._tasks:
                if task["job"] == job_name:
                    try:
                        jobs[job_name].append(task)
                    except KeyError:
                        jobs[job_name] = list()
                        jobs[job_name].append(task) 

        j = dumps(jobs, indent=4)
        m = dumps(self._machines, indent=4)
        return dedent(
            """\
            Jobs: {0}
            Machines: {1}
            """).format(j, m)

    def get_machines(self) -> list[Machine]:
        return self._machines

    def get_tasks(self) -> list[Task]:
        return self._tasks
    
    def get_jobs(self) -> list[Job]:
        return self._jobs
