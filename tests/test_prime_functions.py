#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Test functions in src/prime_functions.py.
"""

import pytest

# import sys
# sys.path.append('../src/') 
from src.prime_functions import miller_rabin

class TestMillerRabin(object):
    """
    Test miller_rabin function in miller_rabin.py. 
    """
    
    def test_negative_input(self):
        with pytest.raises(ValueError) as info:
            miller_rabin(n=-1)
        assert info.match("Number must be greater than zero!")
    
    def test_invalid_float_input(self):
        with pytest.raises(ValueError) as info:
            miller_rabin(n=7.1)
        assert info.match("Number must be an integer!")
    
    def test_valid_float_input(self):
        n = 13 + 1e-9
        expected = miller_rabin(13)
        actual = miller_rabin(n)
        assert actual == expected, f"miller_rabin({n}) returned {actual} instead of {expected}"
    
    def test_known_primes(self):
        expected = True
        actual = all(miller_rabin(p) for p in {2, 3, 5, 7, 11, 13, 17, 19})
        assert actual == expected, "miller_rabin returned False for a small known prime!"  # TODO: print which ones.
    
    def test_composites(self):
        expected = True
        composites = [233 * 239] # TODO: add known awkward composites.
        actual = not any(miller_rabin(c) for c in composites) 
        assert actual == expected, "miller_rabin returned True for a known composite!" # TODO: print which ones.
        
   
    