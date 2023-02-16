from jobshop import Jobshop
from taskplotter import TaskPlotter
from os.path import join, dirname

if __name__ == '__main__':
        while True:
            try:
                filename = input("Filename: ")
                directory = dirname(__file__)
                filepath = join(directory, "../../result",filename)
                print(filepath)
                jobshop = Jobshop(filepath)
            except FileNotFoundError:
                print(f"\nThe file '{filename}' was not found in the folder 'result'.")
                continue
            
            TaskPlotter(jobshop.get_tasks()).plot()
            break
