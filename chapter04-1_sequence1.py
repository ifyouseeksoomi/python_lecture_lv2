# Chapter 04 Sequence

# 시퀀스 객체 : 시퀀스 자료형으로 만든 객체
# 요소 : 시퀀스 객체 내에 들어있는 각 값

# 순서가 있다 --> 인덱스 참조 가능
# 대표적으로 string, list, tuple, range (안 대표적으로는 bytes, bytearray)

# 가장 큰 특징 : 공통된 동작과 기능을 제공
# indexing, slicing, concatenation, repetition, in 연산자, len() 등

####################################################################

# 파이썬에의 객체 분류 1. 컨테이너 자료형 vs. 플랫 자료형
# 컨테이너 : 서로 다른 자료형을 담을 수 있는 경우 (list, tuple, collections.deque)
# 플랫 : 단일 자료형만 담을 수 있는 경우(str, bytes, bytearray, array.array, memoryview)
# (플랫의 경우 당연히 한 개의 자료형만 취급하므로 속도면에서 우위를 지님 --> 자연어 처리, 숫자, 이산에서 사용)

# 파이썬의 객체 분류 2. 가변형 vs. 불변형
# 가변(mutable) : list, bytearray, array.array, memoryview, collections.deque
# 불변(immutable) : tuple, string, bytes

# 이번 강의 목표 : 리스트 및 튜플 고급 이해

###################################################################

# Comprehending Lists (지능형 리스트 / 리스트 컴프리헨션)

import array
chars = '+_)(*&^%$#@!'
# chars[2] = 'h'
# TypeError: 'str' object does not support item assignment
# string의 경우 immutable이므로 불가능

code_list1 = []

for s in chars:
    # 유니코드 리스트
    code_list1.append(ord(s))

print(code_list1)  # [43, 95, 41, 40, 42, 38, 94, 37, 36, 35, 64, 33]
print()

# Comprehending Lists (리스트 컴프리헨션 사용)
code_list2 = [ord(s) for s in chars]
print(code_list2)  # [43, 95, 41, 40, 42, 38, 94, 37, 36, 35, 64, 33]
print()

# Comprehending Lists + map, filter (리스트 컴프리헨션에 맵과 필터 사용)
code_list3 = [ord(s) for s in chars if ord(s) > 40]
print(code_list3)  # [43, 95, 41, 42, 94, 64]
print()

code_list4 = list(filter(lambda x: x > 40, map(ord, chars)))
# filter() : 먼저 list로의 컨버팅 작업이 필요
# 인수는 첫번째로 익명함수 or 함수, 두번째로는 리스트와 같은 자료구조를 받음
print(code_list4)  # [43, 95, 41, 42, 94, 64]
print()

# ""ord()는 문자 -> 유니코드, chr()는 유니코드 -> 문자""" 확인을 위한 전체 출력
print(code_list1)
print(code_list2)
print(code_list3)
print(code_list4)
print([chr(s) for s in code_list1])
print([chr(s) for s in code_list2])
print([chr(s) for s in code_list3])
print([chr(s) for s in code_list4])
print()

# Generator 생성하기
# (플랫이자 가변형인 array를 사용해볼 것)

# (유레카) 제너레이터는 시퀀스 객체를 만들어주는 함수라고 말할 수 있다. (아 시퀀스!)
# local state를 유지(기억)해서, 다음번에 yield 해줘야 하는 값을 알고 있다
# == 메모리를 유지하지 않고, 한 번에 한 개의 항목을 생성
# 제너레이터는 파워풀한 이터레이터 중 하나

list_comprehension_ver = [ord(s) for s in chars]
print(list_comprehension_ver)
# [43, 95, 41, 40, 42, 38, 94, 37, 36, 35, 64, 33]

generator_ver = (ord(s) for s in chars)
print(generator_ver)
# <generator object <genexpr> at 0x7fd6807f5ac0>
# !!!! [] -> ()만 했을뿐인데, 생성해서 메모리에 얹지 않고 다음 yield를 기다리기만 한다
for s in generator_ver:
    print(s)
    # 확인: 기다렸다는듯 43부터 33까지 모두 하나씩 "yield"한 값을 프린트한다

array_ver = array.array('I', (ord(s) for s in chars))
print(array_ver)
# array('I', [43, 95, 41, 40, 42, 38, 94, 37, 36, 35, 64, 33])

print(type(array_ver))
# <class 'array.array'>

print(array_ver.tolist())  # array를 list로 컨버팅 해주는 함수
# [43, 95, 41, 40, 42, 38, 94, 37, 36, 35, 64, 33]
