def test(a, b):

    a.b = 1
    a.c = [10]
    b = "b"

    return b


class B:
    def __init__(self) -> None:
        self.b = 2
        self.c = [11, 12, 13]

    def b_sum(self):
        return


num = 1
b_instance = B()

test(b_instance, num)
print(b_instance.b)
print(b_instance.c)
print(num)
