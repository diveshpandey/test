# A set is an unordered collection of unique elements.
# A set can be created in two ways. via the set function or via a set literal with {} braces.
# Set always take unique values if we repeat values it will converted into unique by default
a = set([2, 2, 3, 1, 1, 2, 3, 4, 5])
print(a)
# or
a = {2, 2, 3, 1, 1, 2, 3, 4, 5}
print(a)

# set supports mathematical set operations like union, intersection, difference and symmetric difference.
a = {1, 2, 3, 4, 5}
b = {1, 2, 3, 6, 7, 8}
print(a.union(b))
print(a | b)
print(a.intersection(b))
print(a & b)

#Python set operations table
# Function                 Alternative Syntax          Description
#   a.add(x)                   N/A                         Add element x to the set a
#   a.clear()                  N/A                         Reset the set a to an empty state, discarding all of its elements.
#   a.remove(x)                N/A                         Remove element x from a set a.
#   a.pop()                    N/A                         Remove an arbitrary element from the set a, raising keyError if the set is empty.
#   a.union(b)                 a | b                       All the union elements in a and b.
#   a.update(b)                a |= b                      Set the contents of a to be the union of the elements in a and b.
#   a.intersection(b)          a & b                       All the elements in both a and b.
#   a.intersection_update(b)   a &= b                      Set the contents of a to be the intersection of the elements in a and b.
#   a.difference(b)            a - b                       The elements in a that are not in b.
#   a.difference_update(b)     a -= b                      Set a to the elements in a that are not in b.
#   a.symmetric_difference(b)  a ^ b                       All of the elements in either a or b but not both.
#   a.symmetric_difference_update(b)    a ^= b             Set a to contain the elements in either a or b but not both.
#   a.issubset(b)              N/A                         True if the elements of a are all contained in b.
#   a.issuperset(b)            N/A                         True if the elements of b are all contained in a.
#   a.isdisjoint(b)            N/A                         True if a and b have bo elements in common.

a = {1, 2, 3, 4, 5}
b = {77, 33, 2, 3}
c = a.copy();
print(c)
c |= b
print(c)
