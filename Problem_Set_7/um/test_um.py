from um import count

def main():
    ...

def test_simple_um():
    assert count("um") == 1

def test_um_with_syntax():
    assert count("Um, thanks for the album.") == 1
    assert count('Um?') == 1

def test_not_um():
    assert count('yummy') == 0
    assert count('ummer') == 0
    assert count('humm, umm umman') == 0
