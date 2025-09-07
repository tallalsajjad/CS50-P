import pytest
from datetime import date
from seasons import AgeInMinutes

def test_parse_date_valid():
    age = AgeInMinutes("2000-01-01")
    assert age.birth_date == date(2000, 1, 1)

def test_parse_date_invalid_format():
    with pytest.raises(SystemExit):
        AgeInMinutes("01-01-2000")

def test_parse_date_invalid_date():
    with pytest.raises(SystemExit):
        AgeInMinutes("2000-02-30")
