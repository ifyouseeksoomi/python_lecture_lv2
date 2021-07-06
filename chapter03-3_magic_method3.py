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
