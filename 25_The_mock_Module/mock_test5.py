import test5

from unittest.mock import patch


@patch("urllib.request.urlopen")
def dummy_reader(mock_obj):
    result = test5.read_webpage("https://www.google.com")
    mock_obj.assert_called_with("https://www.google.com")
    print(result)


if __name__ == '__main__':
    dummy_reader()