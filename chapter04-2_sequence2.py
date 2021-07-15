# Chapter 04 Sequence

# 파이썬에의 객체 분류 1. 컨테이너 자료형 vs. 플랫 자료형
# 컨테이너 : 서로 다른 자료형을 담을 수 있는 경우 (list, tuple, collections.deque)
# 플랫 : 단일 자료형만 담을 수 있는 경우(str, bytes, bytearray, array.array, memoryview)
# (플랫의 경우 당연히 한 개의 자료형만 취급하므로 속도면에서 우위를 지님 --> 자연어 처리, 숫자, 이산에서 사용)

# 파이썬의 객체 분류 2. 가변형 vs. 불변형
# 가변(mutable) : list, bytearray, array.array, memoryview, collections.deque
# 불변(immutable) : tuple, string, bytes

####################################################################

# 튜플의 고급 사용
# mutable vs. immutable
# sort vs. sorted

####################################################################

# 고급 튜플
# Unpacking
# b, a = a, b (temp 필요 없이 이런 식의 할당이 바로 가능)

print(divmod(100, 9))
# (11, 1) : divmod함수는 두 개의 인자를 받아 그들을 나눈 몫과 나머지를 반환
print(divmod(*(100, 9)))
# (11, 1) : 아스타리스크 하나를 앞에 적어 튜플로 인자를 넣으면 전달된 인자를 언패킹하여 함수가 실행달
print(*(divmod(100, 9)))
# 11 1 : 아스타리스크를 아예 divmod 함수 앞에 붙여버리면 아예 결과값을 언패킹해버림

# 결론
# 아스타리스크는 언패킹의 기능을 하는구나

print()
print()

# 변수를 선언하여 할당하여 언패킹 심화 실습해보기

# x, y, *rest = range(10)
# ValueError: too many values to unpack (expected 3)
# 짐을 풀려하는데 너무 많은 값이 있어 --> range(10)의 개수가 x, y, rest 변수의 개수보다 넘 많아

# 반대로 이런 상황도 있음
# x, y, *rest = range(2)
# ValueError: not enough values to unpack (expected 3, got 2)
# 이번엔 반대로 짐풀려하는데 값이 적어 이런거임

# 이때 마지막 변수에 아스타리스크 하나 찍으면 상황이 해결된다

# print(x, y, rest)
# 위의 경우 : 0 1 [2, 3, 4, 5, 6, 7, 8, 9]
# 아래의 경우 : 0 1 []

# +) 이 때 순서는 랜덤이 아니고 지켜짐
# +) 맨 마지막에 아스타리스크를 안찍고, y나 x에 찍어도 작동 함
# --> *x, y, rest = range(10)으로 선언 시
# print 결과 : [0, 1, 2, 3, 4, 5, 6, 7] 8 9

####################################################################

# mutable(가변) vs. immutable(불변)

# tuple은 컨테이너형이자 불변형 (서로 다른 데이터 타입을 담을 수 있는 불변 객체)
# list는 컨테이너형이자 가변형 (서로 다른 데이터 타입을 담을 수 있는 가변 객체)

l = (15, 20, 25)
m = [15, 20, 25]

print(l, id(l))
# (15, 20, 25) 140214802314048

print(m, id(m))
# [15, 20, 25] 140214821657600

l = l * 2
m = m * 2

print(l, id(l))
# (15, 20, 25, 15, 20, 25) 140283497239264
print(m, id(m))
# [15, 20, 25, 15, 20, 25] 140283500240000

# 여기서 확인할 수 있는 것
# 튜플형으로 선언한 것도, 리스트로 선언한 것도 id값이 모두 바뀐다
# 재선언 과정 (l = l*2, m = m*2)에서 Id가 바뀌는 것
# 하지만 아래처럼 하면 어떨까

l *= 2
m *= 2

print(l, id(l))
# (15, 20, 25, 15, 20, 25, 15, 20, 25, 15, 20, 25) 140215506464624
print(m, id(m))
# [15, 20, 25, 15, 20, 25, 15, 20, 25, 15, 20, 25] 140215533640832

# 여기서 확인할 수 있는 것
# 튜플형으로 선언한 경우는 역시 이 때도 id값이 바뀐다 (불변형)
# 그러나 리스트형으로 선언한 것은 id값이 유지되는 것을 볼 수 있다

# '='는 '할당'이지만 *=의 경우는 '수정'으로 인식하는 것
# 연산자의 활용에 따라 그것을 재할당으로 볼 것인지, 수정으로 볼 것인지 달라질 수 있다

print()
print()

####################################################################

# sort vs. sorted
# reverse, key=len, key=str.lower (소문자 기준 정렬), key=func (내가 만든 함수 기준 정렬)

# sorted
# 정렬 후, 새로운 객체를 반환
# (원본 수정 X)

f_list = ['orange', 'apple', 'mango',
          'papaya', 'lemon', 'strawberry', 'coconut']

print('sorted - ', sorted(f_list))
# sorted -  ['apple', 'coconut', 'lemon', 'mango', 'orange', 'papaya', 'strawberry']
print(f_list)
# ['orange', 'apple', 'mango', 'papaya', 'lemon', 'strawberry', 'coconut']
# (sorted 이후 원본은 유지되는 것을 볼 수 있음)

print()
print()

print('sorted(reverse) - ', sorted(f_list, reverse=True))
# sorted(reverse) -  ['strawberry', 'papaya', 'orange', 'mango', 'lemon', 'coconut', 'apple']
print('sorted(key=len) - ', sorted(f_list, key=len))
# sorted(key=len) -  ['apple', 'mango', 'lemon', 'orange', 'papaya', 'coconut', 'strawberry']
print('sorted(lambda) - ', sorted(f_list, key=lambda x: x[-1]))
# sorted(lambda) -  ['papaya', 'orange', 'apple', 'lemon', 'mango', 'coconut', 'strawberry']
# (이건 각 element의 맨 마지막 글자의 알파벳 순서로 정렬된 것


# sort
# 정렬 후 객체 직접 변경
# (원본 수정 O!)
# --> 원본이 변경되어도 관계 없을 때 사용해야 한다

# sorted는 실객체 건드리는 것이 아니고 다른 뭔가를 뚝딱 만들어내는 방식이므로 반환값을 만들어내지만
# sort의 경우 실제로 객체(원본)를 변경하기 때문에 반환값이 없다

# 반환 값 확인 (None)
print('sort - ', f_list.sort())
# 호출 방법도 다르다. sorted의 경우와 달리 실제 대상을 직접 변경하겠다는 느낌을 물씬 담아 객체.sort()
# print 결과 : sort -  None

print(f_list)
# ['apple', 'coconut', 'lemon', 'mango', 'orange', 'papaya', 'strawberry']
# 실제로 f_list 자체, 즉 원본이 직접 변경되어버렸음을 확인할 수 있다.
# sort는 실제로 한번 실행할 때마다 원본이 계속 바뀐다.

print()
print()

print('sort(reverse) - ', f_list.sort(reverse=True), f_list)
# sort(reverse) -  None ['strawberry', 'papaya', 'orange', 'mango', 'lemon', 'coconut', 'apple']
print('sort(key=len) - ', f_list.sort(key=len), f_list)
# sort(key=len) -  None ['mango', 'lemon', 'apple', 'papaya', 'orange', 'coconut', 'strawberry']
print('sort(lambda) - ', f_list.sort(key=lambda x: x[-1]), f_list)
# sort(lambda) -  None ['papaya', 'apple', 'orange', 'lemon', 'mango', 'coconut', 'strawberry']


# 최종 정리
# List vs. Array 적합한 사용법은?
# 리스트 기반일 경우 -> List : 융통성(컨테이너 타입이므로), 다양한 자료형, 범용적 사용
# 숫자(int) 기반일 경우 -> Array : 배열(리스트와 거의 호환되긴 함)
