# Test Conversion Guide — Rules & Standards

## Test case structure

Every test case must follow this exact structure:

{
  {
  "test_name": "Valid login",
  "prerequisites": [
    {
      "type": "navigate",
      "url": "https://parabank.parasoft.com/parabank/index.htm"
    }
  ],
  "flow": [
    {
      "page": "LoginPage",
      "action": "enter_username",
      "params": {"value": "testuser"}
    },
    {
      "page": "LoginPage",
      "action": "enter_password",
      "params": {"value": "password123"}
    },
    {
      "page": "LoginPage",
      "action": "click_login",
      "params": {}
    }
  ],
  "assertions": [
    {
      "page": "DashboardPage",
      "check": "is_visible",
      "params": {}
    }
  ]
}
---

## Step Types — This is the most important rule

ALWAYS return valid JSON. No explanations.
ACTIONS must be selected ONLY from this list:
[
"navigate",
"enter_username",
"enter_password",
"click_login",
"click",
"enter_text",
"select_dropdown",
"upload_file"
]


## Page naming rules:
Login related → "LoginPage"
Dashboard related → "DashboardPage"
Generic fallback → "Page"
PARAM RULES:
If step contains input → use: {"value": "..."}
If no data → use: {}
DO NOT:
Create new action names
Combine multiple steps into one
Skip steps
Add explanation text
STEP MAPPING LOGIC:

Examples:

"open login page" → action: "navigate", page: "LoginPage"
"enter username xyz" → action: "enter_username", params: {"value": "xyz"}
"click login button" → action: "click_login"
"verify dashboard is visible" → assertion: "is_visible", page: "DashboardPage"
ASSERTIONS must go ONLY in "assertions" section.
FLOW must contain ONLY user actions, NOT validations.
INPUT WILL BE:
Test Name
Steps (plain English)
OUTPUT MUST BE:

ONLY JSON. No markdown. No explanation.
