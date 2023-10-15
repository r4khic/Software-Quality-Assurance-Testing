from playwright.sync_api import sync_playwright
from playwright.sync_api import Error

'''Implement implicit wait, explicit wait and fluent wait '''


def test_implicit_wait():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()

        # Set implicit wait
        page.set_default_timeout(5000)  # 5 seconds

        page.goto("https://www.reddit.com")

        try:
            sign_up_button = page.wait_for_selector(".signup-button")
            sign_up_button.click()
            print("Clicked the 'Sign Up' button.")
        except TimeoutError:
            print("The 'Sign Up' button was not found within the timeout")

        browser.close()


test_implicit_wait()


def test_explicit_wait():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()

        page.goto("https://www.reddit.com")

        try:
            sign_up_button = page.wait_for_selector(".signup-button", timeout=10000)
            sign_up_button.click()
            print("Clicked the 'Sign Up' button.")
        except TimeoutError:  # Use TimeoutError from playwright.sync_api
            print("The 'Sign Up' button was not found within the timeout.")

        browser.close()


test_explicit_wait()


def custom_condition(page):
    sign_up_button = page.query_selector(".signup-button")
    return sign_up_button is not None


def test_fluent_wait():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()

        page.goto("https://www.reddit.com")

        try:
            page.wait_for_function(lambda: custom_condition(page), timeout=10000)
            sign_up_button = page.query_selector(".signup-button")
            sign_up_button.click()
            print("Clicked the 'Sign Up' button.")
        except TimeoutError:
            print("The 'Sign Up' button was not found within the timeout.")

        browser.close()
test_fluent_wait()