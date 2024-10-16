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


    # 프로그램의 메인 로직을 여기에 구현

if __name__ == "__main__":
    # 프로그램이 직접 실행될 때만 main() 함수를 호출
    main()
