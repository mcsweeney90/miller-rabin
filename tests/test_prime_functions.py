#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Test functions in src/prime_functions.py.
"""

import pytest

# import sys
# sys.path.append('../src/') 
from prime_functions import miller_rabin

class TestMillerRabin(object):
    """
    Test miller_rabin function in miller_rabin.py. 
    """
    
    def test_negative_input(self):
        with pytest.raises(ValueError) as info:
            miller_rabin(n=-1)
        assert info.match("Number must be greater than zero!")
    
    def test_invalid_float_input(self):
        tests = [7.1, 7.01, 7 + 1e-3, 7 + 1e-4, 7 + 1e-5]
        for n in tests:
            with pytest.raises(ValueError) as info:
                miller_rabin(n)
            assert info.match("Number must be an integer!")
    
    def test_valid_float_input(self):
        n = 7 + 1e-10
        expected = miller_rabin(7)
        actual = miller_rabin(n)
        assert actual == expected, f"miller_rabin{n}) returned {actual} instead of {expected}"
    
    def test_primes(self):
        primes = {2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47,
                  53, 59, 61, 67, 71, 73, 79, 83, 89, 97, # All primes less than 100
                  877, 27644437, 35742549198872617291353508656626642567, 359334085968622831041960188598043661065388726959079837, # Bell primes
                  211, 2311, 200560490131, # Euclid primes
                  719, 5039, 39916801, 479001599, 87178291199, 10888869450418352160768000001, 265252859812191058636308479999999, 
                  263130836933693530167218012159999999, 8683317618811886495518194401279999999, # Factorial primes
                  257, 65537, # Fermat primes
                  233, 1597, 28657, 514229, 433494437, 2971215073, 99194853094755497, 
                  1066340417491710595814572169, 19134702400093278081449423917, # Fibonacci primes
                  113, 167, 269, 389, 419, 509, 659, 839, 1049, 1259, 1889, # Highly cototient primes
                  593, 32993, 2097593, 8589935681, 59604644783353249, 523347633027360537213687137, 
                  43143988327398957279342419750374600193, # Leyland primes 
                  127, 8191, 131071, 524287, 2147483647, 2305843009213693951, 618970019642690137449562111, 
                  162259276829213363391578010288127, 170141183460469231731687303715884105727, # Mersenne primes
                  1361, 2521008887, 16022236204009818131831320183, # Mills primes
                  239, 9369319, 63018038201, 489133282872437279, 19175002942688032928599, # Newman-Shanks-Williams primes
                  40487, 6692367337, # Non-generous primes
                  5741, 33461, 44560482149, 1746860020068409, 68480406462161287469, 13558774610046711780701, 
                  4125636888562548868221559797461449,  # Pell primes 
                  211, 2309, 2311, 30029, 200560490131, 304250263527209, 23768741896345550770650537601358309, # Primorial primes
                  1111111111111111111, 11111111111111111111111, # Repunit primes
                  683, 2731, 43691, 174763, 2796203, 715827883, 2932031007403, 768614336404564651, 
                  201487636602438195784363, 845100400152152934331135470251, 56713727820156410577229101238628035243, # Wagstaff
                  383, 32212254719, 2833419889721787128217599, 195845982777569926302400511, 4776913109852041418248056622882488319 # Woodall
                  }
        expected = True
        actual = all(miller_rabin(p) for p in primes)
        assert actual == expected, "miller_rabin returned False for a known prime!"  # TODO: print which ones.
    
    def test_composites(self):
        expected = True
        composites = [233 * 239] # TODO: strong pseudoprimes.
        actual = not any(miller_rabin(c) for c in composites) 
        assert actual == expected, "miller_rabin returned True for a known composite!" # TODO: print which ones.
        
   
    