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

s.t. Set_order_among_same_starts_1{m in Machines, t in Tasks, t2 in Tasks: t2 != t}:
    start[t2] >= start[t] + required_time_to_process[t] - M * (3-assign[t,m]-assign[t2,m]-preceed[t,t2]);

s.t. Set_order_among_same_starts_2{m in Machines, t in Tasks, t2 in Tasks: t2 != t}:
    start[t] >= start[t2] + required_time_to_process[t2] - M * (3-assign[t,m]-assign[t2,m]-1+preceed[t,t2]);

#Objective
minimize Makespan:
    makespan;


solve;

printf '{';
printf '"tasks": [';
for{t in Tasks, m in Machines: assign[t,m] == 1}{
    printf '{"name":';
    printf '"%s",',t;
    printf '"required_time_to_process" : ';
    printf '%d,',required_time_to_process[t];
    printf '"start" : ';
    printf '%d,',start[t];
    printf '"machine" : ';
    printf '"%s"',m;
    printf '}' & (if t == "T"&card(Tasks) then "" else ",");
}
printf ']';
printf '}';

end;