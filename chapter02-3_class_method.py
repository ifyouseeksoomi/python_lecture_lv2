# Chapter 02-03

# chapter 2-3 : 파이썬 클래스 심화
# 클래스 기반 메소드 심화
# Class Method
# Instance Method
# Static Method


class Car:
    """
    Car class
    Author : Alex
    Date : 2021. 06
    Description : Class, Static, Instance Method
    """

    # 클래스 변수 (모든 인스턴스가 공유)
    price_per_raise = 1.0

    def __init__(self, company, details):
        self._company = company
        self._details = details

    def __str__(self):
        # return 'str: {} - {}'.format(self._company, self._details)
        return 'str: ' + f'{self._company} - {self._details}'

    def __repr__(self):
        return 'repr: ' + f'{self._company} - {self._details}'

    # Instance Method
    # self : 객체의 고유한 속성 값을 사용 ( == (self)가 붙으면 인스턴스 메소드다~ 라고 이해)

    def detail_info(self):
        print('Current ID : {}'.format(id(self)))
        print('Car Detail Info : {} {}'.format(
            self._company, self._details.get('price')))

    def get_price(self):
        return 'Before Car Price -> company : {}, price : {}'.format(self._company, self._details.get('price'))

    def get_price_calc(self):
        return 'After Car Price -> company : {}, price : {}'.format(self._company, self._details.get('price') * Car.price_per_raise)

    # Class Method
    @classmethod
    def raise_price(cls, per):
        # cls.price_per_raise == Car.price_per_raise
        if per <= 1:
            print('please enter 1 or more.')
            return
        cls.price_per_raise = per
        print('Price has been successfully increased.')

    # Static Method
    # 이 차가 BMW 생산인지 아닌지에 대한 것을 알아보는 메소드
    # 당연히 클래스 메소드로 선언할 수는 없음.
    # 물론 인스턴스 메소드로 선언할 수 있다. self로 받고 if문과 for문을 이용해서. 하지만 보다 전체적으로 아우를 수 있는 메소드를 만들고 싶을 때
    # Static method를 생각해볼 수 있겠다.
    @staticmethod
    def is_bmw(inst):  # inst == instance (이 인스턴스가 bmw니? 를 물어볼테니까 당연히 인스턴스는 전달이 되어야 한다)
        if inst._company == 'BMW':
            return 'OKAY : This car is made by BMW.'
        return 'Sorry. This car is made by {}'.format(inst._company)


# 인스턴스 생성
car1 = Car('Ferrari', {'color': 'White', 'horsepower': 400, 'price': 8000})
car2 = Car('BMW', {'color': 'Black', 'horsepower': 270, 'price': 5000})

# 인스턴스들의 전체 정보 확인
car1.detail_info()
car2.detail_info()

# 가격 정보 확인
print(car1._details.get('price'))  # 8000
print(car1._details['price'])  # 8000
# 그러나 이 방법(직접 인스턴스의 속성에 접근하는 방식)은 캡슐화에 어긋나기 때문에
# 파이썬 외의 언어에서 private등으로 선언하게 되면 접근이 어려울 수 있다 (권장 X)
# 이럴 때에 보통은, **인스턴스 메소드**를 만들어 내가 원하는 속성만 확인하는 방법을 사용한다.

#########################################################################################################

# 클래스로 올라가서 instance method인 get_price 작성 후 내려오기

print(car1.get_price)
# <bound method Car.get_price of repr: Ferrari - {'color': 'White', 'horsepower': 400, 'price': 8000}>
print(car1.get_price_calc)
# <bound method Car.get_price_calc of repr: Ferrari - {'color': 'White', 'horsepower': 400, 'price': 8000}>
print(car1.get_price())
# Before Car Price -> company : Ferrari, price : 8000
print(car1.get_price_calc())
# After Car Price -> company : Ferrari, price : 8000.0

Car.price_per_raise = 1.5
# 인상률 조정 (1.0 -> 1.5)

print(car1.get_price())
# Before Car Price -> company : Ferrari, price : 8000
print(car1.get_price_calc())
# After Car Price -> company : Ferrari, price : 12000.0

##########################################################################################################

# 그러나 변수 직접 접근은 좋지 않다고 했으니!
# 클래스 변수 역시 마찬가지이다. (75번째 줄에서 Car.price_per_raise = 1.5로 직접 수정하는 것 --> 별로)

# 다시 위의 클래스 올라가서 class method 선언하여 더욱 현명한 유지보수를 해보자

# 클래스 메소드
# @classmethod 로 데코레이터 선언
# 무조건 첫번째 인자로는 cls(클래스)를 받는다
# 클래스 변수에 대한 CRUD가 있다는 것을 단박에 눈치챌 수 있는 메소드

Car.raise_price(1)
# please enter 1 or more.
Car.raise_price(1.7)
# Price has been successfully increased.
print(car1.get_price())
# Before Car Price -> company : Ferrari, price : 8000
print(car1.get_price_calc())
# After Car Price -> company : Ferrari, price : 13600.0 (!!!!!!!!!!!!!!!!!!!!!!)

# 클래스 변수에 직접 접근하지 않고, 클래스 메소드를 이용하여 클래스 변수를 수정하면
# 캡슐화 원칙을 깨지 않을 수 있다는 점에서도 좋지만
# 실제로 메소드 속에 로직도 넣을 수 있다는 점 (방금처럼 인상률이 1을 초과할 때만 바꾼다든지하는 것들)이 참 좋다
# 클래스 안에 묶어서 세트화(?) 할 수 있다는 것 --> Pythonic

##########################################################################################################

# Static Method

# 인스턴스 메소드 : self를 받음
# 클래스 메소드 : cls를 받음
# 스태틱 메소드 : self도 cls도 안받음
# (뭐지??? --> 그냥 유연하게 써라 이 말임)

# 구글링을 해봐도 현재 개발자들끼리 이러한 스태틱 메소드에 대해 설전(이것의 필요성에 대해)이 있는 것을 확인할 수 있음
# <!!!!> class method vs. static method << 이런 글을 읽어볼 필요가 있다

# Car 객체가 10000개 나왔다고 치고,
# 이 차가 BMW에서 나왔는지를 알아보는 메소드를 만들어 보자

# 다시 클래스로 올라가서 스태틱 메소드를 작성해본다

# 스태틱 메소드를 인스턴스로 호출
print(car1.is_bmw(car1))
# Sorry. This car is made by Ferrari
print(car2.is_bmw(car2))
# OKAY : This car is made by BMW.

# <!!> 주의할 점
# 스태틱 메소드 선언 시 inst를 받기로 했었다. self로 넣지 않고 car1, car2로 넣어야함에 주의하자.

# 그리고 스태틱 메소드는 클래스 호출도 가능
print(Car.is_bmw(car1))
print(Car.is_bmw(car2))
# (근데 좀 당연히 될 것 같다)
# 바로 이런점을 유연하다고 본다

# 결국,
# 밖으로 빼서 단일 메소드화 시키기에는 조금 그렇고(클래스 자체와 연관성이 깊어서)
# 그렇다고 클래스 메소드로 선언할 수는 없고
# 인스턴스 메소드로 선언하자니 뭔가 멋이 없는 것도 같고 보다 포괄적으로 선언하고 싶을 때는 스태틱 메소드를 선언한다.
