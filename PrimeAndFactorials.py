class primeAndFactorials:

    def __init__(self):
        self.largest_number_probed_for_prime = 2
        self.largest_known_prime = 2
        self.largest_known_slots = [['..'],['.']]

    def enumerate_prime(self, currentLength, verbose=True):
        not_a_prime = False
        for each_slot_index, each_slot in enumerate(self.largest_known_slots[0]):
            if len(self.largest_known_slots[1][each_slot_index]) == len(each_slot):
                not_a_prime = True
                self.largest_known_slots[1][each_slot_index] += "."
                continue
            quotient, remainder = divmod(len(self.largest_known_slots[1][each_slot_index]),len(each_slot))
            self.largest_known_slots[1][each_slot_index] = "."*(remainder+1)

        self.largest_number_probed_for_prime += 1
        if not not_a_prime:
            self.largest_known_prime = self.largest_number_probed_for_prime
            self.largest_known_slots[0].append("."*self.largest_known_prime)
            self.largest_known_slots[1].append(".")
            if verbose:
                print(f"Found a new prime number: {self.largest_known_prime}")
        currentLength = len(str(self.largest_known_prime))
        return currentLength

    def find_next_prime(self, primeNumberLength=3, cutOffLargestPrimesRequired=100, byLength=True, verbose=False):
        currentLength = len(str(self.largest_known_prime))
        if byLength:
            while currentLength <= primeNumberLength:
                currentLength = self.enumerate_prime(currentLength, verbose=verbose)
        else:
            currentCount = 1
            while currentCount <= cutOffLargestPrimesRequired:
                _ = self.enumerate_prime(currentLength, verbose=verbose)   
                currentCount += 1 

    def get_all_primes(self):
        primes = []
        for each_slot in self.largest_known_slots[0]:
            primes.append(len(each_slot))
        return primes

    def __str__(self):
        return str(len(self.largest_known_slots[0][-1]))


if __name__ == "__main__":

    primeAndFactorials_obj_byLength = primeAndFactorials()
    primeAndFactorials_obj_byLength.find_next_prime(primeNumberLength=2)
    print(primeAndFactorials_obj_byLength)
    print(primeAndFactorials_obj_byLength.get_all_primes())

    primeAndFactorials_obj_byNumberTimes = primeAndFactorials()
    primeAndFactorials_obj_byNumberTimes.find_next_prime(cutOffLargestPrimesRequired=100, byLength=False)
    print(primeAndFactorials_obj_byNumberTimes)
    print(primeAndFactorials_obj_byNumberTimes.get_all_primes())







