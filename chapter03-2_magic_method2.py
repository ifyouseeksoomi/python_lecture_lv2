# Chapter 03 magic method (==special method)

# Special method
# 매직 메소드 심화
# 클래스 매직 메소드 실습

# 클래스 예제 2

# 벡터 (x, y) : 크기와 방향을 갖는 값 (문송한 이야기)
# (5, 2) + (4, 3) = (9, 5)
# (10, 3) * 5 = (50, 15)
# Max((5, 10)) = 10

# 위와 같은 벡터의 기능(?)을 매직 메소드를 이용해서 구현해보기

import haversine


class Vector(object):  # (object) 쓰지 않아도 되지만, 명시적으로 써도 가
    def __init__(self, *args):  # (self, x, y) 써도 좋지만 조금 더 세련된 방식으로 패킹을 해서 매개변수가 넘어오는 것으로 해보자
        '''
        Creating a vector 
        for example : v = Vector(5, 10)
        '''
        if len(args) == 0:  # if v = Vector() 처럼 생성하면 (참고: len(args)는 args로 넘겨지는 숫자의 개수에 해당함을 print로 확인했음)
            self._x, self._y = 0, 0  # 첫번째 0을 x에, 두번째 0은 y에 들어갈 것 : 이런 것도 언패킹에 해당
        else:
            self._x, self._y = args

    def __repr__(self):
        '''
        Returning the vertor's information
        '''
        return 'Vector(%r, %r)' % (self._x, self._y)

    def __add__(self, other):
        '''
        Returning the result of addition : self and the other
        '''
        return Vector(self._x + other._x, self._y + other._y)

    def __mul__(self, other):
        '''
        Returning the result of multiplication : self and the other
        '''
        return Vector(self._x * other._x, self._y * other._y)

    def __bool__(self):  # 좌표 평면 상에서 0, 0에 있는지 없는지를 확인하는 메소드
        '''
        Returning 'False' when it's on (0, 0)
        '''
        return bool(max(self._x, self._y))


# print(Vector.__doc__)
# class 바로 아래 ''' '''를 이용하여 doc을 만들 때

# print(Vector.__init__.__doc__)
# class 내 __init__ 메소드 내에 ''' '''를 이용하여 doc을 만들 때

# Vector 인스턴스 생성
v1 = Vector(5, 7)
v2 = Vector(23, 35)
v3 = Vector()

# Vector 인스턴스 출력
print(v1)
print(v2)
print(v3)
print()
print()

# 매직메소드 출력
print(v1.__init__.__doc__)
print(Vector.__repr__.__doc__)
print(v2.__add__.__doc__)
print(Vector.__mul__.__doc__)
print(v3.__bool__.__doc__)
print(v1+v2)
print(v1*v2)
print(bool(v1), bool(v2), bool(v3))  # True, True, False
