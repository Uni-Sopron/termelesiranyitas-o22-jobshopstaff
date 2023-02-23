from jobshop import Jobshop
from taskplotter import TaskPlotter
from os.path import join, dirname

if __name__ == '__main__':
        while True:
            try:
                filename = input("Filename: ")
                directory = dirname(__file__)
                filepath = join(directory, "../../result",filename)
                jobshop = Jobshop(filepath)
                print(jobshop)
            except FileNotFoundError:
                print(f"\nThe file '{filename}' was not found in the folder 'result'.")
                continue
            TaskPlotter(jobshop.get_tasks(), jobshop.get_jobs()).plot()
            break
