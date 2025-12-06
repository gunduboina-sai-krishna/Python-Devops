sample_tuple = ('a', 'a', 'b', 'b', 'c', 'd')
print(sample_tuple.count('a')) # counts the specific element in the tuple a repeated 2 times.
print(sample_tuple[1])
print(sample_tuple[-1]) # indexing
print(sample_tuple.index('a'))

a, b = 1, 2
print(a,b)

# sample_tuple[0] = 'xyz'
# print(sample_tuple) # TypeError: 'tuple' object does not support item assignment - tuple is immutable


# how to change the tuple and create the new_tuple
sample_tuple = ('abc', 'def', 'ghi')
new_tuple = ('xyz',) + sample_tuple[:]
print(new_tuple)  