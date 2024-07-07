class N1:
    def test(self):
        print('N1')


class N2:
    def test(self):
        print('N2')


class A(N1, N2):
    def test(self):
        print('A')


class B(N2, N1):
    def test(self):
        print('B')


class C(A, B):
    def test(self):
        print('C')


c = C()

print(C.mro())
# C, A, N1, N2, B