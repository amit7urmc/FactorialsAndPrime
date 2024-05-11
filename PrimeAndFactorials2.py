class primeAndFactorials2:

    def __init__(self):
        self.largest_number_probed_for_prime = 3
        self.largest_known_prime = 3
        self.largest_known_slots = [[2, 3]]

    def enumerate_prime(self, verbose=True):
        newCandidate = self.largest_number_probed_for_prime + 1
        prime_found = False
        num_hits = 0
        num_skips = 0
        for eachSlot in self.largest_known_slots[0]:
            if newCandidate%eachSlot==0:
                self.largest_number_probed_for_prime = newCandidate
                currentLength = len(str(self.largest_known_prime))
                return currentLength
        for eachSlot in self.largest_known_slots[0]: 
            if newCandidate%eachSlot == (eachSlot-1):
                num_hits += 1
                if num_hits == 2:
                    prime_found = True
                    break
            if newCandidate%eachSlot:
                num_skips += 1
        if prime_found or num_skips==len(self.largest_known_slots[0]):
            self.largest_number_probed_for_prime = newCandidate
            self.largest_known_prime = newCandidate
            self.largest_known_slots[0].append(newCandidate)
            if verbose:
                print(f"Found a new prime: {newCandidate}")
        else:
            self.largest_number_probed_for_prime = newCandidate
        currentLength = len(str(self.largest_known_prime))
        return currentLength

    def find_next_prime(self, primeNumberLength=3, cutOffLargestPrimesRequired=100, byLength=True, verbose=False):
        currentLength = len(str(self.largest_known_prime))
        if byLength:
            while currentLength <= primeNumberLength:
                currentLength = self.enumerate_prime(verbose)
        else:
            currentCount = 1
            while currentCount <= cutOffLargestPrimesRequired:
                _ = self.enumerate_prime(verbose)   
                currentCount += 1 

    def get_all_primes(self):
        return self.largest_known_slots[0]

    def __str__(self):
        return str(self.largest_known_slots[0][-1])


if __name__ == "__main__":

    primeAndFactorials_obj_byLength = primeAndFactorials2()
    primeAndFactorials_obj_byLength.find_next_prime(primeNumberLength=3)
    print(primeAndFactorials_obj_byLength)
    print(primeAndFactorials_obj_byLength.get_all_primes())

    primeAndFactorials_obj_byNumberTimes = primeAndFactorials2()
    primeAndFactorials_obj_byNumberTimes.find_next_prime(cutOffLargestPrimesRequired=1000, byLength=False)
    print(primeAndFactorials_obj_byNumberTimes)
    print(primeAndFactorials_obj_byNumberTimes.get_all_primes())







