from playwright.sync_api import sync_playwright

'''2)	Create a test case for login and logout functionality'''
def test_github_login_logout():
    with sync_playwright() as p:
        # Launch a new browser instance
        browser = p.chromium.launch(headless=False)  # Set headless to True if you don't want to see the browser UI
        page = browser.new_page()

        # Navigate to GitHub's login page
        page.goto("https://github.com/login")

        # Enter valid username and password
        page.fill("input[name='login']", "your_github_username")
        page.fill("input[name='password']", "your_github_password")

        # Click the login button
        page.click("input[name='commit']")

        # Verify that the user is successfully logged in (e.g., by checking the presence of a profile icon)
        assert page.is_visible("img.avatar-user")

        # Click on the profile icon and then the logout button
        page.click("summary[aria-label='View profile and more']")
        page.click("button.dropdown-item.dropdown-signout")

        # Verify that the user is successfully logged out (e.g., by checking the presence of a login button)
        assert page.is_visible("a[href='/login']")

        # Close the browser
        browser.close()


if __name__ == "__main__":
    test_github_login_logout()
