from __future__ import absolute_import
import unittest
import axelrod
from axelrod.tests.property import *

from hypothesis import given, example
from hypothesis.strategies import integers, floats, random_module, assume


class TestMatch(unittest.TestCase):
    """
    Test that the composite method works
    """

    def test_call(self):
        match = matches().example()
        self.assertIsInstance(match, axelrod.Match)

    @given(match=matches(min_turns=10, max_turns=50, min_noise=0, max_noise=1))
    def test_decorator(self, match):
        self.assertIsInstance(match, axelrod.Match)
        self.assertGreaterEqual(len(match), 10)
        self.assertLessEqual(len(match), 50)
        self.assertGreaterEqual(match.noise, 0)
        self.assertLessEqual(match.noise, 1)

    @given(match=matches(min_turns=10, max_turns=50, min_noise=0, max_noise=0))
    def test_decorator_with_no_noise(self, match):
        self.assertIsInstance(match, axelrod.Match)
        self.assertGreaterEqual(len(match), 10)
        self.assertLessEqual(len(match), 50)
        self.assertEqual(match.noise, 0)


class TestTournament(unittest.TestCase):

    def test_call(self):
        tournament = tournaments().example()
        self.assertIsInstance(tournament, axelrod.Tournament)
