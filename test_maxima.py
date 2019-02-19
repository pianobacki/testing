import numpy as np
import pytest
from maxima import find_maxima

seed = 5
rand_state = np.random.RandomState(seed)

def test_maxima():
    testarr = np.random.randint(5, size = 10)
    testarr[3] = 10
    output = find_maxima(testarr)
    expected_result = 3
    assert expected_result in output
    