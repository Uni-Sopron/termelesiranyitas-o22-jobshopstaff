import matplotlib.pyplot as plt
from matplotlib.patches import Patch
from random import randrange
from json import load

def rand_color():
    return '#{:06x}'.format(randrange(256 ** 3))

if __name__ == '__main__':
    with open("result.json") as json_data:
        data = load(json_data)
        # vectorize = np.vectorize(int)
        colors_for_machines = dict()
        machines = set()
        for task in data["tasks"]:
            if task["machine"] in machines:
                task = {**task, "color": colors_for_machines[task["machine"]]}
            else:
                color = rand_color()
                task = {**task, "color": color}
                machines.add(task["machine"])
                colors_for_machines[task["machine"]] = color

        task_list = [task["name"] for task in data["tasks"]]
        legends = [Patch(facecolor=colors_for_machines[i], label=i) for i in colors_for_machines]
        req_time_list = [task["required_time_to_process"] for task in data["tasks"]]
        start_list = [task["start"] for task in data["tasks"]]
        color_list = [colors_for_machines[i] for i in colors_for_machines]

        fig, ax = plt.subplots(1, figsize=(16,6))
        ax.barh(task_list,req_time_list, left=start_list,
        color= color_list)
        plt.legend(handles=legends)
        plt.show()