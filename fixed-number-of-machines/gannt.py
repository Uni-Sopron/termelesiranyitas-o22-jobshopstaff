import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Patch
from random import randrange

def get_random_color():
    return '#{:06x}'.format(randrange(256 ** 3))

if __name__ == '__main__':
    vectorize = np.vectorize(int)
    tasks = ['T1','T2','T3','T4','T5','T6','T7','T8',]
    required_time_to_process = ['7','10','9','5','3','1','4','2',]
    start = ['0','7','0','17','17','22','23','27',]
    colors_for_machines = {'M0': get_random_color(),'M1': get_random_color(),'M2': get_random_color(),}
    legends = [Patch(facecolor=colors_for_machines[i], label=i) for i in colors_for_machines]
    fig, ax = plt.subplots(1, figsize=(16,6))
    ax.barh(tasks,vectorize(required_time_to_process), left=vectorize(start),
    color=[colors_for_machines[i] for i in colors_for_machines])
    plt.legend(handles=legends)
    plt.show()