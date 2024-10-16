import random
import sys

def main():
    """
    프로그램의 진입점 함수.
    여기에서 전체 프로그램 로직을 시작합니다.
    """
    print("숫자 야구 게임을 시작합니다.")

    # 1부터 9까지의 숫자 중 서로 다른 3개의 숫자를 랜덤으로 선택
    random_numbers = random.sample(range(1, 10), 3)


    def is_valid_input(user_input):
        # 입력값이 3자리 숫자인지 확인
        if len(user_input) != 3 :
            return False

        # 숫자가 서로 다른지 확인
        if len(set(user_input)) != 3:
            return False

        return True
    
    print(random_numbers)
    

    try:
        check = is_valid_input(random_numbers)
        if check:
            print("유효한 입력입니다:", random_numbers)
    except ValueError as e:
        print(f"에러: {e}")
        sys.exit(1)  # 애플리케이션 종료

    def compare_numbers(user_input, computer_numbers):
        """사용자 입력과 컴퓨터 숫자를 비교하여 결과(스트라이크, 볼, 낫싱)를 반환"""
        strike = 0
        ball = 0

        # 스트라이크와 볼을 계산
        for i in range(3):
            if user_input[i] == computer_numbers[i]:
                strike += 1  # 같은 위치에 같은 숫자면 스트라이크
            elif user_input[i] in computer_numbers:
                ball += 1  # 다른 위치에 같은 숫자면 볼

        # 결과 출력
        if strike == 0 and ball == 0:
            return "낫싱"
        else:
            return f"{strike} 스트라이크, {ball} 볼"

    print("랜덤 숫자:", random_numbers)

    while True:
        # 사용자 입력 받기
        user_input = input("3자리 숫자를 입력하세요: ")

        try:
            # 입력값이 유효한지 확인
            is_valid_input(user_input)
            
            # 숫자 비교 후 결과 출력
            result = compare_numbers(user_input, list(map(str, random_numbers)))
            print(result)

            # 3 스트라이크면 게임 종료
            if result == "3 스트라이크, 0 볼":
                print("축하합니다! 숫자를 모두 맞추셨습니다.")
                break
        except ValueError as e:
            print(f"에러: {e}")
            sys.exit(1)  # 애플리케이션 종료


    # 프로그램의 메인 로직을 여기에 구현

if __name__ == "__main__":
    # 프로그램이 직접 실행될 때만 main() 함수를 호출
    main()
