import pytest


if __name__ == '__main__':
    pytest.main(["-sq","test/openpai/test_get.py",'--alluredir=allure-results'])