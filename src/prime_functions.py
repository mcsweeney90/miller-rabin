#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Prime number functions I've often found useful for coding challenges etc.
"""

import numpy as np
from math import sqrt, prod

def prime_factors(n):
    """
    Returns the prime factors of n.
    Fairly fast, although e.g., sympy.ntheory.factorint is about 3x faster.

    Parameters
    ----------
    n : INT
        Number to factorize.

    Returns
    -------
    factors : DICT
        Prime factors of n in form {p : multiplicity of p}.
    """
    # Check for input errors.
    if n < 0:
        raise ValueError("Number must be positive!")

    # If n is float of the form n.000... etc, then convert to int, else throw an error.
    if isinstance(n, float):
        i = int(n)
        if abs(n - i) < 1e-6:
            n = int(n)
        else:
            raise ValueError("Number must be an integer!")
            
    factors = {}
    while n > 1:
        temp = n
        while n % 2 == 0:
            n = n // 2
            try:
                factors[2] += 1
            except KeyError:
                factors[2] = 1
        for p in range(3, int(sqrt(n)) + 1, 2):
            while n % p == 0:
                n //= p
                try:
                    factors[p] += 1
                except KeyError:
                    factors[p] = 1
        if n == temp: # n is prime.
            factors[n] = 1
            n = 1
    return factors

def num_divisors(n):
    """
    Number of divisors of integer n.
    If n = p1^e1 * p2^e2 *... where p1, p2, ... are prime then the number of divisors is (e1 + 1) * (e2 + 1) *...

    Parameters
    ----------
    n : INT
        Number to compute divisor count for.

    Returns
    -------
    INT
        Number of divisors of n.
    """        
    return prod(e + 1 for e in prime_factors(n).values())

def proper_divisors(n):
    """
    Returns the proper divisors of n.

    Parameters
    ----------
    n : INT
        Number to get proper divisors of.

    Returns
    -------
    LIST
        Proper divisors of n.
    """
    # Check for input errors.
    if n <= 0:
        raise ValueError("Number must be positive!")

    # If n is float of the form n.000... etc, then convert to int, else throw an error.
    if isinstance(n, float):
        i = int(n)
        if abs(n - i) < 1e-6:
            n = int(n)
        else:
            raise ValueError("Number must be an integer!")
            
    divisors = [1]
    rt = sqrt(n)
    for i in range(2, int(rt) + 1):
        if n % i == 0:
            divisors.append(i)
            divisors.append(n//i)
    return divisors[:-1] if (n > 1 and rt % 1 == 0) else divisors

def get_primes(N):
    """
    Get all primes less than N (exclusive). 

    Parameters
    ----------
    N : INT
        Limit.

    Returns
    -------
    NDARRAY
        All of the primes < N.
    """
    # Check for input errors.
    if N <= 0:
        raise ValueError("Number must be positive!")
    elif N < 3:
        raise ValueError("There are no primes smaller than 2!")

    # If n is float of the form n.000... etc, then convert to int, else throw an error.
    if isinstance(N, float):
        i = int(N)
        if abs(N - i) < 1e-6:
            N = int(N)
        else:
            raise ValueError("Number must be an integer!")
            
    sieve = np.ones(N//2, dtype=bool)
    for p in range(3, int(sqrt(N)) + 1, 2):
        if sieve[p//2]:
            sieve[p*p//2::p] = False
    return np.r_[2, 2*np.nonzero(sieve)[0][1::]+1]

def get_primes_without_numpy(N):
    """
    Get all primes less than N. Non-numpy version.
    Still fairly fast but not as fast as the version above.

    Parameters
    ----------
    N : INT
        Limit.

    Returns
    -------
    LIST
        All of the primes < N.
    """
    # Check for input errors.
    if N <= 0:
        raise ValueError("Number must be positive!")
    elif N < 3:
        raise ValueError("There are no primes smaller than 2!")

    # If n is float of the form n.000... etc, then convert to int, else throw an error.
    if isinstance(N, float):
        i = int(N)
        if abs(N - i) < 1e-6:
            N = int(N)
        else:
            raise ValueError("Number must be an integer!")
            
    sieve = [True] * (N//2)
    for p in range(3, int(sqrt(N)) + 1, 2):
        if sieve[p//2]:
            sieve[p*p//2::p] = [False] * ((N-p*p-1)//(2*p)+1)
    return [2] + [2*p+1 for p in range(1, N//2) if sieve[p]]

def is_prime_trial(n):
    """
    Trial division primality check. Returns True if n is prime.
    Uses the fact that all primes other than 2 and 3 are of the form 6k +/- 1.
    Usually only ever used to show how impractical it is.

    Parameters
    ----------
    n : INT
        Possible prime.

    Returns
    -------
    BOOL
        True if prime, false otherwise.
    """
    # Check for input errors.
    if n < 0:
        raise ValueError("Number must be positive!")

    # If n is float of the form n.000... etc, then convert to int, else throw an error.
    if isinstance(n, float):
        i = int(n)
        if abs(n - i) < 1e-6:
            n = int(n)
        else:
            raise ValueError("Number must be an integer!")
            
    if n in {0, 1}:
        return False
    elif n in {2, 3}:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    a, b = 5, 2
    while a * a <= n:
        if n % a == 0:
            return False
        a += b
        b = 6 - b
    return True

def miller_rabin_classic(n):
    """
    Miller-Rabin primality test.
    Uses known deterministic set of witnesses for n < ~ 10^24. 

    Parameters
    ----------
    n : INT
        The number to check if prime.

    Returns
    -------
    BOOL
        True if prime, False otherwise.

    References
    ------------
    https://en.wikipedia.org/wiki/Miller%E2%80%93Rabin_primality_test
    http://rosettacode.org/wiki/Miller%E2%80%93Rabin_primality_test#Python
    https://oeis.org/A014233
    """

    def maybe_prime(a):
        """
        Returns True if n passes the witness test, with a as witness - i.e., n may be prime.
        Returns False if it fails the test and is definitely composite.
        """
        x = pow(a, d, n) # TODO: d defined in function body, not best practice.
        if x in {1, n - 1}:
            return True
        for _ in range(r - 1):
            x = (x * x) % n
            if x == n - 1:
                return True
        return False

    # Check for input errors.
    if n < 0:
        raise ValueError("Number must be positive!")

    # If n is float of the form n.000... etc, then convert to int, else throw an error.
    if isinstance(n, float):
        i = int(n)
        if abs(n - i) < 1e-6:
            n = int(n)
        else:
            raise ValueError("Number must be an integer!")

    # Handle n = 0 and n = 1 separately (loops forever otherwise).
    if n in {0, 1}:
        return False
    
    # Get all (25) primes less than 100.
    # TODO: pow in maybe_prime needs np.int64s from get_primes converted to ints. 
    primes = [int(p) for p in get_primes(100)]

    # Check against small set of known primes.
    if n in primes:
        return True
    if any((n % p) == 0 for p in primes):
        return False

    # n may be prime, so start algorithm proper.
    # Decompose n = 2**r * d + 1.
    d, r = n - 1, 1
    while d % 2 == 0:
        d //= 2
        r += 1        

    # Determine the witnesses to use.
    if n < 2047:
        witnesses = primes[:1] 
    elif n < 1373653:
        witnesses = primes[:2] 
    elif n < 25326001:
        witnesses = primes[:3] 
    elif n < 3215031751:
        witnesses = primes[:4] 
    elif n < 2152302898747:
        witnesses = primes[:5] 
    elif n < 3474749660383:
        witnesses = primes[:6] 
    elif n < 341550071728321:
        witnesses = primes[:7]   
    elif n < 3825123056546413051:
        witnesses = primes[:9]  
    elif n < 318665857834031151167461:
        witnesses = primes[:12]  
    elif n < 3317044064679887385961981:
        witnesses = primes[:13] 
    else:  # TODO: parameter specifying number of primes to use?
        witnesses = primes

    # Return True (i.e., probably prime) if all calls to maybe_prime are True, False otherwise.
    return all(maybe_prime(a) for a in witnesses)

def miller_rabin_minimal(n):
    """
    Miller-Rabin primality test with witness sets of minimal sizes.

    Parameters
    ----------
    n : INT
        The number to check if prime.

    Returns
    -------
    BOOL
        True if prime, False otherwise.

    References
    ------------
    http://miller-rabin.appspot.com/
    """

    def maybe_prime(a):
        """
        Returns True if n passes the witness test, with a as witness - i.e., n may be prime.
        Returns False if it fails the test and is definitely composite.
        """
        x = pow(a, d, n) # d defined in function body, not best practice.
        if x in {1, n - 1}:
            return True
        for _ in range(r - 1):
            x = (x * x) % n
            if x == n - 1:
                return True
        return False

    # Check for input errors.
    if n < 0:
        raise ValueError("Number must be positive!")

    # If n is float of the form n.000... etc, then convert to int, else throw an error.
    if isinstance(n, float):
        i = int(n)
        if abs(n - i) < 1e-6:
            n = int(n)
        else:
            raise ValueError("Number must be an integer!")

    # Handle n = 0 and n = 1 separately (loops forever otherwise).
    if n in {0, 1}:
        return False

    # Get all (25) primes less than 100.
    # TODO: pow in maybe_prime needs np.int64s from get_primes converted to ints. 
    primes = [int(p) for p in get_primes(100)]

    # Check against small set of known primes.
    if n in primes:
        return True
    if any((n % p) == 0 for p in primes):
        return False

    # n may be prime, so start algorithm proper.
    # Decompose n = 2**r * d + 1.
    d, r = n - 1, 1
    while d % 2 == 0:
        d //= 2
        r += 1

    # Determine the witnesses to use.
    if n < 341531: 
        witnesses = [9345883071009581737]
    elif n < 1050535501:
        witnesses = [336781006125, 9639812373923155]
    elif n < 350269456337:
        witnesses = [4230279247111683200, 14694767155120705706, 16641139526367750375]
    elif n < 55245642489451:
        witnesses = [2, 141889084524735, 1199124725622454117, 11096072698276303650]
    elif n < 7999252175582851:
        witnesses = [2, 4130806001517, 149795463772692060, 186635894390467037, 3967304179347715805]
    elif n < 585226005592931977:
        witnesses = [2, 123635709730000, 9233062284813009, 43835965440333360, 761179012939631437, 1263739024124850375]
    elif n < 18446744073709551616: # 2**64
        witnesses = [2, 325, 9375, 28178, 450775, 9780504, 1795265022]
    elif n < 3825123056546413051:
        witnesses = primes[:9]  
    elif n < 318665857834031151167461:
        witnesses = primes[:12]  
    elif n < 3317044064679887385961981:
        witnesses = primes[:13] 
    else:  # TODO: parameter specifying number of primes to use?
        witnesses = primes

    # Return True (i.e., probably prime) if all calls to maybe_prime are True, False otherwise.
    return all(maybe_prime(a) for a in witnesses)