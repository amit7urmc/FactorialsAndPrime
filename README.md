---
title: Two new but naive ways to generate prime numbers.
author: Amit Kumar
date: 11th May, 2024 (09:12AM) +05:30 GMT
---
Wrote two classes to generate prime numbers:

- PrimeAndFactorials
- PrimeAndFactorials2

They are hopefully novel but also naive for sure, since the time complexity w.r.t eratosthenes is high. See below comparisons for timeit results. I am sharing it only because the methods seem to be different and not because they are any performant. Somebody may utilize this work for entirely different purpose.

```python
>>> import timeit
>>> timeit.timeit(stmt='primeObj1 = primeAndFactorials();primeObj1.find_next_prime(cutOffLargestPrimesRequired=1000, byLength=False)',setup='from PrimeAndFactorials import primeAndFactorials', number=5)
0.2627572159981355
>>> timeit.timeit(stmt='primeObj2 = primeAndFactorials2();primeObj2.find_next_prime(cutOffLargestPrimesRequired=1000, byLength=False)',setup='from PrimeAndFactorials2 import primeAndFactorials2', number=5)
0.011401384996133856
>>> timeit.timeit(stmt='eratosthenes(maximum=1000)',setup='from eratosthenes import eratosthenes', number=5)
0.0021134779963176697
```
As you can see PrimeAndFactorials is >100 times worse than eratosthenes while PrimeAndFactorials is >5 times worse than eratosthenes.


