class Node():
    def __init__(self, key, cor):
        self._p = None
        self._right = None
        self._key = key
        self._left = None
        self._cor = cor

    def get_cor(self):
        return self._cor

    def set_cor(self, valor):
        self._cor = valor

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


class RBT():
    def __init__(self):
        self.__nil = Node(None, "BLACK")
        self.__nil.set_left(self.get_nil())
        self.__nil.set_right(self.get_nil())
        self.__root = self.get_nil()

    def get_root(self):
        return self.__root

    def set_root(self, valor):
        self.__root = valor

    def get_nil(self):
        return self.__nil

    def set_nil(self, valor):
        self.__nil = valor

    def Altura(self, x):
        if x == self.get_nil():
            return -1
        h1 = self.Altura(x.get_left())
        h2 = self.Altura(x.get_right())
        return (1 + max(h1, h2))

    def Inorder(self, x):  ##################
        if x != self.get_nil():
            self.Inorder(x.get_left())
            print(x.get_key())
            self.Inorder(x.get_right())

    def Preorder(self, x):  ##################
        if x != self.get_nil():
            print(x.get_key())
            self.Preorder(x.get_left())
            self.Preorder(x.get_right())

    def Postorder(self, x):  ##################
        if x != self.get_nil():
            self.Postorder(x.get_left())
            self.Postorder(x.get_right())
            print(x.get_key())

    def Search(self, x, k):
        while x != self.get_nil() and k != x.get_key():
            if k < x.get_key():
                x = x.get_left()
            else:
                x = x.get_right()
        return x

    def Minimo(self, x):
        while x.get_left() != self.get_nil():
            x = x.get_left()
        return x

    def Maximo(self, x):
        while x.get_right() != self.get_nil():
            x = x.get_right()
        return x

    def Sucessor(self, x):
        if x.get_right() != self.get_nil():
            return self.Minimo(x.get_right())
        else:
            y = x.get_p()
            while y != self.get_nil() and x == y.get_right():
                x = y
                y = y.get_p()
            return y

    def Predecessor(self, x):
        if x.get_left() != self.get_nil():
            return self.Maximo(x.get_left())
        else:
            y = x.get_p()
            while y != self.get_nil() and x == y.get_left():
                x = y
                y = y.get_p()
            return y

    def Insert_Fixup(self, z):
        while z.get_p().get_cor() == "RED":
            if z.get_p() == z.get_p().get_p().get_left():
                y = z.get_p().get_p().get_right()
                if y.get_cor() == "RED":
                    z.get_p().set_cor("BLACK")
                    y.set_cor("BLACK")
                    z.get_p().get_p().set_cor("RED")
                    z = z.get_p().get_p()
                else:
                    if z == z.get_p().get_right():
                        z = z.get_p()
                        self.Left_Rotate(z)
                    z.get_p().set_cor("BLACK")
                    z.get_p().get_p().set_cor("RED")
                    self.Right_Rotate(z.get_p().get_p())
            else:
                y = z.get_p().get_p().get_left()
                if y.get_cor() == "RED":
                    z.get_p().set_cor("BLACK")
                    y.set_cor("BLACK")
                    z.get_p().get_p().set_cor("RED")
                    z = z.get_p().get_p()
                else:
                    if z == z.get_p().get_left():
                        z = z.get_p()
                        self.Right_Rotate(z)
                    z.get_p().set_cor("BLACK")
                    z.get_p().get_p().set_cor("RED")
                    self.Left_Rotate(z.get_p().get_p())
        self.get_root().set_cor("BLACK")

    def Insert(self, dado):
        new = Node(dado, "RED")
        y = self.get_nil()
        x = self.get_root()
        while x != self.get_nil():
            y = x
            if new.get_key() < x.get_key():
                x = x.get_left()
            else:
                x = x.get_right()
        new.set_p(y)
        if y == self.get_nil():
            self.set_root(new)
        elif new.get_key() < y.get_key():
            y.set_left(new)
        else:
            y.set_right(new)
        new.set_right(self.get_nil())
        new.set_left(self.get_nil())
        new.set_cor("RED")
        self.Insert_Fixup(new)

    def Delete_Fixup(self, x):
        while x != self.get_root() and x.get_cor() == "BLACK":
            if x == x.get_p().get_left():
                w = x.get_p().get_right()
                if w.get_cor() == "RED":
                    w.set_cor("BLACK")
                    x.get_p().set_cor("RED")
                    self.Left_Rotate(x.get_p())
                    w = x.get_p().get_right()
                if w.get_left().get_cor() == "BLACK" and w.get_right().get_cor() == "BLACK":
                    w.set_cor("RED")
                    x = x.get_p()
                else:
                    if w.get_right() == "BLACK":
                        w.get_left().set_cor("BLACK")
                        w.set_cor("RED")
                        self.Right_Rotate(w)
                        w = x.get_p().get_right()
                        w.set_cor(x.get_p().get_cor())
                        x.get_p.set_cor("BLACK")
                        w.get_right().set_cor("BLACK")
                        self.Left_Rotate(x.get_p())
                        x = self.get_root()
            else:
                w = x.get_p().get_left()
                if w.get_cor() == "RED":
                    w.set_cor("BLACK")
                    x.get_p().set_cor("RED")
                    self.Right_Rotate(x.get_p())
                    w = x.get_p().get_left()
                if w.get_right().get_cor() == "BLACK" and w.get_left().get_cor() == "BLACK":
                    w.set_cor("RED")
                    x = x.get_p()
                else:
                    if w.get_left() == "BLACK":
                        w.get_right().set_cor("BLACK")
                        w.set_cor("RED")
                        self.Left_Rotate(w)
                        w = x.get_p().get_left()
                        w.set_cor(x.get_p().get_cor())
                        x.get_p.set_cor("BLACK")
                        w.get_left().set_cor("BLACK")
                        self.Right_Rotate(x.get_p())
                        x = self.get_root()
        x.set_cor("BLACK")

    def Delete(self, z):
        z = self.Search(self.get_root(), z)
        if z.get_left() == self.get_nil() or z.get_right() == self.get_nil():
            y = z
        else:
            y = self.Sucessor(z)
        if y.get_left() != self.get_nil():
            x = y.get_left()
        else:
            x = y.get_right()
        if x != self.get_nil():
            x.set_p(y.get_p())
        if y.get_p() == self.get_nil():
            self.set_root(x)
        elif y == y.get_p().get_left():
            y.get_p().set_left(x)
        else:
            y.get_p().set_right(x)
        if y != z:
            z.set_key(y.get_key())
        if y.get_cor() == "BLACK":
            self.Delete_Fixup(x)
        return y

    def Left_Rotate(self, x):
        y = x.get_right()  # define y
        x.set_right(y.get_left())  # transforma a subárvore à esquerda y na subárvore à direita de x
        y.get_left().set_p(x)
        y.set_p(x.get_p())
        if x.get_p() == self.get_nil():  # In the RBT "None" is T.get_None()
            y.get_left().set_p(x)
        y.set_p(x.get_p())  # liga o pai de x a y
        if x.get_p() == self.get_nil():
            self.set_root(y)
        elif x == x.get_p().get_left():
            x.get_p().set_left(y)
        else:
            x.get_p().set_right(y)
        y.set_left(x)  # Coloca x à esquerda de y
        x.set_p(y)

    def Right_Rotate(self, x):
        y = x.get_left()
        x.set_left(y.get_right())
        y.get_right().set_p(x)
        y.set_p(x.get_p())
        if x.get_p() == self.get_nil():
            y.get_right().set_p(x)
        y.set_p(x.get_p())
        if x.get_p() == self.get_nil():
            self.set_root(y)
        elif x == x.get_p().get_right():
            x.get_p().set_right(y)
        else:
            x.get_p().set_left(y)
        y.set_right(x)
        x.set_p(y)


a = RBT()
b = [2,4,76,32,65,8,324,9,54,312,7]
for i in b:
  a.Insert(i)
a.Delete(8)
a.Delete(2)
a.Delete(312)
print("inorder")
a.Inorder(a.get_root())
print("preorder")
a.Preorder(a.get_root())
print("posorder")
a.Postorder(a.get_root())
