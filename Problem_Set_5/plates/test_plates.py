from plates import is_valid
def main():
      test_maximum_letter()

def test_maximum_letter():
    assert is_valid("AG") == True
    assert is_valid('a') == False

def test_first_two_alphabet():
    assert is_valid("12") == False
    assert is_valid("1") == False

def test_first_zero():
    assert is_valid("0") == False

def test_last_zero():
    assert is_valid("cs50") == True

def test_middle_alphabet():
    assert is_valid("AFB34A") == False

def test_ponctuation():
    assert is_valid("Bam.^n") == False
def test_number_placement():
     assert is_valid("ABA310") == True

def test_zero_placement():
     assert is_valid("cs05") == False



if __name__ == "__main__":
        main()

