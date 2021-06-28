# Chapter 02-02

# chapter 2-2 : 클래스 상세 설명
# 클래스 변수 vs 인스턴스 변수
# 클래스 메소드 실습
# 네임스페이스

class Car:
    """
    Car class
    Author : Alex
    Date : 2021. 06
    """

    # 클래스 변수 (모든 인스턴스가 공유)
    car_count = 0

    def __init__(self, company, details):
        self._company = company
        self._details = details
        Car.car_count += 1

    def __str__(self):
        # return 'str: {} - {}'.format(self._company, self._details)
        return 'str: ' + f'{self._company} - {self._details}'

    def __repr__(self):
        return 'repr: ' + f'{self._company} - {self._details}'

    def __del__(self):
        Car.car_count -= 1

    def detail_info(self):
        print('Current ID : {}'.format(id(self)))
        print('Car Detail Info : {} {}'.format(
            self._company, self._details.get('price')))


car1 = Car('Ferrari', {'color': 'White', 'horsepower': 400, 'price': 8000})
car2 = Car('BMW', {'color': 'Black', 'horsepower': 270, 'price': 5000})
car3 = Car('Audi', {'color': 'Silver', 'horsepower': 300, 'price': 6000})
car4 = Car('Audi', {'color': 'Silver', 'horsepower': 300, 'price': 6000})

# print(car1)
# print(car2)
# print(car3)
# print(car4)

# print(id(car3))
# print(id(car4))

# print(car3._company is car4._company)
# print(car3 is car4)

#########################################################################################################

# self의 의미
# self를 맨 첫번째 인자(매개변수)로 받는다 : 인스턴스 메소드
# 같은 클래스에서 찍어낸 객체들은 각자 고유의 Id(주소값)을 가지게 되는데, 이 고유의 주소값들을 가지기 위해 필요한 것 : self

#########################################################################################################

# dir & __dict__ 확인
# print(dir(car1))  # ['__class__', '__delattr__', '__dict_dir(car1), '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', '_company', '_details']
# print(dir(car2))

# {'_company': 'Ferrari', '_details': {'color': 'White', 'horsepower': 400, 'price': 8000}}
# print(car1.__dict__)
# print(car2.__dict__)

# print(car1.__dir__)  # <built-in method __dir__ of Car object at 0x7fba2e93dfd0>
# print(car2.__dir__)

# dir
# : 한 오브젝트가 가지는 모든 애트리뷰트들(원래 가졌던것이든 새롭게 커스터마이징해서 들어간것이든)을 리스트형태로 보여주는 메소드
# : 부모객체로부터 상속받은 모든 것(속성)들을 다 보여줌 (해당 밸류는 보여주지 않음)

# __dict__
# : 불필요한 값을 제외하고, 실제로 클래스 작성 시 커스터마이징한 것들만 키밸류 형태로(딕셔너리 형태로) 보여주는 메소드
# : 부모 객체에서 상속받은 모든 속성들을 다 보여주지는 않으나 키 밸류 형태이므로 어떤 실제 밸류가 있는지까지 보여줌

#########################################################################################################

# Docstring
# print(car1.__doc__)
#
#     Car class
#     Author : Alex
#     Date : 2021. 06
#
# 내가 이 클래스에 대해서 개괄적으로 적어둔 주석이 출력됨 (협업에서 매우 중요하고도 자신감을 가질 수 있는 자세)

########################################################################################################

# Car class에 def detail_info(self)라는 인스턴스 메소드 하나 추가 후 진행
# car1.detail_info()
# car2.detail_info()

# 비교
# print(car1.__class__, car2.__class__)
# # id값 모두 동일함. 인스턴스 자체에 대한 주소값이 아니라 클래스 자체(빵틀)의 주소값을 물어보기 때문.
# print(id(car1.__class__), id(car2.__class__))

# 에러
# car1.detail_info()
# 얘는 문제 없음 (직접 인스턴스를 생성해서 호출하므로 self를 넘기지 않아도 매개변수가 자동으로 전달이 되는 형태)
# Car.detail_info(car1)
# 얘도 문제 없음 (클래스 이름으로 접근했을 때는 인자가 자동으로 전달되지는 않으므로 명시적으로 특정 인스턴스를 매개변수로 전달)
# Car.detail_info()
# 얘는 에러 : TypeError: detail_info() missing 1 required positional argument: 'self'

#########################################################################################################

# 위로 올라가서 클래스 내 클래스 변수 car_count 선언 후 다시 내려옴

# 클래스 변수의 공유성 확인하기

print(car1.__dict__)
# {'_company': 'Ferrari', '_details': {'color': 'White', 'horsepower': 400, 'price': 8000}}
# car_count 변수 보이지 않음 그러나!

print(car1.car_count)
# 0
# 선언한 car_count 값이 출력됨. 뭐지?
# 다시 클래스로 가서 __init__에 car_count를 1씩 증가하는 식 선언

print(car1.car_count)
# 4
# 내가 위에서 car1, car2, car3, car4 즉, Car 클래스를 가지고 인스턴스를 네 개 찍어냈다. 이때, 하나씩 찍어내질 때마다
# 클래스 변수는 +1되며 결국 마지막에 4가 되었고, 그 값을 출력한 것

# <핵심> 클래스 변수는 모든 인스턴스가 공유하는 값이다!
# 하나의 클래스에서 공통적으로 참조하는 변수를 할당할 때 클래스 변수를 사용
# ex. 학교 클래스를 만들 때 한 학생이 전입/전출할 때마다 student_count +=1, -=1로 선언해두면 총 학생수를 구하기 편할 것.

print(dir(car1))
# ['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', '_company', '_details', 'car_count', 'detail_info']
# 이 때는 car_count 변수가 나온다

# 클래스 변수에의 접근
print(car1.car_count)  # 4
print(Car.car_count)  # 4 (보다 정석)

# 정리
# 클래스 변수까지 확인할 때는 __dict__보다 dir를 쓰자
# +)
# 인스턴스 변수(ex. _company, _details)를 선언할 때에는 앞에 언더바를 붙이고,
# 클래스 변수(ex. car_count)를 선언할 때는 언더바를 붙이지 않는 것이 암묵적 룰(PEP 권장 사항)

#########################################################################################################

# 위에 Car 클래스로 올라가서 __del__ 선언 후 다시 내려옴

del car4

# 삭제 확인
print(car1.car_count)  # 3
print(Car.car_count)  # 3

#########################################################################################################

# 인스턴스 네임스페이스에 없으면 상위(클래스 변수단)에서 검색
# 즉, 동일한 이름으로 변수 생성 가능 (인스턴스 검색 후 -> 상위(클래스 변수(부모 변수)) 검색하기 떄문)

# 이게 무슨 말이냐면,
# __init__ 단에서 내가 car_count라는 변수를 만일 선언했다고 치면, (self.car_count =10)
# 한 객체에 대해서 car_count를 찍으면 10이 나올 것. 단,
# 클래스에 대해서 car_count를 찍으면 그냥 그대로 3이 나올 것

# 핵심 포인트
# 동일한 이름으로 변수는 웬만하면 생성하지 말고,
# 만일이라도 그런 일이 발생했다면 인스턴스 변수 --> 클래스 변수 이 순서로 찾는다는 사실
