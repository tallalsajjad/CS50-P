import pytest
import working
def main():
    test_time()
    wrong_format()
    test_wrong_hour()
    test_wrong_minute()
def test_time():
    assert working.convert('9 AM to 5 PM') == '09:00 to 17:00'
    assert working.convert('10:30 PM to 8 AM') == '22:30 to 08:00'
def wrong_format():
    with pytest.raises(ValueError):
        working.convert('9 AM - 5 PM')
    with pytest.raises(ValueError):
        working.convert('09:00 AM - 17:00 PM')

def test_wrong_hour():
    with pytest.raises(ValueError):
        working.convert('015:00 AM - 17:00 PM')

def test_wrong_minute():
    with pytest.raises(ValueError):
        working.convert('9:60 AM to 5:60 PM')
    with pytest.raises(ValueError):
        working.convert('9:90 AM to 5:70 PM')

if __name__ == "__main__":
    main()

