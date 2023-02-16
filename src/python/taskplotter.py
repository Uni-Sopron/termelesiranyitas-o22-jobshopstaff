import matplotlib.pyplot as plt
from matplotlib.patches import Patch
from jobshop import Task, Jobshop

class TaskPlotter:
    def __init__(self, tasks:list[Task]) -> None:
        plt.figure(facecolor='#262626', figsize=(16,9))
        ax = plt.axes()
        ax.set_facecolor("#262626")
        ax.spines["left"].set_color("white")
        ax.spines["bottom"].set_color("white")
        ax.spines["top"].set_visible(False)
        ax.spines["right"].set_visible(False)
        ax.tick_params(colors='white')
        plt.title("Tasks", color="white")
        plt.xlabel("Time", color="white")
        plt.ylabel("Tasks", color="white")
        plt.grid(axis="x")
        handles: set[(str,str)] = set()
        for task in tasks:
            handles.add((task["color"], task["machine"]))
        plt.legend(handles=[Patch(facecolor=c, label=m) for (c,m) in handles])
        plt.barh(
            [task["name"] for task in tasks],
            [task["duration"] for task in tasks],
            left=[task["start"] for task in tasks],
            color = [task["color"] for task in tasks]
        )
     
    def plot(self) -> None:
        plt.show()