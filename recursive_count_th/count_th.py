'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''

def count_th(word):

    if len(word) < 2:
        return 0

    if word[0] == "t" and word[1] == "h":
        return 1 + count_th(word[1:]) # slicing the word at that index and passing that new word in

    else:
        return count_th(word[1:]) # slicing the word at that index and passing that new word in
# base case

# must change state toward base case
# must call itself

# Create a base case and work toward it:
    # if length of word is less than 2 (the length of th)
# check to see if zeroth and 1st index have th, if so, return the count and then reinsert the word at the the 2nd index to reevaluate
# if not, don't return a count, but reevaluate at the 2nd index