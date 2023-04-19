# Functional Testing

## Authentication

Description:

Ensure a user can register on the store.

Steps:

1. Navigate to [Ethical Gearz](https://ci-p5-egz.herokuapp.com/) and click Register
2. Enter email, username and password
3. Click Register

Expected:

The user is directed back to login screen to login after entering suitable username and password, registration is successful

Actual:

The user is directed back to login screen to login after entering suitable username and password, registration was successful with an email confirmation link being recieved. 

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

The user is directed to the relevant page

Actual:

The user is directed to the relevant page

<hr>
## Bugs

* Used *[StackOverFlow](https://stackoverflow.com/questions/70466886/typeerror-init-got-an-unexpected-keyword-argument-providing-args)* to fix allauth version error, which required an upgrade to allauth 0.51.0

* Used *[StackOverFlow](https://stackoverflow.com/questions/70285834/forbidden-403-csrf-verification-failed-request-aborted-reason-given-for-fail/70326426#70326426)* to fix csrf verification error to login to django admin site, which required adding CSRF_TRUSTED_ORIGINS in settings.py file.
