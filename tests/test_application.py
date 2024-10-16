import pytest
from unittest.mock import patch
from baseball.main import main


# 게임 종료 후 재시작 테스트
def test_게임종료_후_재시작(capsys):
    with patch('random.sample', side_effect=[[1, 3, 5], [5, 8, 9]]):
        # 입력값 모의 처리
        입력값 = iter(["246", "135", "1", "597", "589", "2"])
        with patch('builtins.input', side_effect=입력값):
            main()

        # 출력값 캡처
        캡처된_출력 = capsys.readouterr().out
        assert "낫싱" in 캡처된_출력
        assert "3스트라이크" in 캡처된_출력
        assert "1볼 1스트라이크" in 캡처된_출력
        assert "게임 종료" in 캡처된_출력


# 예외 테스트
def test_예외_테스트():
    with pytest.raises(ValueError):
        입력값 = iter(["1234"])  # 잘못된 입력 처리
        with patch('builtins.input', side_effect=입력값):
            main()

