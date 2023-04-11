# Functional Testing

## Authentication

Description:

Steps:

Expected:

Actual:

## Bugs

* Used *[StackOverFlow](https://stackoverflow.com/questions/70466886/typeerror-init-got-an-unexpected-keyword-argument-providing-args)* to fix allauth version error, which required an upgrade to allauth 0.51.0

* Used *[StackOverFlow](https://stackoverflow.com/questions/70285834/forbidden-403-csrf-verification-failed-request-aborted-reason-given-for-fail/70326426#70326426)* to fix csrf verification error to login to django admin site, which required adding CSRF_TRUSTED_ORIGINS in settings.py file.
