from bank import value

def main():
    test_Hello()
    test_startswith_h()
    test_anyother_greeting()
    test_case_insensitivity()
    test_whitespace_handling()

def test_Hello():
    assert value("hello") == 0

def test_startswith_h():
    assert value("Hi Gi") == 20

def test_anyother_greeting():
    assert value("What's up Man") == 100

def test_case_insensitivity():
    assert value("hElLo") == 0

def test_whitespace_handling():
    assert value("  hello  ") == 0
    assert value("  Hi Gi  ") == 20
    assert value("  What's up Man  ") == 100

if __name__ == "__main__":
    main()
