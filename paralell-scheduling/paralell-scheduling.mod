set Tasks;
    param required_time_to_process{Tasks} >=0 integer;

param precedence{Tasks,Tasks} default 0 binary;
param M:= sum{t in Tasks} required_time_to_process[t];

#Variables
var start{Tasks} >=0;
var makespan >=0;

#Constraints
s.t. Set_makespan{t in Tasks}:
    makespan >= start[t] + required_time_to_process[t];

s.t. Must_happen_in_sequence{t in Tasks, t2 in Tasks: t2 != t and precedence[t,t2] == 1}:
    start[t2] >= start[t] + required_time_to_process[t];

#Objective
minimize Makespan:
    makespan;


solve;

printf "import pandas as pd\n";
printf "import matplotlib.pyplot as plt\n";
printf "import numpy as np\n";

printf "\nif __name__ == '__main__':";
printf "\n    vectorize = np.vectorize(int)";
printf "\n    tasks = [";
for{t in Tasks}{
    printf "'%s',",t;
}
printf "]";
printf "\n    required_time_to_process = [";
for{t in Tasks}{
    printf "'%d',",required_time_to_process[t];
}
printf "]";
printf "\n    start = [";
for{t in Tasks}{
    printf "'%d',",start[t];
}
printf "]";
printf "\n    fig, ax = plt.subplots(1, figsize=(16,6))";
printf "\n    ax.barh(tasks,vectorize(required_time_to_process), left=vectorize(start))";
printf "\n    plt.show()";

end;