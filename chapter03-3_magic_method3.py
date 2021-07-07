# Chapter 03 magic method (==special method)

# 데이터 모델 설계
# Named Tuple 설명 (데이터 전처리)
# Model Unpacking
# Named Tuple 실습

# 객체 : 파이썬의 데이터를 추상화
# 모든 객체 : id, type으로 확인이 가능


# 일반적인 튜플을 이용하여 두 점 사이의 거리 구하기
from collections import namedtuple
from math import sqrt  # sqrt : 루트를 사용할 때 루트를 씌워주는 함수
pt1 = (1.0, 5.0)
pt2 = (2.5, 1.5)

l_leng1 = sqrt((pt1[0] - pt2[0])**2 + (pt1[1] - pt2[1])**2)
print(l_leng1)  # 3.8078865529319543


# 네임드 튜플을 사용한 두 점 사이의 거리 구하기
# 네임드 튜플 구글링
# : collections 모듈 하위의 클래스 / 딕셔너리처럼 K-V 매핑 형태 --> V에 K 혹은 인덱스 사용하여 접근 가능

# [1] 네임드 튜플 선언
# 선언 방식부터 클래스 형식으로 튜플을 추상화함
Point = namedtuple('Point', 'x y')
# 이 때 x y는 키에 해당하며
# 이 때의 1.0과 5.0은 각각의 x y에 매핑된 밸류에 해당하게 된다 / 혹은 인덱스 0은 1.0, 인덱스 1은 5.0의 접근도 가능

pt3 = Point(1.0, 5.0)
pt4 = Point(2.5, 1.5)

print(pt3)
# Point(x=1.0, y=5.0)
print(pt3[0])
# 인덱스로 접근해보기 : 1.0
print(pt3.x)
# key로 접근해보기 : 1.0
print(pt4)
# Point(x=2.5, y=1.5)


l_leng2 = sqrt((pt3.x - pt4.x)**2 + (pt3.y - pt4.y)**2)
print(l_leng2)  # 3.8078865529319543

# 일반 튜플과 네임드 튜플 모두 같은 결과를 보여주나
# 코딩의 흐름을 읽기에 네임드 튜플이 훨씬 더 유리하고 깔금함을 알 수 있다.
# 특히 지금은 값이 두 개밖에 없기에 인덱스 접근이 깔끔해보일 수 있으나 값의 개수가 늘어날수록 key로 접근하는 것이 유리하다는 것을 알 수 있을 것!

# 네임드 튜플 선언하는 네 가지 방법
Point1 = namedtuple('Point', ['x', 'y'])  # 리스트로 선언
Point2 = namedtuple('Point', 'x, y')  # 콤마
Point3 = namedtuple('Point', 'x y')  # 그냥
# <class '__main__.Point'>
Point4 = namedtuple('Point', 'x y x class', rename=True)
# rename = True옵냥이 들어가면서 예약어인 class를 사용할 수 있게 되었다 (rename의 default= False)

# 출력
print(Point1, Point2, Point3, Point4)

# dict to unpack
temp_dict = {'x': 75, 'y': 55}

# 객체 생성
p1 = Point1(x=10, y=35)
p2 = Point2(20, 40)
p3 = Point3(45, y=20)
p4 = Point4(10, 20, 30, 40)
p5 = Point3(**temp_dict)  # 네임드 튜플형식이 아닌 딕셔너리인 것을 kwargs로 넘겨도 파이썬이 알아서 이해한다


print()

# 객체 출력
print(p1)
print(p2)
print(p3)
print(p4)  # Point(x=10, y=20, _2=30, _3=40)
# x가 중복이기 때문에 스스로 난수를 만들어 _2를, rename True 옵션을 준 class는 _3으로 알아서 할당해둠
print(p5)  # Point(x=75, y=55)

# 사용
print(p1.x + p2.y)  # 인덱스 접근 말고 이런 키 접근!

# unpacking?
a, b = p5
print()
print(a, b)  # 75 55
print()

# 네임드 튜플 메소드
temp = [52, 38]

# _make() : 새로운 객체 생성 / 리스트를 기반(Point1참조)으로 네임드 튜플로 캐스팅을 함
p6 = Point1._make(temp)
print(p6)
print()

# _fields : 필드 네임 확인 / 키 값만 조회
print(p1._fields, p2._fields, p3._fields, p4._fields, p5._fields, p6._fields)
# ('x', 'y') ('x', 'y') ('x', 'y') ('x', 'y', '_2', '_3') ('x', 'y') ('x', 'y')
print()

# _asdict() : OrderedDict 반환
# 원래 딕셔너리는 정렬하지 않는데 정렬된 딕셔너리? --> 네임드 튜플을 딕셔너리로 반환하는 형태로 생각하면 된다
print(p1._asdict())  # {'x': 10, 'y': 35}
print(p4._asdict())  # {'x': 10, 'y': 20, '_2': 30, '_3': 40}
print(p6._asdict())  # {'x': 52, 'y': 38}
print()

# 네임드 튜플을 이용한 실 사용에 가까운 실습
# 한 학급에 20명의 학생, 총 4개의 반(A, B, C, D)

# 네임드 튜플 선언
Classes = namedtuple('Classes', ['group', 'number'])

# 그룹 리스트 선언
numbers = [str(n) for n in range(1, 21)]
groups = 'A B C D'.split()

print(numbers)
print(groups)
print()

# list comprehension을 사용하여 만들기
students = [Classes(group, number) for group in groups for number in numbers]
print(len(students))
print(students)
print()

# 가독성을 위한 추천
students2 = [Classes(group, number)
             for group in 'A B C D'.split()
             for number in [str(n)
                            for n in range(1, 21)]]
print(len(students2))  # == print(len(students))
print(students2)  # == print(students)
print()

# for문 돌려보기
for s in students:
    print(s)
