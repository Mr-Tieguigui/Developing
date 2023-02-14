
import numpy as np
import pandas as pd

import pytest

from seaborn._core.rules import (
    VarType,
    variable_type,
    categorical_order,
)


def test_vartype_object():

    v = VarType("numeric")
    assert v == "numeric"
    assert v != "categorical"
    with pytest.raises(AssertionError):
        v == "number"
    with pytest.raises(AssertionError):
        VarType("date")


def test_variable_type():

    s = pd.Series([1., 2., 3.])
    assert variable_type(s) == "numeric"
    assert variable_type(s.astype(int)) == "numeric"
    assert variable_type(s.astype(object)) == "numeric"
    assert variable_type(s.to_numpy()) == "numeric"
    assert variable_type(s.to_list()) == "numeric"

    s = pd.Series([1, 2, 3, np.nan], dtype=object)
    assert variable_type(s) == "numeric"

    s = pd.Series([np.nan, np.nan])
    # s = pd.Series([pd.NA, pd.NA])
    assert variable_type(s) == "numeric"

    s = pd.Series(["1", "2", "3"])
    assert variable_type(s) == "categorical"
    assert variable_type(s.to_numpy()) == "categorical"
    assert variable_type(s.to_list()) == "categorical"

    s = pd.Series([True, False, False])
    assert variable_type(s) == "numeric"
    assert variable_type(s, boolean_type="categorical") == "categorical"
    s_cat = s.astype("category")
    assert variable_type(s_cat, boolean_type="categorical") == "categorical"
    assert variable_type(s_cat, boolean_type="numeric") == "categorical"

    s = pd.Series([pd.Timestamp(1), pd.Timestamp(2)])
    assert variable_type(s) == "datetime"
    assert variable_type(s.astype(object)) == "datetime"
    assert variable_type(s.to_numpy()) == "datetime"
    assert variable_type(s.to_list()) == "datetime"


def test_categorical_order():

    x = pd.Series(["a", "c", "c", "b", "a", "d"])
    y = pd.Series([3, 2, 5, 1, 4])
    order = ["a", "b", "c", "d"]

    out = categorical_order(x)
    assert out == ["a", "c", "b", "d"]

    out = categorical_order(x, order)
    assert out == order

    out = categorical_order(x, ["b", "a"])
    assert out == ["b", "a"]

    out = categorical_order(y)
    assert out == [1, 2, 3, 4, 5]

    out = categorical_order(pd.Series(y))
    assert out == [1, 2, 3, 4, 5]

    y_cat = pd.Series(pd.Categorical(y, y))
    out = categorical_order(y_cat)
    assert out == list(y)

    x = pd.Series(x).astype("category")
    out = categorical_order(x)
    assert out == list(x.cat.categories)

    out = categorical_order(x, ["b", "a"])
    assert out == ["b", "a"]

    x = pd.Series(["a", np.nan, "c", "c", "b", "a", "d"])
    out = categorical_order(x)
    assert out == ["a", "c", "b", "d"]
