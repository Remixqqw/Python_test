import math
from Kirill_SerializerAndFuncs.serializers_factory import SerializersFactory, SerializerType


def my_decor(meth):
    def inner(*args, **kwargs):
        print('I am in my_decor')
        return meth(*args, **kwargs)

    return inner


class A:
    x = 10

    @my_decor
    def my_sin(self, c):
        return math.sin(c * self.x)

    @staticmethod
    def stat():
        return 145

    def __str__(self):
        return 'AAAAA'

    def __repr__(self):
        return 'AAAAA'


class B:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    @property
    def prop(self):
        return self.a * self.b

    # @prop.setter
    # def prop(self,a):
    #     self.a = a

    @classmethod
    def class_meth(cls):
        return math.pi


class C(A, B):
    pass


ser = SerializersFactory.create_serializer(SerializerType.XML)

#C2 = type("C2", C.__bases__, {k : v for k, v in C.__dict__.items()})
# var = 15
# var_ser = ser.dumps(var)
# var_des = ser.loads(var_ser)
# print(var_des)
#print(C2.prop)
C_ser = ser.dumps(C)
C_des = ser.loads(C_ser)

c = C_des(1, 2)
c_ser = ser.dumps(c)
c_des = ser.loads(c_ser)

print(c_des)
print(c_des.x)
print(c_des.my_sin(10))
print(c_des.prop)
#c_des.prop = 3
#print(c_des.prop)
print(C_des.stat())
print(c_des.class_meth())



# f = C(1, 2)
# print(f.my_sin(11))





