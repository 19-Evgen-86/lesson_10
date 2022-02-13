from typing import Optional, List, Dict
from unittest import mock

import functions


@mock.patch("functions.data_request")
def test_data_request(mock_data_request):
    # при вызове data_request без параметров или и параметром типа str, результат должен быть список словарей
    # (все или часть объектов из json)
    # при вызове data_request с параметром int результатом должен быть словарь(один объект из json)
    mock_data_request.return_value = List[Dict]
    assert functions.data_request() == List[Dict]
    mock_data_request.return_value = Dict
    assert functions.data_request(int) == Dict
    mock_data_request.return_value = List[Dict]
    assert functions.data_request(str) == List[Dict]
