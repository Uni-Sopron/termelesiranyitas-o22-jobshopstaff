import matplotlib.pyplot as plt
from jobshop import Task, Machine

def add_labels_to_plotter(tasks:list[Task]) -> None:
    for task in tasks:
        x = task["start"] + task["duration"]/2.0
        y = task["machine"]
        plt.text(x, y, task["name"], ha = 'center', color="white", bbox = dict(facecolor = 'grey', alpha =.8))

class TaskPlotter:
    def __init__(self, tasks:list[Task], machines:list[Machine]) -> None:
        plt.figure(facecolor='#262626', figsize=(16,9))
        ax = plt.axes()
        ax.set_facecolor("#262626")
        ax.spines["left"].set_color("white")
        ax.spines["bottom"].set_color("white")
        ax.spines["top"].set_visible(False)
        ax.spines["right"].set_visible(False)
        ax.tick_params(colors='white')
        plt.title("Jobshop", color="white")
        plt.xlabel("Time", color="white")
        plt.ylabel("Machines", color="white")
        add_labels_to_plotter(tasks)
        plt.barh(
            [task["machine"] for task in tasks],
            [task["duration"] for task in tasks],
            left=[task["start"] for task in tasks],
            color = [next(machine["color"] for machine in machines if machine["name"] == task["machine"]) for task in tasks],
            edgecolor= "white"
        )
     
    def plot(self) -> None:
        plt.show()