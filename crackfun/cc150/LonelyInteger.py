# Method: use hashtable

# Time O(n)
# Space O(n)

def lonelyInteger(array):
    result = 0
    for x in array:
        result^= x
    return result
# This bit operation reduces the space complexity a lot.

'''
More about bit operations
'''

