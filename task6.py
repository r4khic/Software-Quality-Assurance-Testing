from playwright.sync_api import sync_playwright
'''Implement select class '''


def interact_with_dropdown():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()

        page.goto('https://www.duckduckgo.com')  # Replace with the URL containing the dropdown

        # Selecting an option by its value:
        page.select_option("select#myDropdown", value="option2")

        # Selecting an option by its label (visible text):
        page.select_option("select#myDropdown", label="Option 3")

        # Selecting an option by its index:
        # Playwright doesn't directly support selection by index, so we'd use a workaround:
        index_to_select = 1  # 0-based index, so 1 means the second option
        options = page.query_selector_all("select#myDropdown > option")
        value_of_option = options[index_to_select].evaluate("option => option.value")
        page.select_option("select#myDropdown", value=value_of_option)

        browser.close()


interact_with_dropdown()
