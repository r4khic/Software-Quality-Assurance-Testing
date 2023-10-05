from playwright.sync_api import sync_playwright

'''1)	Automate test case of search functionality '''''
def test_wikipedia_search():
    with sync_playwright() as p:
        # Launch a new browser instance
        browser = p.chromium.launch(headless=False)  # Set headless to True if you don't want to see the browser UI
        page = browser.new_page()

        # Navigate to Wikipedia
        page.goto("https://en.wikipedia.org/")

        # Find the search input, type "Python programming", and press Enter
        page.fill("input[name='search']", "Python programming")
        page.press("input[name='search']", "Enter")

        # Wait for the search results page to load and assert the title
        page.wait_for_selector("h1#firstHeading")
        assert page.text_content("h1#firstHeading") == "Python (programming language)"

        # Close the browser
        browser.close()


if __name__ == "__main__":
    test_wikipedia_search()
