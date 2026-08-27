import os
import tempfile

from code import (
    make_headings,
    make_row,
    make_data,
    make_file,
    build_me
)

def test_build_me():
    result = build_me()

    assert result is None
    
def test_make_headings():
    headings = make_headings()

    expected = ["transaction_id","timestamp","store_id","product_id","quantity","unit_price","total_amount","payment_method"]

    assert isinstance(headings, list)
    assert headings == expected
    assert len(headings) == 8
    
def test_make_row():
    row = make_row()

    assert isinstance(row, list)
    assert len(row) == 8

    assert isinstance(row[0], int)
    assert isinstance(row[1], str)
    assert isinstance(row[2], int)
    assert isinstance(row[3], int)
    assert isinstance(row[4], int)
    assert isinstance(row[5], float)
    assert isinstance(row[6], float)
    assert isinstance(row[7], str)

def test_make_data():
    data = make_data(5)

    assert isinstance(data, list)
    assert len(data) == 5

    for row in data:
        assert isinstance(row, list)
        assert len(row) == 8


def test_make_file():
    filename = tempfile.mktemp(suffix=".csv")

    headings = make_headings()
    data = make_data(3)

    result = make_file(filename, headings, data)

    assert result is True
    assert os.path.exists(filename)

    os.remove(filename)