include "alldifferent.mzn";
/*#### Parameters ####*/
enum States_available = {A1,B1,C1,B2}; /* is nodes */
set of int: number_States = 1..4;
set of States_available: axe1=A1..B2;
set of States_available: axe2=A1..B2;
array[axe1, axe2] of bool: share_species = [| true, true, true, true | true, true, true, false | true, true, true, true | true, false, true, true |];
array[axe1, axe2] of bool: incompatibilities = [| false, false, false, false | false, false, false, true | false, false, false, false | false, true, false, false |];

/*#### Vars ####*/
array[number_States] of var States_available: ordering;
constraint alldifferent(ordering);
/*#### Constraints ####*/
constraint forall(i in number_States)(forall(j in number_States)(if j > i /\ share_species[ordering[i],ordering[j]]=true then forall(k in number_States)(if k > i/\ share_species[ordering[i], ordering[k]]=true then if share_species[ordering[j], ordering[k]]=true then true else if incompatibilities[ordering[k],ordering[j]]=false then true else false endif endif else true endif) else true endif));

solve satisfy;
/* constraint forall(i,j in axe1, k in axe2)(if k, j in simpliciaux then do nothing else if adjacency[i,j]=true and adjacency[k,j]=true then simpliciaux += i else do nothing endif) */