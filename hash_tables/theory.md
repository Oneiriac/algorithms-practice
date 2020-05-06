## Simple uniform hashing

Assumption 1: an ideal hashing function will evenly distribute items into the slots of a hash table (i.e. **uniformly**)

Assumption 2: each key's mapping in the hash table is **independent** of another key's mapping

### SUHA and separate chaining

If we have n keys to be stored and m slots in the table, what is the expected length of a chain (the **load factor**)?

- n/m = alpha: assuming independence, the chance of a given key going to any given slot is 1/m. Summed together n times, we get n/m
- As long as m is theta n, alpha will be constant.
- Running time is at least 1 + alpha

## Hash functions

### Method 1: division

h(k) = n mod m

In theory, very bad; in practice, okay when m is prime and not close to a power of 2 or power of 10

### Method 2: multiplication

1. Multiply key by a constant A, 0 < A < 1
2. Remove fractional part of product (by subtracting floored product)
3. Multiply value by m
   h(k) = m\*( A\*k - floor(A\*k) )

Usually m is a power of 2 to allow more efficient bit-level operations.

### Method 3: Universal hashing

Choosing a random hash function:

1. k mod m (to make sure it's between 0 and m-1)
2. Two random numbers a and b b/w 0 and p-1, where p is a very large prime number

h(k) = (a\*k mod b) mod m

This means that even for worst-case keys, probabilities of collision is 1/m
