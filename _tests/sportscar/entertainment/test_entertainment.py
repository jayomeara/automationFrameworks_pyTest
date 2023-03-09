from pytest import mark

@mark.ui
@mark.entertainment
def test_can_navigate_topage(chrome_browser):
        chrome_browser.get('http://motortrend.com/')
        assert True

@mark.entertainment
def test_entertainment_functions_as_expected():
        assert True