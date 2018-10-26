# Python dictionary is an unordered collection of items. While other compound data types
# have only value as an element, a dictionary has a key: value pair.
# Dictionary Syntax: {'Key1': 'Value1', 'Key2': 'Value2'}
# Empty Dictionary
d1 = {}
print(d1)

# Non-Empty Dictionary
d1 = {'a': 'Some Values', 'b': [1, 2, 3, 4]}
print(d1)

# Note: Dictionary Keys Should be Unique and immutable(not changeable) in nature.
# If we put non-unique (Repeated) keys in Dict and print Dict, we will get union of all keys and there values
# will be the last updated from right.
d1 = {'p': 'sdf', 'a': 'Some Values', 'b': [1, 2, 3, 4], 'b': 34, 'b': 454, 'a': 'DP', 'aa': 'yo', 'a': 'rr'}
print(d1)

# Access, insert or set elements using the same syntax
# for Set
d1 = dict({'a': 'Some Values', 'b': [1, 2, 3, 4]})
d1[7] = 'an integer'
print(d1)
# for access
print(d1['b'])
# for set elements
d1['b'] = [4, 3, 2, 1]
print(d1)

# check for a 'Key' if it is there in a dict or not.
# we use the same syntax for checking values in a list or tuple
# Syntax: <key> in <dict name>
print('b' in d1)

# Delete operation in dict
# using del or pop keyword
# we give key value to del/pop for delete
# syntax: del <dict_name[<key>]> or <dictionary_name_object>.pop(<key>)
d1[5] = 'some value'
print(d1)
d1['dummy'] = 'another value'
print(d1)
del d1[5]
print(d1)
# Deleted value capture against key
# pop method of dict always returns a deleted value against key of a dict
deleted_value = d1.pop('dummy')
print(deleted_value)
print(d1)

# keys() and values() method of dict give us iterators of the dict's keys and values respectively
# these functions out put the keys and value in the same order.
print(d1.keys())
print(d1.values())

# Merging of one dict into another dict by using update method of dict.
# Note: when we merge 1 dict into another then if both the dict got same key/keys then the
# key/keys=>value/values will get updated with the merging dict key/keys=>value/values.
# update takes only one argument at a time.
d1.update({'b': 'foo', 'c': 12})
print(d1)

# How to Create Dictionaries from Sequences.
# sequence1 be like ['Physics', 'Chemistry', 'Maths']
# sequence2 be like [91, 88, 89]
# dictSeq1Seq2 {'Physics': 91, 'Chemistry': 88, 'Maths': 89}

# Method 1
sequence1 = ['Physics', 'Chemistry', 'Maths']
sequence2 = [91, 88, 89]
dictSeq1Seq2 = {}
for key, value in zip(sequence1, sequence2):
    dictSeq1Seq2[key] = value
print(dictSeq1Seq2)

# Method 2
# Since a dict is essentially a collection of 2-tuples.
# the dict function accepts a list of 2-tuples. Ex. [('Physics', 91), ('Chemistry', 88), ('Maths', 89)]
# zip() function returns a list of tuples like this [('Physics', 91), ('Chemistry', 88), ('Maths', 89)]
dictSeq1Seq2 = dict(zip(sequence1, sequence2))
print(dictSeq1Seq2)
print(dict(zip(['Ram', 'Ravi'], [(1, 2), (3, 4)])))


# How to Get value of a dict against key
# Methon 1
dd = {'divesh': 14, 'Ravi': 2}
if 'divesh' in dd:
    value = dd['divesh']
else:
    value = 7
print(value)

# Methon 2
print(dd.get('divesh'))

# Exercise: we have a list of words : ['apple', 'bat', 'bar', 'atom', 'book']
# we want the following output like this: dict1 : {'a': ['apple', 'atom',], 'b': ['bat', 'bar', 'book']}
# Method 1
dict1 = {}
words = ['apple', 'bat', 'bar', 'atom', 'book']
for word in words:
    letter = word[0]
    value = dict1.get(letter)
    if value is None:
        dict1[letter] = [word]
    else:
        dict1[letter].append(word)
print(dict1)

# Method 2
# setdefault() dict method is precisely for this purpose or this exercise.
dict1 = {}
for word in words:
    letter = word[0]
    dict1.setdefault(letter, []).append(word)
print(dict1)

# Method 3
# more easier way to do this exercise by importing a package called collection.
# the built-in collection module has a useful class, defaultdict.

from collections import defaultdict
# dict1 = {}
dict1 = defaultdict(list)
for word in words:
    dict1[word[0]].append(word)
print(dict1)

# How to check a key is valid for a dict or not
# while the values of a dict can be any Python Object, the keys generally have to be immutable object like scalar types
# (int, float , string) or tuples ( all objects in the tuple need to be immutable too)
# Technical term we use here is "Hashability".
# we can check whether an object is hashable (can be used as a key in a dict) with the hash function.
# Example
hash('string')
hash((1, 2, (2, 3)))
# hash((1, 2, [2, 3]))  # this one fails because lists are mutable.

# to use a list as a key, one option is to convert it to a tuple, which can be hashed as long as its elements also can.
dd = {}
dd[tuple([1, 2, 3])] = 5
print(dd)
