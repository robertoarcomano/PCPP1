class A1:
    def test(self):
        print('A1')


class A2:
    def test(self):
        print('A2')


class A(A1, A2):
    def test(self):
        print('A')


class B1:
    def test(self):
        print('B1')


class B2:
    def test(self):
        print('B2')


class B(B1, B2):
    def test(self):
        print('B')


class C(A, B):
    def test(self):
        print('C')


c = C()

print(C.mro())
# C, A, A1, A2, B, B1, B2