
# Feature: Customer Login

## Page URL
https://parabank.parasoft.com/parabank/index.htm

## What this feature does
The login panel on the homepage allows existing registered customers
to authenticate and access their banking dashboard. It sits on the
left side of the homepage under "Customer Login".

## Page Elements
- Username field: text input, no character limit shown, required
- Password field: password input (masked), required
- Login button: submits the form
- "Forgot login info?" link: navigates to lookup page
- "Register" link: navigates to new customer registration

## Success Flow
- User enters valid username and password
- Clicks Login
- Redirected to /parabank/overview.htm (Accounts Overview page)
- Left panel shows full account services menu:
  (Open New Account, Accounts Overview, Transfer Funds,
   Bill Pay, Find Transactions, Update Contact Info,
   Request Loan, Log Out)

## Error Flows
- Wrong username or password → stays on login page,
  shows error: "The username and password could not be verified."
- Empty username + valid password → form does not submit or shows error
- Valid username + empty password → form does not submit or shows error
- Both fields empty → form does not submit or shows error

## Business Rules
- Credentials are case-sensitive
- No visible password strength rules on this page
- No CAPTCHA on login
- Session persists until user clicks Log Out
- "Forgot login info?" requires First Name, Last Name,
   Address, City, State, Zip, SSN to recover credentials

## Known Test Data
- Valid user: username = john, password = demo
- Invalid user: username = fakeuser, password = wrongpass

## Fields to validate
| Field    | Required | Max Length | Special chars allowed |
|----------|----------|------------|-----------------------|
| Username | Yes      | Unknown    | Yes                   |
| Password | Yes      | Unknown    | Yes                   |