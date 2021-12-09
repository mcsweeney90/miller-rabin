#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Miller-Rabin primality test.
"""

def composite_test(a, d, n, s):
    """Helper function for Miller_Rabin function below."""
    a_exp = pow(a, d, n)
    if a_exp == 1:
        return True
    for i in range(s - 1):
        if a_exp == n - 1:
            return True
        a_exp = (a_exp * a_exp) % n
    return a_exp == n - 1

def miller_rabin(n, known_primes=[2, 3, 5, 7, 11, 13, 17, 19]):
    """
    Miller-Rabin primality test.
    See: https://en.wikipedia.org/wiki/Miller%E2%80%93Rabin_primality_test
         http://rosettacode.org/wiki/Miller%E2%80%93Rabin_primality_test#Python
         http://miller-rabin.appspot.com/ for the best current bases
    """
    if n == 1:
        return False
    if n in known_primes:
        return True
    if any((n % p) == 0 for p in known_primes):
        return False
    d, s = n - 1, 1
    while d % 2 == 0:
        d //= 2
        s += 1
    if n < 2047:
        base = [2]
    elif n < 1373653:
        base = [2, 3]
    elif n < 9080191:
        base = [31, 73]
    elif n < 25326001:
        base = [2, 3, 5]
    elif n < 3215031751:
        base = [2, 3, 5, 7]
    elif n < 4759123141:
        base = [2, 7, 61]
    elif n < 1122004669633:
        base = [2, 13, 23, 1662803]
    elif n < 2152302898747:
        base = [2, 3, 5, 7, 11]
    elif n < 3474749660383:
        base = [2, 3, 5, 7, 11, 13]
    elif n < 341550071728321:
        base = [2, 3, 5, 7, 11, 13, 17]
    elif n < 3825123056546413051:
        base = [2, 3, 5, 7, 11, 13, 17, 19, 23]
    elif n < 318665857834031151167461:
        base = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37]
    elif n < 3317044064679887385961981:
        base = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41]    
    else: # TODO: probabilistic version.
        return False # TODO: probabilistic version.
    return all(composite_test(a, d, n, s) for a in base)