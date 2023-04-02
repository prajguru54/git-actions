from app.main import sum


def test_sum() -> None:
    assert sum(4, 5) == 9
