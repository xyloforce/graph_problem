/*#### Parameters ####*/
enum States_available = {A1,B1,C1,B2}; /* is nodes */
set of States_available: incompatibility1 = {B1, B2};
set of int: number_States = 1..4;

set of States_available: axe1=A1..B2;
set of States_available: axe2=A1..B2;

array[axe1, axe2] of bool: share_species = [| true, true, true, true | true, true, true, false | true, true, true, true | true, false, true, true |];

/*#### Vars ####*/
array[axe1, axe2] of var bool: adjacency;
/*#### Constraints ####*/
constraint forall(i in axe1, j in axe2) (adjacency[i,j] = share_species[i,j]); /* states sharing a species are adjacent */

/* ensure that no node of identical color are adjacent */

constraint forall(i in incompatibility1) (forall (j in incompatibility1)(if j != i then adjacency[i,j]=false else true endif));

/* for all i, k */
array[number_States] of var States_available: ordering;
constraint forall(i in number_States, k in axe2)(forall (j in number_States)(if adjacency[ordering[i], ordering[j]]==true \/ j > i \/ adjacency[ordering[i], k]==true then adjacency[ordering[j], k]=true else false endif));
solve satisfy;
/* constraint forall(i,j in axe1, k in axe2)(if k, j in simpliciaux then do nothing else if adjacency[i,j]=true and adjacency[k,j]=true then simpliciaux += i else do nothing endif) */