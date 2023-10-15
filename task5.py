from playwright.sync_api import sync_playwright

'''Implement action class'''


def perform_actions():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()

        page.goto('https://www.boredpanda.com/')

        # Hover over an element:
        hover_element = page.locator('.main-header-logo')
        hover_element.hover()
        page.wait_for_timeout(2000)  # wait for 2 seconds to observe the hover effect

        # Right-click on an element:
        right_click_element = page.locator('.main-header-logo')
        right_click_element.click(button='right')
        page.wait_for_timeout(2000)  # wait for 2 seconds to observe the right-click action

        # Double-click on an element:
        double_click_element = page.locator('.main-header-logo')
        double_click_element.dblclick()
        page.wait_for_timeout(2000)  # wait for 2 seconds to observe the double-click action

        browser.close()


perform_actions()
