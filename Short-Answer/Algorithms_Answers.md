#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.


## Exercise I

a)
O(n)

b)
O(n^^2)

c)
O(n)

## Exercise II

Firstly, it says we have plenty of eggs.  We should just let people throw the eggs. 🥚

But since we want to minimize the egg breaking we'll maybe do the following:

- Since we don't know where the egg breaks or doesn't in a building of n floors, let's cut the floors in half and drop our egg from the middle floor.
- If the egg doesn't break, we're good and can go home.
- If the egg breaks, we've eliminated all of the higher floors, but because it breaks still, we need to do another half.
- With our new middle floor from the lower half, we'll check again to see if our egg breaks.
- We'll keep repeating this process until we find a middle floor that doesn't break our egg.

We're essentially using binary search, which has time complexity of O(log n) - since we're cutting things in half.
