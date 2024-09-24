from selene import browser, be, have


def test_successful_search(driver):
    browser.element('[name="q"]').should(be.blank).type('yashaka/selene').press_enter()
    browser.element('[id="search"]').should(have.text('User-oriented Web UI browser tests in Python'))


def test_unsuccessful_search(driver):
    text_example = 'f9u8-h294,.hu294u24-dud9-k2d1'
    browser.element('[name="q"]').should(be.blank).type(text_example).press_enter()
    browser.element('.card-section').should(have.text('did not match any documents'))
