from src.services import quaggy_manager

def test_check_quaggy(mocker):
    mock_class = mocker.patch('src.services.quaggy_manager.QuaggyManager')
    mock_class.return_value.get_food.return_value = "grape"
    result = quaggy_manager.check_quaggy()
    assert result == "Quaggy is eating grape."

    # 別のケースをテスト
    #mock_quaggy_manager.check_quaggy.return_value = False
    #result = mock_quaggy_manager.check_quaggy()
    #assert result == False