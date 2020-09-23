import pytest


if __name__ == '__main__':
    pytest.main(["-sq","test/openpai/",'--alluredir=allure-results','--html=report/test.html'])