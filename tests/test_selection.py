import pytest

from src.hybrid_ads_boolean import hybrid_ads_boolean
from src.weighted_median import weighted_median


# -----------------------------
# Hybrid ADS Tests
# -----------------------------

def test_median_basic():
    arr = [3, 1, 4, 2, 5]
    result = hybrid_ads_boolean(arr, Pmax=1, Pmin=1)

    assert result["median"] == 3


def test_pmax_basic():
    arr = [1, 2, 3, 4, 5]
    result = hybrid_ads_boolean(arr, Pmax=2, Pmin=1)

    # 2nd maximum of [1,2,3,4,5] is 4
    assert result["pmax"] == 4


def test_pmin_basic():
    arr = [1, 2, 3, 4, 5]
    result = hybrid_ads_boolean(arr, Pmax=1, Pmin=2)

    # 2nd minimum is 2
    assert result["pmin"] == 2


def test_duplicates():
    arr = [1, 2, 2, 3, 4]
    result = hybrid_ads_boolean(arr, Pmax=1, Pmin=1)

    assert result["median"] == 2


def test_empty_array():
    with pytest.raises(ValueError):
        hybrid_ads_boolean([], Pmax=1, Pmin=1)


# -----------------------------
# Weighted Median Tests
# -----------------------------

def test_weighted_median_basic():
    values = [1, 2, 3, 4]
    weights = [1, 1, 1, 1]

    assert weighted_median(values, weights) == 2


def test_weighted_median_weight_shift():
    values = [1, 2, 3, 4]
    weights = [1, 1, 10, 1]

    # heavy weight at 3
    assert weighted_median(values, weights) == 3


def test_weighted_invalid_lengths():
    with pytest.raises(ValueError):
        weighted_median([1, 2], [1])


def test_weighted_negative_weight():
    with pytest.raises(ValueError):
        weighted_median([1, 2], [1, -1])
