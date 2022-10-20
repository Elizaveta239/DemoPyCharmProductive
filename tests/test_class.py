

def return_one_or_value(val):
    if val % 2 == 0:
        return val
    else:
        return 1


class TestValues:
    def test_value1(self):
        val = 1
        assert 1 == val

    def test_value2(self):
        assert return_one_or_value(10) == 10

    def test_value3(self):
        assert return_one_or_value(5) == 5

