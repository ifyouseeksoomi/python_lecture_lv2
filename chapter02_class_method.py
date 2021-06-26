# 클래스 기반 개발 설명

# 1) 절차 지향 vs. 객체 지향
# 2) 객체 지향 프로그래밍의 장점
# 3) 클래스 기반 코딩 실습


# Chapter 02-01

# OOP
# 장점: 코드 재사용, 코드 중복 방지, 유지보수 용이, 대형 프로젝트에 유리

# 과거 함수 중심 코딩의 문제 : 데이터 방대 -> 한 번 만든 이후 수정 어려움 -> 복잡
# 클래스 중심 코딩 : 데이터 중심 -> 모든 것이 객체로 관리

# Type 1. 일반적인 과거의 코딩 (끝없는 COPY&PASTE --> 유지 보수 용이하지 않고 드럽게 비효율적이)
# 차량 1
car_company = 'Ferrari'
car_detail_1 = [
    {'color': 'White'},
    {'horsepower': 400},
    {'price': 8000}
]

# 차량 2
car_company = 'BWM'
car_detail_1 = [
    {'color': 'Black'},
    {'horsepower': 270},
    {'price': 5000}
]

# 차량 3
car_company = 'Audi'
car_detail_1 = [
    {'color': 'Silver'},
    {'horsepower': 300},
    {'price': 6000}
]

# Type 2. 위의 C&P 방식을 조금 개선해보기 위한 리스트 구조
# 인덱스로 접근하기에 실수 방지가 어려우며 삭제도 불편, 전반적인 관리 불편 (데이터 양 늘어나면 더더욱)
car_company_list = ['Ferrari', 'Bmw', 'Audi']
car_detail_list = [
    {'color': 'White', 'horsepower': 400, 'price': 8000},
    {'color': 'Black', 'horsepower': 270, 'price': 5000},
    {'color': 'Silver', 'horsepower': 300, 'price': 6000}
]

# print(car_company_list)
# print(car_detail_list)

# BMW가 망하는 경우라면 이렇게 삭제하겠지
del car_company_list[1]
del car_detail_list[1]

# print(car_company_list)
# print(car_detail_list)

# Type 3. 딕셔너리 구조 (그나마 좀 나음)
# 코드 반복 지속, 키의 중첩 문제 발생 (딕셔너리에서 기본적으로 키 중복은 불가능한데)
# 아래 코드에서는 Nested dictionary 사용

car_dicts = [
    {'car_company': 'Ferrari', 'car_detail': {
        'color': 'White', 'horsepower': 400, 'price': 8000}},
    {'car_company': 'BMW', 'car_detail': {
        'color': 'Black', 'horsepower': 270, 'price': 5000}},
    {'car_company': 'Audi', 'car_detail': {
        'color': 'Silver', 'horsepower': 300, 'price': 6000}}
]

# print(car_dicts)
# del car_dicts[1]
# print(car_dicts)
# car_dicts.pop('car_company' == 'Ferrari')
# print(car_dicts)

# Type 4. 클래스 구조 (드디어)
# 구조 설계 후 재사용성 증가, 코드 반복 최소화, 메소드 활용


class Car:
    def __init__(self, company, details):
        self._company = company
        self._details = details

    def __str__(self):
        # return 'str: {} - {}'.format(self._company, self._details)
        return 'str: ' + f'{self._company} - {self._details}'

    def __repr__(self):
        return 'repr: ' + f'{self._company} - {self._details}'

    # 사실 str와 repr의 메소드는 역할이 비슷하다

    # 강사 말에 따르면,
    # __str__ : 비공식적으로(사용자 입장) 사용자 입장에서 string으로 print()를 사용할 때,
    # __repr__: 반대로 객체 그 자체를 그대로 보다 엄격히(개발자 입장) 보여주고 싶을 때


car1 = Car('Ferrari', {'color': 'White', 'horsepower': 400, 'price': 8000})
print(car1)
# 스페셜 메소드(__str__) 설정 전에는 매핑 주소가 나옴 클래스 내부에 스페셜 메소드 설정 시 str로 뜸
# __repr__ 설정 전에는 __str__이 나오지만 설정 후에는 __str__이 있어도 __repr__로 나옴

car2 = Car('BMW', {'color': 'Black', 'horsepower': 270, 'price': 5000})
car3 = Car('Audi', {'color': 'Silver', 'horsepower': 300, 'price': 6000})
print(car2)
print(car3)

# __dict__
print(car1.__dict__)
# 일반 속성으로 접근하는 것으로 해당 객체 안의 모든 속성을(속성명까지) 볼 수 있다 (str, repr와는 다름) - dictionary 형식이라 dict인듯

# dir
print(dir(car1))
# ['__class__', '__delattr__', '__dict__', '__dir__', '_doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', '_company', '_details']
# car1 객체의 모든 메타 정보가 보여짐
# 이때 보여지는 모든 메타 클래스는 전부다 파이썬에서 구현해 놓은 것으로 내가 굳이 클래스 내에 선언하지 않더라도 갖다 쓸 수가 있다

# 리스트 선언
car_list = []
car_list.append(car1)
car_list.append(car2)
car_list.append(car3)

print(car_list)

for x in car_list:
    # print(x) # str으로 나옴
    print(repr(x))  # repr로 나옴
