#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Miller-Rabin primality test.
"""

import numpy as np

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

N = 233 * 239
print(miller_rabin(N))
        