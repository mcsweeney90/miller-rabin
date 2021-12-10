#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Prime-related functions used for coding competitions etc. 
"""

import numpy as np
from math import sqrt, prod

def prime_factors(n):
    """
    Returns the prime factors of n. 
    Fairly fast, although sympy.ntheory.factorint is about 3x faster. 

    Parameters
    ----------
    n : INT
        Number to factorize.

    Returns
    -------
    factors : DICT
        Prime factors of n in form {p : multiplicity of p}.
    """
    # TODO: check valid input.
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
            if n % p == 0:                
                n //= p 
                try:
                    factors[p] += 1
                except KeyError:
                    factors[p] = 1
                break
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
    # TODO: check valid input.
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
    # TODO: check valid input.
    divisors = [1]
    rt = sqrt(n)
    for i in range(2, int(rt) + 1):
        if n % i == 0:
            divisors.append(i)
            divisors.append(n//i)  
    return divisors[:-1] if (n > 1 and rt % 1 == 0) else divisors

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
    # TODO: check valid input.
    if n == 1:
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

def get_primes(N):
    """
    Get all primes less than or equal to N. 

    Parameters
    ----------
    N : INT
        Limit.

    Returns
    -------
    NDARRAY
        All of the primes <= N.
    """
    # TODO: check valid input.
    sieve = np.ones(N//2, dtype=np.bool)
    for p in range(3, int(sqrt(N)) + 1, 2):
        if sieve[p//2]:
            sieve[p*p//2::p] = False
    return np.r_[2, 2*np.nonzero(sieve)[0][1::]+1]

def get_primes_without_numpy(N):
    """
    Get all primes less than or equal to N. Non-numpy version. 
    Still fairly fast but not as fast as the numpy version above.

    Parameters
    ----------
    N : INT
        Limit.

    Returns
    -------
    LIST
        All of the primes <= N.
    """
    # TODO: check valid input.
    sieve = [True] * (N//2)
    for p in range(3, int(sqrt(N)) + 1, 2):
        if sieve[p//2]:
            sieve[p*p//2::p] = [False] * ((N-p*p-1)//(2*p)+1)
    return [2] + [2*p+1 for p in range(1, N//2) if sieve[p]]

def miller_rabin(n, k=8, known_primes=None):
    """
    Miller-Rabin primality test.

    Parameters
    ----------
    n : INT
        The number to check if prime.
    k : INT
        Number of witnesses to use for probabilistic version.
    known_primes : ITERABLE, optional
        Small set of known primes to test against. The default is None.

    Returns
    -------
    BOOL
        True if prime, False otherwise.
        
    FURTHER INFO
    ------------
    https://en.wikipedia.org/wiki/Miller%E2%80%93Rabin_primality_test
    http://rosettacode.org/wiki/Miller%E2%80%93Rabin_primality_test#Python
    http://miller-rabin.appspot.com/ 
    """
    
    def maybe_prime(a):
        """
        Returns True if n passes the witness test, with a as witness - i.e., n may be prime. 
        Returns False if it fails the test and is definitely composite.  
        """
        x = pow(a, d, n)
        if x in {1, n - 1}:
            return True
        for _ in range(r - 1):
            x = (x * x) % n
            if x == n - 1:
                return True
        return False
    
    # Check for input errors.
    assert isinstance(n, int), "Number must be an integer!" # TODO: int conversion for e.g. n.0?
    assert n > 0, "Number must be greater than zero!"
            
    # Handle n = 1 separately (loops forever otherwise).
    if n == 1:
        return False
    
    # If known_primes not defined, use first 8 primes. 
    # TODO: compute first p primes for parameter p?     
    if known_primes is None:
        known_primes = {2, 3, 5, 7, 11, 13, 17, 19}
    
    # Check against small set of known primes.
    if n in known_primes:
        return True
    if any((n % p) == 0 for p in known_primes):
        return False
    
    # n may be prime, so start algorithm proper.
    # Decompose n = 2**r * d + 1.
    d, r = n - 1, 1
    while d % 2 == 0:
        d //= 2
        r += 1
    
    # Determine the witnesses to use. 
    # TODO: compare timings with optimal bases that can be found online.
    if n < 2047:
        witnesses = [2]
    elif n < 1373653:
        witnesses = [2, 3]
    elif n < 9080191:
        witnesses = [31, 73]
    elif n < 25326001:
        witnesses = [2, 3, 5]
    elif n < 3215031751:
        witnesses = [2, 3, 5, 7]
    elif n < 4759123141:
        witnesses = [2, 7, 61]
    elif n < 1122004669633:
        witnesses = [2, 13, 23, 1662803]
    elif n < 2152302898747:
        witnesses = [2, 3, 5, 7, 11]
    elif n < 3474749660383:
        witnesses = [2, 3, 5, 7, 11, 13]
    elif n < 341550071728321:
        witnesses = [2, 3, 5, 7, 11, 13, 17]
    elif n < 3825123056546413051:
        witnesses = [2, 3, 5, 7, 11, 13, 17, 19, 23]
    elif n < 318665857834031151167461:
        witnesses = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37]
    elif n < 3317044064679887385961981:
        witnesses = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41]    
    else: 
        witnesses = np.random.choice(range(2, n - 1), size=k)
        
    # Return True (i.e., probably prime) if all calls to maybe_prime are True, False otherwise.
    return all(maybe_prime(a) for a in witnesses)  

    
# =============================================================================
# Testing.
# =============================================================================

# N = 233 * 239
# print(miller_rabin(N))



        