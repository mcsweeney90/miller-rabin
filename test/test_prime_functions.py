#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Test functions in src/prime_functions.py.
"""

import pytest

import sys
sys.path.append('../src/') 
from prime_functions import miller_rabin

class TestMillerRabin(object):
    """
    Test miller_rabin function in miller_rabin.py. 
    """
    
    def test_known_primes(self):
        expected = True
        actual = all(miller_rabin(p) for p in {2, 3, 5, 7, 11, 13, 17, 19})
        assert actual == expected, "Those are all known primes!"
        
    def test_known_composites(self):
        expected = True
        actual = not any(miller_rabin(c) for c in range(4, 101, 2)) 
        assert actual == expected, "Those are all known composites!"
    
    def test_awkward_composites(self):
        expected = True
        composites = [233 * 239] # TODO: add others.
        actual = not any(miller_rabin(c) for c in composites) 
        assert actual == expected, "Those are all known (awkward) composites!"
        
    # def test_negative_input(self):
    #     TODO.
    
    # def test_zero_input(self):
    #     TODO.
    
    # def test_float_input(self):
    #     TODO.
    