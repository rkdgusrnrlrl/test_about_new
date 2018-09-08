class NewDontGiveInstance(object):
    def __init__(self):
        print("NewDontGiveInstance __init__ called")
        self.name = "hello"

    def __new__(cls):
        print("NewDontGiveInstance __new__ called")


class A(object):
    def __init__(self):
        print("A __init__ called")
        self.name = "hello"

    def __new__(cls):
        print("A __new__ called")
        return super().__new__(cls)


class B(A):
    def __init__(self):
        print("B __init__ called")
        super().__init__()

    def __new__(cls):
        print("B__new__ called")
        return super(B, cls).__new__(cls)


class C(A):
    def __init__(self):
        print("C __init__ called")
        super().__init__()

    def __new__(cls):
        print("C __new__ called")
        return super(C, cls).__new__(cls)


class D(B, C):
    def __init__(self):
        print("D __init__ called")
        super().__init__()

    def __new__(cls):
        print("D__new__ called")
        return super(D, cls).__new__(cls)


class Parent(object):
    def __init__(self, child_type):
        self.type = child_type

    def __new__(cls, child_type):
        if child_type == 'A': return super(Parent, cls).__new__(ChildA)
        if child_type == 'B': return super(Parent, cls).__new__(ChildB)
        return super().__new__()


class ChildA(Parent):
    pass


class ChildB(Parent):
    pass


#__new__ 메서드에서 super().__new__(아마 인스턴스를 넘겨주는듯) 를 넘겨 주지 않으면
def test_instace_should_be_none():
    a = NewDontGiveInstance()
    assert a is None


def test_how_call_new_order():
    D()


def test_Parent_factory():
    a = Parent('A')
    b = Parent('B')

    assert ChildA == type(a)
    assert ChildB == type(b)
