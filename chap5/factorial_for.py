# 반복문으로 팩토리얼 구하기

# 함수 선언
def factorial(n):
    # 변수 선언
    output = 1
    # 반복문을 돌려 숫자를 더합니다.
    for i in range(1, n+1):
        output *= i
        # 리턴
    return output

# 함수 호출
print ("1!:", factorial(1))
print ("2!:", factorial(2))
print ("3!:", factorial(3))
print ("4!:", factorial(4))
print ("5!:", factorial(5))