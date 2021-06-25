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
        return 'str : f'{self._company} - {self._details}'


car1 = Car('Ferrari', {'color': 'White', 'horsepower': 400, 'price': 8000})
print(car1)  # 스페셜 메소드 설정 전에는 매핑 주소가 나오지만, 클래스 내부에 스페셜 메소드 설정 시 str로 뜸
