import random
import sys

def main():
    """
    프로그램의 진입점 함수.
    여기에서 전체 프로그램 로직을 시작합니다.
    """
    print("숫자 야구 게임을 시작합니다.")

    def play_game():
        # 1부터 9까지의 숫자 중 서로 다른 3개의 숫자를 랜덤으로 선택
        random_numbers = random.sample(range(1, 10), 3)

        def is_valid_input(user_input):
            # 입력값이 3자리 숫자인지 확인
            if len(user_input) != 3 or not user_input.isdigit():
                raise ValueError("입력은 3자리 숫자여야 합니다.")
            
            # 숫자가 서로 다른지 확인
            if len(set(user_input)) != 3:
                raise ValueError("입력 값의 각 자리는 서로 달라야 합니다.")
            
            return True

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
    
    while True:
        play_game()  # 게임 한 번 실행
        
        # 게임 종료 후 재시작 또는 완전 종료 선택
        while True:
            choice = input("게임을 다시 시작하려면 1, 완전히 종료하려면 2를 입력하세요: ")
            if choice == '1':
                print("게임을 다시 시작합니다.")
                break  # 게임을 다시 시작 (play_game 호출)
            elif choice == '2':
                print("게임을 종료합니다.")
                sys.exit(0)  # 프로그램 완전 종료
            else:
                print("잘못된 입력입니다. 1 또는 2를 입력하세요.")

if __name__ == "__main__":
    # 프로그램이 직접 실행될 때만 main() 함수를 호출
    main()
