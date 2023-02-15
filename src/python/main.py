from jobshop import Jobshop
from taskplotter import TaskPlotter

if __name__ == '__main__':
        while True:
            try:
                filename = input("Filename: ")
                jobshop = Jobshop(filename)
            except FileNotFoundError:
                print(f"\nThe file '{filename}' was not found.")
                continue
            
            TaskPlotter(jobshop.get_tasks()).plot()
            break
