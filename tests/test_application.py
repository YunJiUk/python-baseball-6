import pytest
from unittest.mock import patch
from baseball.main import main

# 게임 종료 후 재시작 테스트
def test_게임종료_후_재시작(capsys):
    # random.sample을 호출할 때 [1, 3, 5]와 [5, 8, 9]를 순차적으로 반환하도록 설정
    with patch('random.sample', side_effect=[[1, 3, 5], [5, 8, 9]]):
        입력값 = iter(["246", "135", "1", "597", "589", "2"])  # 사용자 입력값 설정

        # input 값을 미리 정의하고 테스트 중에는 sys.exit() 호출되지 않도록 patch
        with patch('builtins.input', side_effect=입력값), patch('sys.exit') as mock_exit:
            main()

        # 출력 결과를 캡처
        캡처된_출력 = capsys.readouterr().out

        # 결과 검증
        assert "낫싱" in 캡처된_출력  # 첫 번째 입력 246 -> 낫싱
        assert "3 스트라이크, 0 볼" in 캡처된_출력  # 두 번째 입력 135 -> 3 스트라이크
        assert "게임을 종료합니다." in 캡처된_출력  # 마지막에 "게임을 종료합니다."가 출력됨

# 예외 테스트
def test_예외_테스트():
    with pytest.raises(ValueError):  # ValueError 예외 발생 테스트
        # 입력값을 추가하여 StopIteration 방지
        입력값 = iter(["1234", "2"])  # 잘못된 입력과 종료 선택을 함께 제공
        with patch('builtins.input', side_effect=입력값), patch('sys.exit') as mock_exit:
            main()
