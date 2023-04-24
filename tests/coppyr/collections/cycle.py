# -*- coding: utf-8 -*-
from coppyr.collections import cycle

from tests.base import BaseTestCase


class CycleTestCase(BaseTestCase):
    def test_basic(self):
        test_cycle = cycle(5)

        # check the basic first 5
        for i in range(5):
            assert next(test_cycle) == i

        # check that it starts over
        assert next(test_cycle) == 0

    def test_two_cycles(self):
        test_cycle = cycle(5)

        for i in range(5):
            assert next(test_cycle) == i

        for i in range(5):
            assert next(test_cycle) == i

    def test_different_start(self):
        test_cycle = cycle(5,10)

        for i in range(5,10):
            assert next(test_cycle) == i

    def test_different_step(self):
        test_cycle = cycle(0,10,2)

        for i in range(0,10,2):
            assert next(test_cycle) == i
