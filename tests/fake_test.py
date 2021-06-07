def totally_real_method(a: int = 1):
    return a + 1

def test_not_real():
    assert 2 == totally_real_method()
    assert 2 != totally_real_method(a=2)
