from playwright.sync_api import sync_playwright

'''Book a flight using with at least one title checkpoint in web flight reservation system '''


def test_blazedemo_book_flight():
    with sync_playwright() as p:
        # Launch a new browser instance
        browser = p.chromium.launch(headless=False)  # Set headless to True if you don't want to see the browser UI
        page = browser.new_page()

        # Navigate to the BlazeDemo homepage
        page.goto("http://blazedemo.com")

        # Select a departure city and destination city
        page.select_option("select[name='fromPort']", "Boston")
        page.select_option("select[name='toPort']", "London")

        # Click the "Find Flights" button
        page.click("input[type='submit']")

        # Choose a flight from the search results
        page.click("input[type='submit']")

        # Provide passenger details
        page.fill("input[name='inputName']", "John Doe")
        page.fill("input[name='address']", "123 Main St")
        page.fill("input[name='city']", "Boston")
        page.fill("input[name='state']", "MA")
        page.fill("input[name='zipCode']", "02110")
        page.fill("input[name='creditCardNumber']", "4111111111111111")
        page.fill("input[name='creditCardMonth']", "12")
        page.fill("input[name='creditCardYear']", "2023")
        page.fill("input[name='nameOnCard']", "John Doe")

        # Confirm and purchase the flight
        page.click("input[type='submit']")

        # Verify the booking confirmation title
        assert page.text_content("h1") == "Thank you for your purchase today!"

        # Close the browser
        browser.close()


if __name__ == "__main__":
    test_blazedemo_book_flight()
