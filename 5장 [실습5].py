#2개의 2자리 정수를 무작위로 생성하여 
# 덧셈,뺄셈,곱셈,나눗셈 문제를 내고 사용자의 입력값과 계산값을 비교하여 정답 오답 출력하기(if~else사용)

import random

num1 = random.randint(10, 99)
num2 = random.randint(10, 99)

s = ['+', '-', '*', '/']
n = random.choice(s)
if n == '+':
    result = num1 + num2
elif n == '-':
    result = num1 - num2
elif n == '*':
    result = num1 * num2
else:
    result = num1 / num2
user_input = float(input(f"{num1} {n} {num2} = ? "))
if user_input == result:
    print("정답")
else:
    print("오답")







