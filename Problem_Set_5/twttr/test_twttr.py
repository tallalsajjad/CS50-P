from twttr import shorten

def main():
    test_lower_upper_case()
    test_numbers()
    test_puntuation()


def test_lower_upper_case():
    assert shorten("twitter") == 'twttr'
    assert shorten("PYTHON") == 'PYTHN'

def test_numbers():
    assert shorten("1245") == '1245'

def test_puntuation():
    assert shorten("!@#%") == '!@#%'

if __name__ == "__main__":
    main()
