# aoc-2023

`my solutions for aoc 2023 (done in 2024 bc college apps)`

## My Solutions

**Day 11**

Part 1:

Loop through the dataset row-wise, creating a 2D array as you go which tracks the 
value and position of each object. Keep track of the total number of empty rows
you have encountered, and for every object you encounter, add it's row index
in the dataset to the number of empty rows seen so far. Do the same for columns,
updating the new 2D array. From there, simply loop through each pair of 
galaxies, using the formula `abs(x2 - x1) + abs(y2 - y1)` to find the distance
between each.

Part 2:

Same as part 1, but rather than incrementing the empty row/col counter by `1`,
increase it by `999999`.

**Day 10**

Part 1:

Brute force; follow the path as if it were a linked list via recursion,
saving the distance of each node as you go. Answer will be the ceiling quotient
of the max distance and 2.

Part 2:

Consider one row of map: `.....|..|.....`. It is evident that in this row, two
points are _necessarily_ part of the loop, as we entered the loop at the first
pole, and exited at the second. If you consider a more complicated row:
`...|..||..|...`, it is evident here that 4 points are part of the loop, by the
same reasoning. To do this analysis on every row, simply keep track of the
vertical direction of each node in the loop; only points that are not `.` are
necessary to track, since they are the only ones that move vertically. To
calculate direction, simply look at the previous and next nodes in the loop
to see if the row changes. From there, loop through each row, and keep track
of the number of times the direction has changed during the iteration to find
out whether or not a point on the map in question is in or out of the loop.
No complicated dfs needed!

**Day 9**

Part 1 & 2:

Brute force; constructing the derivative arrays for each row.

**Day 8**

Part 1:

Simple brute force.

Part 2:

What is not mentioned in the prompt is that for the input set, every ghost only
has one 'Z' node that it continuously loops on. Therefore, for every ghost, we
can write an equation `pos(n) = first_z_pos + distance_between_zs * n`
. It also turns out, (and this is also not mentioned in the prompt), that
`first_z_pos` and `distance_between_zs` is equal. So, we can write the relation,
`d0 * a = d1 * b = d2 * c = d3 * d = d4 * e = d5 * f`, where each `d` is the
distance between zs for each ghost `a-f`. To solve this system, find the LCM of the
5 coefficients.

**Day 7**

Part 1:

To calculate the type of hand, build a frequency list of characters in the card,
and do some basic control flow to differentiate between cards based on the max
frequency and number of distinct cards. Loop through all the hands, and store them
in 7 different arrays associated with their hand type. Sort each array with the
comparison function checking characters 1 by 1 in the hand as per the puzzle. Then,
simply calculate the total winnings.

Part 2:

Same as p1, but with two changes. 1: in the type calculation, account for jokers
by treating them as the highest frequency non-joker card. This will always lead
to the most optimal "joker-upgrade." 2: in the comparison, treat 'J' as the
smallest number, as per the puzzle.

**Day 6**

Part 1:

Quadratic formula.

Part 2:

Quadratic formula.

**Day 5**

Part 1:

Construct 'map' objects that are able to convert a specific number through the map.
Loop through all the seeds and all the maps to get the final locations.

Part 2:

Construct 'map objects in the same way, but the conversion function takes in a
list of 'ranges'. For each range, find the first place where the range should be 'split'
(namely, where a mapping starts or end within that range). Split the range, and add the
right-split back to the ranges list, guaranteeing that the left-split of the range can
be cleanly converted. Do that for each map, and the smallest starting number for the
final ranges will be the smallest location.

**Day 4**

Part 1:

Put all winners in a set, check the rest of the numbers against that set.

Part 2:

Same as p1, but add the number of winners calculated multiplied by the number of winners associated with that card.

**Day 3**

Part 1:

Basically the brute force method; Look for numbers in each row, once found, enter a
search that goes through each neighbour looking for symbols.

Part 2:

Exact same as part 1, but every time a gear is found, the associated number is stored
with it in a set (the set contains arrays of numbers, representing the tooth-count).

**Day 2**

Part 1:

Loop through pulls to check for validity against a map of values

Part 2:

For each game, keep a map of min values, and update them by checking through
each pull.

**Day 1**

Part 1:

Loop through characters, find digits

Part 2:

Loop through the line, checking slices of length 5 to see if they're digits.
