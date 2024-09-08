import datetime

import pytest

from src.services import quaggy_manager


def test_check_quaggy_status(mocker):
    mock_class = mocker.patch("src.services.quaggy_manager.QuaggyWatcher")
    mock_class.return_value.check_status.return_value = "walking"
    result = quaggy_manager.check_quaggy_status(1)
    assert result == "Quaggy(ID: 1) is walking now."

    # 別のケースをテスト
    # mock_quaggy_manager.check_quaggy.return_value = False
    # result = mock_quaggy_manager.check_quaggy()
    # assert result == False


@pytest.mark.parametrize(
    "quaggy_id, now_time, origin_expected_behavior, expected_behavior",
    [
        (142, datetime.datetime.now(), "walk", "walk"),
        (
            142,
            datetime.datetime.now() + datetime.timedelta(hours=1),
            "free",
            "undesided",
        ),
        (142, datetime.datetime.now() + datetime.timedelta(hours=-1), "free", "free"),
        (142, datetime.datetime.now() + datetime.timedelta(hours=-1), None, None),
    ],
)
def test_get_quaggy_schedule(
    mocker, quaggy_id, now_time, origin_expected_behavior, expected_behavior
):

    mock_class = mocker.patch("src.services.quaggy_manager.QuaggyWatcher")
    mock_class.return_value.get_schedule.return_value = origin_expected_behavior

    behavior = quaggy_manager.get_quaggy_schedule(quaggy_id, now_time)
    assert behavior == expected_behavior
