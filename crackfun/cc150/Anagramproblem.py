''''
Anagrams: Same Letter, Same Counts, different orders
Given two strings, how any characters do we need to remove from either to make them anagrams?
Example:
    hello and billion ---> llo and llo,  return 6
    glue and legs ---> gle and leg, return 2
    candy and day --> ady and day, return 2
'''
import collections
def anagram(s,t):
    ds = collections.Counter(s)
    dt = collections.Counter(t)
    delta1 = ds - dt
    delta2 = dt - ds

    return sum(delta1.values())+sum(delta2.values())



