# Chapter 04 Sequence

# 파이썬에의 객체 분류 1. 컨테이너 자료형 vs. 플랫 자료형
# 컨테이너 : 서로 다른 자료형을 담을 수 있는 경우 (list, tuple, collections.deque)
# 플랫 : 단일 자료형만 담을 수 있는 경우(str, bytes, bytearray, array.array, memoryview)
# (플랫의 경우 당연히 한 개의 자료형만 취급하므로 속도면에서 우위를 지님 --> 자연어 처리, 숫자, 이산에서 사용)

# 파이썬의 객체 분류 2. 가변형 vs. 불변형
# 가변(mutable) : list, bytearray, array.array, memoryview, collections.deque
# 불변(immutable) : tuple, string, bytes

####################################################################

# 해시 테이블
# 딕셔너리 생성의 고급 예제
# Setdefault 사용법

####################################################################

# 해시 테이블

# key에 value를 저장하는 구조
# 파이썬 언어 자체가 강력한 해시 테이블 엔진으로 구성
# 그렇기 때문에 딕셔너리 형태를 기본적인 데이터 형태로하여 매직메소드 __dir__등이 존재
# --> 파이썬 딕셔너리 타입 : 해시 테이블의 예

# 키 값의 연산 결과(해시값)에 따라 데이터 직접 접근이 가능한 구조
# 해싱 함수를 통해 나온 해시 주소를 기반으로 밸류의 위치를 알 수 있다 (참조)

# 솔직히 뭔말인지 알랑말랑하니 실제 코딩이 필요하다

# Dictionary 구조
# print(__builtins__.__dict__)
# 프린트해서 보면 키:밸류, 키:밸류 형식으로 쭈~욱 나옴
# 파이썬 엔진이 해시 테이블로 소개되어 있다는게 이 말이다

# 해시 값 확인
t1 = (10, 20, (30, 40, 50))
t2 = (10, 20, [30, 40, 50])

# print(hash(t1))
# 465510690262297113
# print(hash(t2))
# TypeError: unhashable type: 'list'

# 리스트가 포함된 튜플은 해시가 안된다(== hashable하지 않다)! 왜?
# hashable하다는 것은 결국, 객체가 생명주기 동안 결코 변경되지 않는 해시값을 가짐을 의미
# 그런데 리스트는 가변 객체이므로 값이 달라지면 hash value도 달라져야 함 --> hashable object의 정의에 어긋나므로 에러를 뱉는 것이다
# 해셔블하려면 기본 불변형 객체일 것

print()
print()

# Dict Setdefault 예제
source = (('k1', 'val1'),
          ('k1', 'val2'),
          ('k2', 'val3'),
          ('k2', 'val4'),
          ('k2', 'val5'))

# 이 source를 어떻게 딕셔너리 형으로 바꿀 수 있을까? (데이터 통합)
new_dict1 = {}
new_dict2 = {}


# Setdefault 사용 X (초보)
for k, v in source:
    if k in new_dict1:
        new_dict1[k].append(v)
    else:
        new_dict1[k] = [v]

print(new_dict1)
# {'k1': ['val1', 'val2'], 'k2': ['val3', 'val4', 'val5']}


# Setdefault 사용 (안초보)
for k, v in source:
    new_dict2.setdefault(k, []).append(v)

print(new_dict2)
# {'k1': ['val1', 'val2'], 'k2': ['val3', 'val4', 'val5']}
# (와 완전 빠르구나)


# 주의
new_dict3 = {k: v for k, v in source}
# 위와 같은 딕셔너리 컴프리헨션이 안되는 이유 : 나중값이 이전 값을 뒤집어써버림
print(new_dict3)
