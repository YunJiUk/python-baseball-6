import random

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
        if len(user_input) != 3 or not user_input.isdigit():
            return False

        # 숫자가 서로 다른지 확인
        if len(set(user_input)) != 3:
            return False

        return True
    
    check = is_valid_input(random_numbers)

    # 프로그램의 메인 로직을 여기에 구현

if __name__ == "__main__":
    # 프로그램이 직접 실행될 때만 main() 함수를 호출
    main()
