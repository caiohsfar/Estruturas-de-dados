class Node():
    def __init__(self, key):
        self._p = None
        self._right = None
        self._key = key
        self._left = None

    def get_key(self):
        return self._key

    def set_key(self, value):
        self._key = value

    def get_right(self):
        return self._right

    def set_right(self, value):
        self._right = value

    def get_left(self):
        return self._left

    def set_left(self, value):
        self._left = value

    def get_p(self):
        return self._p

    def set_p(self, value):
        self._p = value


class BST():
    def __init__(self):
        self.__root = None

    def get_root(self):
        return self.__root

    def set_root(self, valor):
        self.__root = valor

    def Inorder_Tree_Walk(self, x):  ##################
        if x != None:
            self.Inorder_Tree_Walk(x.get_right())
            print(x.get_key())
            self.Inorder_Tree_Walk(x.get_left())

    def Preorder_Tree_Walk(self, x):  ##################
        if x != None:
            print(x.get_key())
            self.Preorder_Tree_Walk(x.get_left())
            self.Preorder_Tree_Walk(x.get_right())

    def Postorder_Tree_Walk(self, x):  ##################
        if x != None:
            self.Postorder_Tree_Walk(x.get_left())
            self.Postorder_Tree_Walk(x.get_right())
            print(x.get_key())

    def Search(self, x, k):
        while x != None and k != x.get_key():
            if k < x.get_key():
                x = x.get_left()
            else:
                x = x.get_right()
        return x

    def Minimo(self, x):
        while x.get_left() != None:
            x = x.get_left()
        return x

    def print_min(self, x):
        return self.Minimo(x).get_key()

    def Maximo(self, x):
        while x.get_right() != None:
            x = x.get_right()
        return x

    def print_max(self, x):
        return self.Maximo(x).get_key()

    def Sucessor(self, x):
        x = self.Search(self.get_root(), x)
        if x.get_right() != None:
            return self.Minimo(x.get_right())
        else:
            y = x.get_p()
            while y != None and x == y.get_right():
                x = y
                y = y.get_p()
            return y

    def print_sucessor(self, x):
        return self.Sucessor(x).get_key()

    def Predecessor(self, x):
        x = self.Search(self.get_root(), x)
        if x.get_left() != None:
            return self.Maximo(x.get_left())
        else:
            y = x.get_p()
            while y != None and x == y.get_left():
                x = y
                y = y.get_p()
            return y

    def print_predecessor(self, x):
        return self.Predecessor(x).get_key()

    def Insert(self, dado):
        novo = Node(dado)
        y = None
        x = self.get_root()
        while x != None:
            y = x
            if novo.get_key() < x.get_key():
                x = x.get_left()
            else:
                x = x.get_right()
        novo.set_p(y)
        if y == None:
            self.set_root(novo)
        elif novo.get_key() < y.get_key():
            y.set_left(novo)
        else:
            y.set_right(novo)

    def Delete(self, z):
        z = self.Search(self.get_root(), z)
        if z.get_left() == None or z.get_right() == None:
            y = z
        else:
            y = self.Sucessor(z.get_key())
        if y.get_left() != None:
            x = y.get_left()
        else:
            x = y.get_right()
        if x != None:
            x.set_p(y.get_p())
        if y.get_p() == None:
            self.set_root(x)
        elif y == y.get_p().get_left():
            y.get_p().set_left(x)
        else:
            y.get_p().set_right(x)
        if y != z:
            z.set_key(y.get_key())
        return y


def Teste():
    a = BST()
    a.Insert(5)
    a.Insert(12)
    a.Insert(6)
    a.Insert(1)
    a.Insert(9)
    a.Inorder_Tree_Walk(a.get_root())
    print("#" * 50)
    a.Preorder_Tree_Walk(a.get_root())
    print("#" * 50)
    a.Postorder_Tree_Walk(a.get_root())
    print("#" * 50)

Teste()
