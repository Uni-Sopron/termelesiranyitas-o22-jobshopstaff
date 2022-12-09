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

s.t. Must_happen_in_sequence_1{t in Tasks, t2 in Tasks: t2 != t and precedence[t,t2] == 1}:
    start[t2] >= start[t] + required_time_to_process[t];

#Objective
minimize Makespan:
    makespan;


solve;

for{t in Tasks}{
    printf "Elvégzendő feladat kódja: %s\nIdőtartama: %d - %d\n\n", t, start[t], start[t] + required_time_to_process[t];
}
printf "A gyártási idő, ha nem ütemezünk, összesen: %d óra.", M;

end;