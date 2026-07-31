# Python Selenium Automation Framework

![Python](https://img.shields.io/badge/Python-3.13-blue?logo=python)
![Selenium](https://img.shields.io/badge/Selenium-4.x-43B02A?logo=selenium)
![Pytest](https://img.shields.io/badge/Pytest-Framework-0A9EDC?logo=pytest)
![GitHub Actions](https://img.shields.io/github/actions/workflow/status/xjoule42/qa-selenium-framework/ui-tests.yml?branch=main&label=CI&logo=githubactions)
![Release](https://img.shields.io/github/v/release/xjoule42/qa-selenium-framework)
![License](https://img.shields.io/github/license/xjoule42/qa-selenium-framework)


A scalable UI test automation framework built with **Python**, **Selenium**, and **Pytest**, following the **Page Object Model (POM)** design pattern. This project showcases clean architecture, reusable automation components, explicit waits, structured logging, and industry best practices for web UI testing.

---

## 🚀 Tech Stack

- Python 3.13+
- Selenium WebDriver
- Pytest
- WebDriver Manager
- HTML Reports (pytest-html)
- Logging
- Page Object Model (POM)
- ChromeDriver

---

## 📁 Project Structure

```text
qa-selenium-framework/
│
├── config/
│   └── settings.py
│
├── reports/
│   ├── html/
│   └── screenshots/
│
├── src/
│   ├── core/
│   │   ├── driver_factory.py
│   │   ├── logger.py
│   │   └── waits.py
│   │
│   ├── locators/
│   │
│   ├── pages/
│   │
│   └── utils/
│
├── tests/
│   ├── smoke/
│   ├── regression/
│   └── e2e/
│
├── .env
├── conftest.py
├── pytest.ini
├── requirements.txt
└── README.md
```

---

# Features

- ✅ Page Object Model (POM)
- ✅ Reusable BasePage
- ✅ Centralized explicit waits
- ✅ Driver Factory
- ✅ Structured logging
- ✅ Smoke Tests
- ✅ Regression Tests
- ✅ End-to-End Tests
- ✅ HTML Reports
- ✅ Environment variables (.env)
- ✅ Scalable project structure

---

# Test Categories

## Smoke

Critical functionality validation.

Examples:

- Login
- Inventory
- Add to Cart
- Remove from Cart
- Checkout

---

## Regression

Validation of business rules and negative scenarios.

Examples:

- Invalid credentials
- Locked user
- Empty username/password
- Error messages

---

## End-to-End

Complete purchase flow.

Flow covered:

Login

↓

Inventory

↓

Cart

↓

Checkout Information

↓

Checkout Overview

↓

Checkout Complete

---

# Installation

Clone the repository

```bash
git clone https://github.com/your-username/qa-selenium-framework.git

cd qa-selenium-framework
```

Create a virtual environment

```bash
python -m venv venv
```

Activate it

Windows

```bash
venv\Scripts\activate
```

Linux / macOS

```bash
source venv/bin/activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

---


# Environment Variables

Create a `.env` file in the project root.

Example:

```env
STANDARD_USERNAME=standard_user
STANDARD_PASSWORD=secret_sauce
BASE_URL=https://www.saucedemo.com/
```

---

# Running Tests

Run all tests

```bash
python -m pytest
```

Verbose mode

```bash
python -m pytest -v
```

Smoke tests

```bash
python -m pytest tests/smoke
```

Regression tests

```bash
python -m pytest tests/regression
```

End-to-End tests

```bash
python -m pytest tests/e2e
```

---

# HTML Report

Generate report

```bash
python -m pytest --html=reports/html/report.html --self-contained-html
```

After execution, open:

```text
reports/html/report.html
```

---

# Logging

The framework provides structured logging during execution.

Example:

```text
Opening: https://www.saucedemo.com/

Typing username

Clicking Login

Waiting for element to be clickable

Checkout completed successfully
```

---

# Design Patterns

This framework uses:

- Page Object Model (POM)
- Factory Pattern (Driver Factory)
- Single Responsibility Principle
- Explicit Waits
- Reusable Components

---

# Future Improvements

- GitHub Actions
- Screenshots on Failure
- Firefox support
- Edge support
- Parallel execution
- Allure Reports
- Docker execution
- Cross-browser testing

---

# Why this project?

This framework was built to demonstrate practical automation testing skills using modern Python testing practices and clean architecture suitable for real-world QA Automation projects.

---

# Author

**Julio Soto**

Senior QA Engineer | Automation Tester

GitHub:

https://github.com/xjoule42

Portfolio:

https://xjoule42.github.io/

---

# License

This project is licensed under the MIT License.