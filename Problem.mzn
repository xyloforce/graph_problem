include "alldifferent.mzn";
/*#### Parameters ####*/
enum States_available; /* is nodes */
set of int: number_States;
set of States_available: axe1;
set of States_available: axe2;
array[axe1, axe2] of bool: share_species;
array[axe1, axe2] of bool: incompatibilities;

/*#### Vars ####*/
array[number_States] of var States_available: ordering;
constraint alldifferent(ordering);
/*#### Constraints ####*/
constraint forall(i in number_States)(forall(j in number_States)(if j > i /\ share_species[ordering[i],ordering[j]]=true then forall(k in number_States)(if k > i/\ share_species[ordering[i], ordering[k]]=true then if share_species[ordering[j], ordering[k]]=true then true else if incompatibilities[ordering[k],ordering[j]]=false then true else false endif endif else true endif) else true endif));

solve satisfy;