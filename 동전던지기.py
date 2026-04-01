import random as r

print("=== 🪙 동전 던지기 도박사 게임 시작 ===")

# 승패 기록을 위한 변수
win = 0
lose = 0

while True:
    print(f"\n현재 전적: {win}승 {lose}패")
    user_input = input("앞면(0) 또는 뒷면(1)을 예측하세요 (종료는 q): ")

    # 종료 조건 처리
    if user_input.lower() == 'q':
        break

    # 입력값이 0 또는 1인지 확인 (if-in 사용)
    if user_input not in ['0', '1']:
        print("❌ 0 또는 1만 입력해주세요!")
        continue

    # 동전 던지기 (0: 앞면, 1: 뒷면)
    user_guess = int(user_input)
    coin = r.randrange(2)
    
    # f-string을 이용한 결과 출력
    result_text = "앞면" if coin == 0 else "뒷면"
    print(f"결과: [ {result_text} ]")

    # 승패 판정
    if user_guess == coin:
        print("🎉 축하합니다! 예측 성공!")
        win += 1
    else:
        print("👻 꽝! 틀렸습니다.")
        lose += 1

print("-" * 30)
print(f"최종 결과: {win}승 {lose}패")
print("게임을 종료합니다. 감사합니다!")

