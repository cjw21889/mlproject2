# -*- coding: UTF-8 -*-

# Import function to test
from mlproject2.distance import haversine, preprocessing, find_df
import pytest
import pandas as pd

def test_haversine():
    assert haversine(48.865070, 2.380009, 48.235070, 2.393409) == 70.00789153218594
    assert type(haversine(48.865070, 2.380009, 48.235070, 2.393409)) == float

def test_preprocessing():
    assert type(preprocessing('does this work')) == str

def test_df():
    x = [1,2,3,4]
    df = find_df(x)
    assert isinstance(df, pd.DataFrame) ==True
