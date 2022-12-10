set Tasks;
    param required_time_to_process{Tasks} >=0 integer;
set Machines;

param precedence{Tasks,Tasks} default 0 binary;
param M:= sum{t in Tasks} required_time_to_process[t];

#Variables
var start{Tasks} >=0;
var makespan >=0;
var assign{Tasks,Machines} binary;
var preceed{Tasks, Tasks} binary;

#Constraints
s.t. Set_makespan{t in Tasks}:
    makespan >= start[t] + required_time_to_process[t];

s.t. Must_happen_in_sequence{m in Machines, t in Tasks, t2 in Tasks: t2 != t and precedence[t,t2] == 1}:
    start[t2] >= start[t] + required_time_to_process[t];

s.t. One_machine_per_task{t in Tasks}:
    sum{m in Machines} assign[t,m] = 1;

s.t. Set_order_among_same_starts{m in Machines, t in Tasks, t2 in Tasks: t2 != t}:
    start[t2] >= start[t] + required_time_to_process[t] - M * (2-assign[t,m]-assign[t2,m]+1-preceed[t,t2]);

#Objective
minimize Makespan:
    makespan;


solve;

printf "import pandas as pd\n";
printf "import matplotlib.pyplot as plt\n";
printf "import numpy as np\n";
printf "from matplotlib.patches import Patch\n";
printf "from random import randrange\n";

printf "\ndef get_random_color():";
printf "\n    return '#{:06x}'.format(randrange(256 ** 3))\n";

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
printf "\n    colors_for_machines = {";
for{m in Machines}{
printf "'%s': get_random_color(),",m;
}
printf "}";
printf "\n    legends = [Patch(facecolor=colors_for_machines[i], label=i) for i in colors_for_machines]";
printf "\n    fig, ax = plt.subplots(1, figsize=(16,6))";
printf "\n    ax.barh(tasks,vectorize(required_time_to_process), left=vectorize(start),";
printf "\n    color=[colors_for_machines[i] for i in colors_for_machines])";
printf "\n    plt.legend(handles=legends)";
printf "\n    plt.show()";

end;