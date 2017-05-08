from unittest.mock import Mock


class TestClass():
    pass

cls = TestClass()
cls.method = Mock(return_value="mocking is fun")
# print(cls.method())
# cls.method.assert_called_once_with()
cls.other_method = Mock(return_value="something else")
# print(cls.other_method.assert_not_called())