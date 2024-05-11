---
title: One new but naive way to generate prime numbers and one Brute force method.
author: Amit Kumar
date: 11th May, 2024 (11:41AM) +05:30 GMT
---
Wrote two classes to generate prime numbers:

- PrimeAndFactorials
- PrimeAndFactorials2 (Brute Force method; Nothing new; Definition of Prime numbers)

PrimeAndFactorials is hopefully novel but also very naive for sure, since the time complexity w.r.t eratosthenes is high. See below comparisons for timeit results. I am sharing it only because the method seems to be different and not because it is any performant. Somebody may utilize this work for entirely different purpose.

```python
>>> import timeit
>>> timeit.timeit(stmt='primeObj1 = primeAndFactorials();primeObj1.find_next_prime(cutOffLargestPrimesRequired=1000, byLength=False)',setup='from PrimeAndFactorials import primeAndFactorials', number=5)
0.2627572159981355
>>> timeit.timeit(stmt='primeObj2 = primeAndFactorials2();primeObj2.find_next_prime(cutOffLargestPrimesRequired=1000, byLength=False)',setup='from PrimeAndFactorials2 import primeAndFactorials2', number=5)
0.009428285000012693
>>> timeit.timeit(stmt='eratosthenes(maximum=1000)',setup='from eratosthenes import eratosthenes', number=5)
0.0010897209999711777
```
As you can see PrimeAndFactorials is >100 times worse than eratosthenes while PrimeAndFactorials (Brute force) is > 8 times worse than eratosthenes.


