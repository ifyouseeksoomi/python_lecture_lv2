# Chapter 03 magic method (==special method)

# 파이썬의 핵심
# 시퀀스, 반복(iterator), 함수(functions), class
# 이것들을 잘해야 파이썬을 잘한다 << 소리를 들을 수 있다

# 매직 메소드란
# 클래스 안에 정의할 수 있는 특별한(built-in) 메소드
# 클래스를 enrich 할 수 있음
# 시작을 __ 로 하는 그 바로 그것들

# 파이썬 공식 문서에서 Data model 페이지를 꼼꼼히 읽을 것
# Low-level에서 코딩할 수 있는 것이 진짜 개발자가 되는 자질

# 기본형
print(int(10))  # 10
print(int)  # class 'int' --> 파이썬의 모든 타입은 다 객체(클래스)

# 모든 속성 및 메소드 출력 : dir()
print(dir(int))
print()
print(dir(float))  # 특이한 메소드가 몇개 보인다
print()

n = 10
print(n+100)
print(n.__add__(100))
# 둘은 결국 같은 기능이다
print()

print(n*100)
print(n.__mul__(100))
# 역시 둘은 같은 기능이다
print()

print(n.__doc__)  # int 클래스를 정의한 개발자가 써둔 주석
print()

print(n.__bool__(), bool(n))  # True True
# __bool__()은 실제 일어나는 내부적 호출, bool()은 클래스 생성자 타입의 호출
print()

# 정리
# 사람들이 파이썬이라는 언어를 개발하기 쉽게, 내부적으로 래핑을 해서 내부적으로 호출되는 언어를 직접 호출해서 쓸 수 있고
# 또한 int class 같은 것을 새롭게 구현하여 +를 썼지만 실제로 연산은 곱연산이 되는 나만의 클래스를 커스터마이징할 수도 있게 해주는 것이
# 매직 메소드(스페셜 메소드)의 기능

# 클래스 예제 1


class Fruit:
    def __init__(self, name, price):  # 매직 메소드인 __init__ 메소드는 생성자이므로 초기화가 필수
        self._name = name
        self._price = price

    def __str__(self):
        return 'Fruit Class Info : {} {}'.format(self._name, self._price)

    def __add__(self, x):
        return self._price + x._price

    def __sub__(self, x):
        return self._price - x._price

    def __le__(self, x):
        print("__le__ method")
        if self._price <= x._price:
            return True
        else:
            return False

    def __ge__(self, x):
        print("__ge__ method")
        if self._price >= x._price:
            return True
        else:
            return False


# 인스턴스 생성
s1 = Fruit('Orange', 7500)
s2 = Fruit('Banana', 3000)

# 위에서 __add__ 매직 메소드를 작성하지 않았다면
print(s1._price + s2._price)
# 와 같은 방식으로 과일 가격의 합을 구해야 했을 것이다.
# 그러나 이런 방식은 좋은 방법이 아니다. 가독성 떨어지고, 코드 양이 너무나 늘어난다.
print()

print(s1+s2)
# __add__ 매직 메소드 구현해두었기 때문에 알아서 가격을 더했다.
# 만일 이 마트에서 과일 한정 전부다 60% 세일을 한다 --> __add__ 리턴 시 전체 값에 * 0.6만 해주면 된다.
print()

print(s1-s2)
print()

print(s1 >= s2)
# __ge__ method
# True

print(s1 <= s2)
# __le__ method
# False

# __ge__와 __le__ 같은 메소드에서 self가 현재 s1인지 s2인지 알 수 있는데,
# 현재 s1이 self, 그리고 s2가 그 외 인자인 x로 받아들여지고 있음을 알 수 있다.
