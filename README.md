# aoc-2023

`my solutions for aoc 2023 (done in 2024 bc college apps)`

## My Solutions

**Day 8**

Part 1:

Simple brute force.

Part 2:

> Easier solution than what I did; find the LCM of the 6 coefficients mentioned
> later in the solution.

What is not mentioned in the prompt is that for the input set, every ghost only
has one 'Z' node that it continuously loops on. Therefore, for every ghost, we
can write an equation `pos(n) = first_z_pos + distance_between_zs * n`
. It also turns out, (and this is also not mentioned in the prompt), that
`first_z_pos` and `distance_between_zs` is equal. So, we can write the relation,
`d0 * a = d1 * b = d2 * c = d3 * d = d4 * e = d5 * f`, where each `d` is the
distance between zs for each ghost `a-f`. My code calculates those coefficiants
and prints out an equation that can be plugged in to any computer algebra system
--I used WolframAlpha--to solve for an integer solution. Once an integer
solution for `a-f` is obtained, simply choose any of the ghosts, multiply the
integer solution provided by the coefficiant, and that will be the total number
of steps.

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
