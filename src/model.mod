set Tasks;
    param duration{Tasks} >=0 default 15 integer;
    param precedence{Tasks} default 0 integer;
set Machines;

param can_handle{Machines, Tasks} default 0 binary;
param M:= sum{t in Tasks} duration[t];

#Variables
var start{Tasks} >=0;
var makespan >=0;
var assign{Tasks,Machines} binary;
var preceeds{Tasks, Tasks} binary;

#Constraints
s.t. Set_makespan{t in Tasks}:
    makespan >= start[t] + duration[t];

s.t. Must_happen_in_sequence{m in Machines, t in Tasks, t2 in Tasks: t2 != t and precedence[t] < precedence[t2]}:
    start[t2] >= start[t] + duration[t];

s.t. Do_what_you_can{m in Machines, t in Tasks: can_handle[m,t] == 0}:
    assign[t,m] = 0;

s.t. One_machine_per_task{t in Tasks}:
    sum{m in Machines} assign[t,m] = 1;

s.t. Set_order_among_same_starts_1{m in Machines, t in Tasks, t2 in Tasks: t2 != t}:
    start[t2] >= start[t] + duration[t] - M * (3-assign[t,m]-assign[t2,m]-preceeds[t,t2]);

s.t. Set_order_among_same_starts_2{m in Machines, t in Tasks, t2 in Tasks: t2 != t}:
    start[t] >= start[t2] + duration[t2] - M * (3-assign[t,m]-assign[t2,m]-1+preceeds[t,t2]);

#Objective
minimize Makespan:
    makespan;

solve;

printf '{"tasks": [';
for{t in Tasks, m in Machines: assign[t,m] == 1}{
    printf '{"name": "%s",',t;
    printf '"machine" : "%s",',m;
    printf '"start" : %d,', start[t];
    printf '"duration": %d', duration[t];
    printf '}' & (
        if t == "T"&card(Tasks)
        then ""
        else ","
        );
}
printf ']}';

end;
