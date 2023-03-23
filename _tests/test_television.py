from pytest import mark

def test_television_turns_on(tv_brand):
    print(f"{tv_brand} turns on as expected")

@mark.skip
def test_browser_can_navigate_to_training_ground(browser):
    browser.get('http://idlewild.industries')

def test_television_turns_on_from_fixture(tv_brand_from_fixture):
    print(f"{tv_brand_from_fixture} turns on as expected")