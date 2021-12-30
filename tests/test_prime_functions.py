#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Test functions in src/prime_functions.py.
"""

import pytest

from prime_functions import prime_factors, num_divisors, proper_divisors, is_prime_trial, miller_rabin

class TestPrimeFactors(object):
    """
    Test prime_factors function. 
    """
    
    def test_negative_input(self):
        """
        Test function raises a ValueError for negative input. 
        """
        with pytest.raises(ValueError) as info:
            prime_factors(n=-1)
        assert info.match("Number must be positive!")
    
    def test_invalid_float_input(self):
        """
        Test function raises ValueErrors for float inputs that are not meant to represent integers. 
        """
        tests = [7.1, 7.01, 7 + 1e-3, 7 + 1e-4, 7 + 1e-5]
        for n in tests:
            with pytest.raises(ValueError) as info:
                prime_factors(n)
            assert info.match("Number must be an integer!")
    
    def test_valid_float_input(self):
        """
        Test function is valid for float input sufficiently close to integer values.  
        """
        n = 7 + 1e-10
        expected = prime_factors(7)
        actual = prime_factors(n)
        assert actual == expected, f"prime_factors({n}) returned {actual} instead of {expected}"
        
    def test_zero(self):
        """
        Test function returns empty dict for n = 0.  
        """
        actual = prime_factors(0)
        expected = {}
        assert actual == expected, f"prime_factors(0) returned {actual} instead of {expected}"
        
    def test_one(self):
        """
        Test function returns empty dict for n = 1.  
        """
        actual = prime_factors(1)
        expected = {}
        assert actual == expected, f"prime_factors(1) returned {actual} instead of {expected}"
        
class TestNumDivisors(object):
    """
    Test num_divisors function. 
    Input errors should be caught by prime_factors, so only need to check logic errors. 
    """    
          
    def test_zero(self):
        """
        Test function returns 1 for n = 0.  
        """
        actual = num_divisors(0)
        expected = 1
        assert actual == expected, f"num_divisors(0) returned {actual} instead of {expected}"
        
    def test_one(self):
        """
        Test function returns 1 for n = 1.  
        """
        actual = num_divisors(1)
        expected = 1
        assert actual == expected, f"num_divisors(1) returned {actual} instead of {expected}"
        
    def test_primes(self):
        """
        Test function returns 2 for primes.  
        """
        actual = tuple(num_divisors(p) for p in [2, 3, 5, 7, 11, 13, 17, 19])
        expected = tuple(2 for p in [2, 3, 5, 7, 11, 13, 17, 19])
        assert actual == expected, "num_divisors did not return 2 for a known prime!"
        
    def test_composites(self):
        """
        Test function returns correct number of divisors for some interesting composites.  
        """
        actual = tuple(num_divisors(n) for n in [4, 6, 8, 9, 10, 12, 14, 15, 16, 18])
        expected = tuple(3, 4, 4, 3, 4, 6, 4, 4, 5, 6)
        assert actual == expected, "num_divisors was incorrect for a small composite!"
        
class TestProperDivisors(object):
    """
    Test proper_divisors function. 
    """
    
    def test_negative_input(self):
        """
        Test function raises a ValueError for negative input. 
        """
        with pytest.raises(ValueError) as info:
            proper_divisors(n=-1)
        assert info.match("Number must be positive!")
    
    def test_invalid_float_input(self):
        """
        Test function raises ValueErrors for float inputs that are not meant to represent integers. 
        """
        tests = [7.1, 7.01, 7 + 1e-3, 7 + 1e-4, 7 + 1e-5]
        for n in tests:
            with pytest.raises(ValueError) as info:
                proper_divisors(n)
            assert info.match("Number must be an integer!")
    
    def test_valid_float_input(self):
        """
        Test function is valid for float input sufficiently close to integer values.  
        """
        n = 7 + 1e-10
        expected = proper_divisors(7)
        actual = proper_divisors(n)
        assert actual == expected, f"proper_divisors({n}) returned {actual} instead of {expected}"
        
class TestIsPrimeTrial(object):
    """
    Test is_prime_trial function. 
    """
    
    def test_negative_input(self):
        """
        Test function raises a ValueError for negative input. 
        """
        with pytest.raises(ValueError) as info:
            is_prime_trial(n=-1)
        assert info.match("Number must be positive!")
    
    def test_invalid_float_input(self):
        """
        Test function raises ValueErrors for float inputs that are not meant to represent integers. 
        """
        tests = [7.1, 7.01, 7 + 1e-3, 7 + 1e-4, 7 + 1e-5]
        for n in tests:
            with pytest.raises(ValueError) as info:
                is_prime_trial(n)
            assert info.match("Number must be an integer!")
    
    def test_valid_float_input(self):
        """
        Test function is valid for float input sufficiently close to integer values.  
        """
        n = 7 + 1e-10
        expected = is_prime_trial(7)
        actual = is_prime_trial(n)
        assert actual == expected, f"is_prime_trial({n}) returned {actual} instead of {expected}"

class TestMillerRabin(object):
    """
    Test miller_rabin function. 
    """
    
    def test_negative_input(self):
        """
        Test function raises a ValueError for negative input. 
        """
        with pytest.raises(ValueError) as info:
            miller_rabin(n=-1)
        assert info.match("Number must be positive!")
    
    def test_invalid_float_input(self):
        """
        Test function raises ValueErrors for float inputs that are not meant to represent integers. 
        """
        tests = [7.1, 7.01, 7 + 1e-3, 7 + 1e-4, 7 + 1e-5]
        for n in tests:
            with pytest.raises(ValueError) as info:
                miller_rabin(n)
            assert info.match("Number must be an integer!")
    
    def test_valid_float_input(self):
        """
        Test function is valid for float input sufficiently close to integer values.  
        """
        n = 7 + 1e-10
        expected = miller_rabin(7)
        actual = miller_rabin(n)
        assert actual == expected, f"miller_rabin{n}) returned {actual} instead of {expected}"
    
    def test_primes(self):
        """
        Ensure that miller_rabin returns True for known primes.
        Examples extracted from this relevant Wikipedia page: 
            https://en.wikipedia.org/wiki/List_of_prime_numbers
        """
        primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47,
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
                  ]
        actual = all(miller_rabin(p) for p in primes)
        expected = True
        assert actual == expected, "miller_rabin returned False for a known prime!"  # TODO: print which ones.
    
    def test_composites(self):
        """
        Ensure that miller_rabin returns False for notable composites. 
        See:
            https://en.wikipedia.org/wiki/Strong_pseudoprime
            http://www.s369624816.websitehome.co.uk/rgep/cartable.html (list of Carmichael numbers)
            https://math.dartmouth.edu/~carlp/PDF/paper25.pdf (strong pseudoprimes for bases 2, 3, and 5)
        """
        composites = [23**2, 233 * 239, # Simple composites 
                      561, 41041, 825265, 321197185, 5394826801, 232250619601, 9746347772161, 1436697831295441,
                      60977817398996785, 7156857700403137441, 1791562810662585767521, 87674969936234821377601,
                      6553130926752006031481761, 1590231231043178376951698401, 35237869211718889547310642241,
                      32809426840359564991177172754241, 2810864562635368426005268142616001, 
                      349407515342287435050603204719587201, # Carmichael numbers
                      25326001, 161304001, 960946321, 1157839381, 3215031751, 3697278427, 5764643587, 
                      6770862367, 14386156093, 15579919981, 18459366157, 19887974881, 21276028621, # Strong pseudoprimes for bases 2, 3, 5
                      3825123056546413051 # Strong pseudoprime for bases 2, 3, 5, 7, 11, 13, 17, 19, and 23 
                      ] 
        actual = not any(miller_rabin(c) for c in composites) 
        expected = True
        assert actual == expected, "miller_rabin returned True for a known composite!" # TODO: print which ones.
        
   
    