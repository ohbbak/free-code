import turtle as t

t.shape("turtle")
size = int(input("집의 크기를 입력하세요: "))

# 지붕 (삼각형)
t.left(60)
t.forward(size)
t.right(120)
t.forward(size)
t.right(30)

# 몸체 (사각형) - 반복문 적용!
for i in range(4):
    t.forward(size)
    t.right(90)

t.done()

