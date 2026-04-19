# Test Writing Guide — Rules & Standards

## Test Case Structure
Every test case must follow this exact structure:

**TC-[ID]: [Short descriptive title]**
- Priority: High / Medium / Low
- Precondition: [State of system before test begins]
- Steps: [numbered list]
- Expected Result: [what success looks like]

---

## Step Types — This is the most important rule

There are exactly two types of steps. Never mix them up.

### Type 1 — Action / Navigation Step
The tester is DOING something. No verification happening.
Action steps must start with one of these verbs only:
- Navigate to
- Click
- Enter
- Type
- Select
- Scroll
- Hover over
- Upload
- Clear
- Submit

**Examples:**
- Navigate to https://parabank.parasoft.com/parabank/index.htm
- Enter "john" in the Username field
- Enter "demo" in the Password field
- Click the Login button
- Select "CHECKING" from the account type dropdown
- Clear the username field

### Type 2 — Verification Step
The tester is CHECKING something. Must always start with "Verify that".
Never use: "Check", "Confirm", "See", "Ensure", "Make sure", "Assert"
Only use: "Verify that"

**Examples:**
- Verify that the Accounts Overview page is displayed
- Verify that the error message "The username and password could not be verified." is shown
- Verify that the password field is masked (characters not visible)
- Verify that the Login button is disabled when fields are empty
- Verify that the URL changes to /parabank/overview.htm

---

## Priority Rules

| Priority | When to use |
|----------|-------------|
| High     | Core functionality — if broken, users cannot use the app |
| Medium   | Important but has a workaround |
| Low      | Cosmetic, UI alignment, nice-to-have |

Login, Register, Transfer Funds, Bill Pay = always High priority
Error messages, field validations = Medium
Label text, color, alignment = Low

---

## Precondition Rules
- Must describe the EXACT state before the test starts
- Always mention which page the user is on
- If test needs logged-in user, state: "User is logged in as john/demo"
- If test needs specific data, state it: "Account 12345 exists with balance $500"
- Never write "None" as precondition — there is always a precondition

**Good:** "User is on the ParaBank login page. User account exists with username: john, password: demo"
**Bad:** "None" or "App is open"

---

## Edge Case Rules — Always cover these for every feature

### 1. Empty field tests
- All fields empty → submit → verify validation message
- One field empty, other filled → verify which error appears
- Only spaces entered → treat as empty

### 2. Boundary value tests
- Minimum characters (1 char in username)
- Maximum characters (very long string 255+ chars)
- Exactly at limit

### 3. Special character tests
- Username with spaces: "john doe"
- Username with symbols: "john@#$"
- SQL injection attempt: ' OR 1=1 --
- XSS attempt: <script>alert('test')</script>

### 4. Case sensitivity tests
- Correct username with wrong case: "JOHN" instead of "john"
- Correct password with wrong case: "DEMO" instead of "demo"

### 5. Repeated action tests
- Login → Logout → Login again (session clears properly)
- Submit form twice quickly (double click)
- Browser back button after login

### 6. Error message tests
- Error message must be exact text — copy it from the app
- Error must appear in correct location on page
- Error must disappear when user corrects the input

---

## Naming Rules for Test Case IDs

Use feature prefix + number:

| Feature | Prefix | Example |
|---------|--------|---------|
| Login | LGN | LGN-001 |
| Register | REG | REG-001 |
| Transfer Funds | TRF | TRF-001 |
| Bill Pay | BLP | BLP-001 |
| Open Account | OAC | OAC-001 |
| Find Transactions | FTR | FTR-001 |
| Update Contact | UPD | UPD-001 |
| Request Loan | LON | LON-001 |

---

## What a complete test case looks like

**LGN-001: Login with valid username and password**
- Priority: High
- Precondition: User is on the ParaBank homepage. Valid account exists with username: john, password: demo
- Steps:
  1. Navigate to https://parabank.parasoft.com/parabank/index.htm
  2. Enter "john" in the Username field
  3. Enter "demo" in the Password field
  4. Click the Login button
  5. Verify that the user is redirected to the Accounts Overview page
  6. Verify that the URL contains /parabank/overview.htm
  7. Verify that the Account Services menu is visible on the left panel
  8. Verify that the welcome message shows the user's name
- Expected Result: User is successfully logged in and lands on the Accounts Overview page

---

**LGN-002: Login with invalid password**
- Priority: High
- Precondition: User is on the ParaBank homepage. Valid account exists with username: john
- Steps:
  1. Navigate to https://parabank.parasoft.com/parabank/index.htm
  2. Enter "john" in the Username field
  3. Enter "wrongpassword" in the Password field
  4. Click the Login button
  5. Verify that the user remains on the login page
  6. Verify that the error message "The username and password could not be verified." is displayed
  7. Verify that the password field is cleared after failed attempt
- Expected Result: Login fails and a clear error message is shown to the user