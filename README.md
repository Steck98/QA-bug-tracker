# QA-bug-tracker

A small console application written in Python for managing bugs and users.

I'm building this project as part of my learning process towards QA Automation. The main goal is to practice Python, working with JSON files, Git, project structure, automated testing and writing code in separate modules instead of putting everything into one file.

The project is still being developed, so some features are not available yet.

## Current features

At the moment the application allows me to:

* add a new user
* add a new bug
* save data to a JSON file
* check if a user/bug ID already exists
* prevent duplicate IDs
* use a simple console menu
* run multiple operations without restarting the application
* handle incorrect menu/input values
* validate user input
* handle application errors
* run automated unit tests
* automatically run tests using GitHub Actions

## How the project works

The project is split into a few parts.

### Models

Contains classes used to represent the data:

* `Bug`
* `User`

### Input Handler

Handles communication with the user through the console.

It is responsible for getting the required information and passing it to the appropriate functions.

### Bug / Employee Management

These modules contain the logic for creating bugs and users.

For example, before adding a new bug, the application checks if another bug with the same ID already exists.

### Validation

Contains functions responsible for validating user input and checking whether provided values are valid.

Validation is separated from the main application logic so it can be tested independently.

### Data Manager

Responsible for reading and saving data.

The application currently uses a JSON file instead of a database.

This way the other modules don't have to directly work with the JSON file.

## Automated Testing

The project uses `pytest` for automated unit testing.

Tests cover the main parts of the application, including:

* models
* services
* input handling
* validation
* data management
* bug management
* user management

The tests are organized separately from the application code under the `tests/` directory.

Tests can be run locally with:

```bash
pytest
```

## CI/CD

The project uses GitHub Actions to automatically run the test suite.

The CI pipeline runs when changes are pushed to the repository or when a Pull Request is created for the `main` branch.

The pipeline currently:

1. checks out the repository
2. sets up Python
3. installs project dependencies
4. runs the complete `pytest` test suite

This allows me to automatically verify that new changes do not break existing functionality before merging them into `main`.

## Project structure

```text
## Project structure

QA-bug-tracker/

│
├── .github/
│   └── workflows/
│       └── ci.yml
│
├── src/
│   ├── models/
│   │   ├── bug.py
│   │   └── user.py
│   │
│   ├── services/
│   │   ├── data_manager.py
│   │   ├── bug_manager.py
│   │   └── employee_manager.py
│   │
│   ├── validators.py
│   ├── input_handler.py
│   └── main.py
│
├── tests/
│   └── unit_tests/
│       ├── input_tests/
│       ├── model_tests/
│       ├── services_tests/
│       └── validation_tests/
│
├── data/
│   └── data.json
│
└── requirements.txt
```

The structure will probably change as the project gets bigger.

## Running the application

Clone the repository and go to the project folder.

Then run:

```bash
python src.main.py
```

The application starts with the main menu.

Example:

```text
===============================

Welcome in our Bug tracker App

===============================

Would you like to:

1. Add new user

2. Report Bug

3. Exit
```

## Running tests

To run the automated tests locally:

```bash
pytest
```

The same test suite is also executed automatically by GitHub Actions.

## Example of current functionality

When adding a bug, the application checks the existing bug IDs.

For example, if:

```text
BUG-001
BUG-002
```

already exist, trying to create another `BUG-001` will be rejected.

The same principle is currently used for employee IDs.

## Technologies

Currently I'm using:

* Python
* pytest
* JSON
* Git
* GitHub
* GitHub Actions
* VS Code

I plan to use more tools later, especially:

* SQL
* API testing
* Selenium

## What I want to add later

The project is still a work in progress.

Some of the things I want to add:

* find bugs
* display bugs
* update bugs
* delete bugs
* find users
* update users
* delete users
* assign bugs to users
* change bug status
* change bug priority
* more validation
* refactoring after adding more functionality
* API testing
* database support
* Selenium tests

## Development

I'm developing the project step by step using separate Git branches for different tasks.

Some of the completed tasks so far:

* QBT-3 — Models
* QBT-4 — Data Manager
* QBT-5 — Input Handler
* QBT-6 — Validation
* QBT-7 — Bug Management
* QBT-8 — User Management
* QBT-9 — Main Menu
* QBT-10 — Error Handling
* QBT-11 — Automated Tests
* QBT-12 — README

The project is not finished yet. I'm adding new functionality gradually and refactoring parts of the code when there is a good reason to do so.

## Why I'm making this project

This is mainly a learning and portfolio project.

I want to use it to practice the things I'm learning in Python and QA Automation instead of only doing small individual exercises.

The idea is to start with a simple console application and gradually turn it into a more complete project with automated tests, API testing, database interaction and UI automation.
