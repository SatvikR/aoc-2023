# aoc-2023

`my solutions for aoc 2023 (done in 2024 bc college apps)`

## My Solutions

**Day 6**

Part 1:

Quadratic formula.

Part 2:

Quadratic formula.

> why???

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
