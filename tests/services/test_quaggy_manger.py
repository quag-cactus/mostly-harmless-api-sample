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
