import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

if __name__ == '__main__':
    vectorize = np.vectorize(int)
    tasks = ['T1','T2','T3','T4','T5','T6','T7','T8',]
    required_time_to_process = ['7','10','9','5','3','1','4','2',]
    start = ['0','7','0','9','14','17','18','22',]
    fig, ax = plt.subplots(1, figsize=(16,6))
    ax.barh(tasks,vectorize(required_time_to_process), left=vectorize(start))
    plt.show()