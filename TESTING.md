# Functional Testing

## Authentication

Description:

Ensure a user can register on the store.

Steps:

1. Navigate to [Ethical Gearz](https://ci-p5-egz.herokuapp.com/) and click Register
2. Enter email, username and password
3. Click Register

Expected:

The user is directed to a verify email messagen after entering suitable email, username and password, registration is successful after verifying email.

Actual:

The user was directed to a verify email messagen after entering suitable email, username and password, registration was successful after verifying email.

<hr>

Description:

Ensure a user can log in to the store.

Steps:

1. Navigate to [Ethical Gearz](https://ci-p5-egz.herokuapp.com/) and click Login
2. Enter login details created during registration
3. Click sign in

Expected:

User is successfully logged in and redirected to the home page.

Actual:

User is successfully logged in and redirected to the home page.

<hr>

Description:

Ensure a user can log out of the store.

Steps:

1. Log in to the store
2. Click the logout button
3. Click confirm on the confirm sign out page

Expected:

User is logged out

Actual:

User is logged out

<hr>

Description:

Ensure a user can log in with the correct credentials

Steps:

1. Navigate to [Ethical Gearz](https://ci-p5-egz.herokuapp.com/) and click Login
2. Enter login details for account (username: backupadmin, password )
3. Click sign in

Expected:

User is successfully logged in and redirected to the home page

Actual:

User is successfully logged in and redirected to the home page

## Navigation Links

Testing was performed to ensure all navigation links on the respective pages, navigated to the correct pages as per design. This was done by clicking on the navigation links on each page.

<hr>

Description:

Ensure a user can navigate to the relevant page, including not logged in users, standard users, and superusers

Steps:

Click on the different navigations link in the navigation bar

Expected:

The user is directed to the relevant page, either redirecting to the login page for protected pages or displaying a 403 error.

Actual:

The user was directed to the relevant page, redirecting to the login page for protected pages and displayed a 403 error.

Testing was performed to ensure a user can successfully buy a product from the store. The steps include logging in, selecting a product, customizing the order, clicking checkout, entering in details, entering credit card information, and receiving an order confirmation email.
Description

Ensure a user can buy a product from the store and receive an order confirmation email.

Steps:

1. Log in to the store
2. Browse products and select a product to purchase
3. Customize the order (if applicable)
4. Click on the checkout button
5. Enter shipping and billing details
6. Enter credit card information
7. Click on the purchase button
8. Check for order confirmation email

Expected:

1. User is able to log in to the store
2. User is able to select a product to purchase
3. User is able to customize the order (if applicable)
4. User is directed to the checkout page
5. User is able to enter shipping and billing details
6. User is able to enter credit card information
7. User is able to complete the purchase
8. User receives an order confirmation email

Actual:

1. User was able to log in to the store
2. User was able to select a product to purchase
3. User was able to customize the order (if applicable)
4. User was directed to the checkout page
5. User was able to enter shipping and billing details
6. User was able to enter credit card information
7. User was able to complete the purchase
8. User received an order confirmation email.

<hr>
## Bugs

* Used *[StackOverFlow](https://stackoverflow.com/questions/70466886/typeerror-init-got-an-unexpected-keyword-argument-providing-args)* to fix allauth version error, which required an upgrade to allauth 0.51.0

* Used *[StackOverFlow](https://stackoverflow.com/questions/70285834/forbidden-403-csrf-verification-failed-request-aborted-reason-given-for-fail/70326426#70326426)* to fix csrf verification error to login to django admin site, which required adding CSRF_TRUSTED_ORIGINS in settings.py file.
