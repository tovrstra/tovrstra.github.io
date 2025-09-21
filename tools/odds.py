#!/usr/bin/env python3
"""Calculate the probability of a hash collision."""


def hash_collision_probability(n: int, k: int) -> float:
    """Calculate the probability of a hash collision using the birthday paradox.

    Parameters
    ----------
    n
        Number of possible hash values.
    k
        Number of items to hash.

    Returns
    -------
    prob
        Probability of at least one collision.
    """
    if k > n:
        return 1.0
    fac = 1.0
    for i in range(k):
        fac *= (n - i) / n
    return 1.0 - fac


if __name__ == "__main__":
    n = 16**12  # Number of possible hash values
    k = 10000  # Number of items to hash
    prob = hash_collision_probability(n, k)
    print(f"Probability of at least one collision: {prob:.6e}")
