# 터틀로 집 만들어보기
import turtle as t
t.shape("turtle")

size = int(input("집의 크기를 입력하세요: "))

t.left(60)
t.forward(size)
t.right(120)
t.forward(size)


t.right(30)
t.forward(size)
t.right(90)
t.forward(size)
t.right(90)
t.forward(size)
t.right(90)
t.forward(size)


t.done()

