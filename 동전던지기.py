#동전을 던져서 앞 뒤 출력 random 함수 사용 r로
import random as r

print("동전 던지기 게임 시작")
coin = r.randrange(2)
if coin == 0:
    print("앞면")
else:
    print("뒷면")
print("게임 종료")


# firebass 예시 및 사용법

