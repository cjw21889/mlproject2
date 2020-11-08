# -*- coding: UTF-8 -*-

# Import function to test
from mlproject2.distance import haversine
import pytest

def test_haversine():
    assert haversine(48.865070, 2.380009, 48.235070, 2.393409) == 71.00789153218594
