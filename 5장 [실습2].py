import random

print("동전 던지기 게임 시작")
coin = random.randrange(2)
if coin == 0:
    print("앞면")
else:
    print("뒷면")
print("게임 종료")