/*#### Parameters ####*/
enum States_available = {P1, C1, A1, Z2, A2, C2, C3, M3, V3, F4, A4}; /* is nodes */
set of States_available: axe1=P1..A4;
set of States_available: axe2=P1..A4;

array[axe1, axe2] of bool: share_species = [|;
array[axe1, axe2] of var bool: adjacency;

int: total_states = 11; /* number of nodes */

/*#### Vars ####*/
/*float: n_max_edges = 2*total_states-2/2;*/


/*#### Constraints ####*/



/* predicate connected(
array [int] of $$N: from,
array [int] of $$N: to,
array [$$N] of var bool: ns,
array [int] of var bool: es
)*/