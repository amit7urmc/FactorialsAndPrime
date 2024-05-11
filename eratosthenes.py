def eratosthenes(maximum: int) -> list[int | None]:
    """
    https://stackoverflow.com/a/69936594/7480460 <-- Solution taken from here.
    Find all the prime numbers between 2 and `maximum`.

    Args:
        maximum: The maximum number to check.

    Returns:
        A list of primes between 2 and `maximum`.
    """

    if maximum < 2:
        return []

    # Discard even numbers by default.
    sequence = dict.fromkeys(range(3, maximum+1, 2), True)

    for num, is_prime in sequence.items():
        # Already filtered, let's skip it.
        if not is_prime:
            continue

        # Avoid marking the same number twice.
        for num2 in range(num ** 2, maximum+1, num):
            # Here, `num2` might contain an even number - skip it.
            if num2 in sequence:
                sequence[num2] = False

    # Re-add 2 as prime and filter out the composite numbers.
    return [2] + [num for num, is_prime in sequence.items() if is_prime]


if __name__ == "__main__":
    print(eratosthenes(maximum=1000))