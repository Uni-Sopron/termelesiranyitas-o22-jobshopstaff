import matplotlib.pyplot as plt
from jobshop import Task, Job
from matplotlib.patches import Patch

def set_base_colors() -> None:
    plt.figure(facecolor='#262626', figsize=(16,9))
    ax = plt.axes()
    ax.set_facecolor("#262626")
    ax.spines["left"].set_color("white")
    ax.spines["bottom"].set_color("white")
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.tick_params(colors='white')

def set_main_labels() -> None:
    plt.title("Jobshop", color="white")
    plt.xlabel("Time", color="white")
    plt.ylabel("Machines", color="white")

def set_data_labels(tasks:list[Task]) -> None:
    for task in tasks:
        x = task["start"] + task["duration"]/2.0
        y = task["machine"]
        plt.text(x, y, task["name"], ha = 'center', color="white", bbox = dict(facecolor = 'grey', alpha =.8))

def set_legends(jobs:list[Job]) -> None:
    handles: set[(str,str)] = set()
    for job in jobs:
        handles.add((job["color"], job["name"]))
    plt.legend(handles=[Patch(facecolor=c, label=n) for (c,n) in handles])

class TaskPlotter:
    def __init__(self, tasks:list[Task], jobs:list[Job]) -> None:
        set_base_colors()
        set_main_labels()
        set_data_labels(tasks)
        set_legends(jobs)
        plt.barh(
            [task["machine"] for task in tasks],
            [task["duration"] for task in tasks],
            left=[task["start"] for task in tasks],
            color = [next(job["color"] for job in jobs if job["name"] == task["job"]) for task in tasks],
            edgecolor= "white"
        )
     
    def plot(self) -> None:
        plt.show()