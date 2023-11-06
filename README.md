
# Tech Stack Documentation

## Tech Stack
- Poetry
- Django
- Django Rest Framework

## Tools
- Recommended Editor: VSCode

## Setting up the Development Environment

1. Clone the repository:
   ```bash
   git clone https://github.com/your/repo.git
   cd repo
   ```

2. Install Poetry using pip:
   ```bash
   pip install poetry
   ```

3. Install project dependencies with Poetry:
   ```bash
   poetry install
   ```

4. Create and activate the virtual environment:
   ```bash
   poetry shell
   ```

5. Make sure all dependencies are installed inside the virtual environment:
   ```bash
   poetry lock
   ```

6. Run the Django server:
   ```bash
   python manage.py runserver
   ```

## Pre-commit Hooks

We use pre-commit hooks to ensure code quality and consistency before each commit. Follow these steps to set up pre-commit hooks:

1. Set up pre-commit hooks:
   ```bash
   pre-commit install
   ```

Now, pre-commit hooks will run automatically before each commit, checking for linting, formatting, and other code quality standards.

## Using Commitizen for Commit Messages

To maintain consistent and meaningful commit messages, we use Commitizen. Commitizen prompts you for the type of change you're committing, whether it's a new feature, a bug fix, documentation changes, etc., and generates a commit message following a specific format.

1. Install Commitizen using pip:
   ```bash
   pip install commitizen
   ```

2. Commit your changes using Commitizen:
   ```bash
   cz commit
   ```

Commitizen will guide you through the process of creating a commit message.

## Running Flake8 and isort

To ensure code quality and proper import sorting, we use Flake8 and isort. You can run them as follows:

1. Run Flake8 to check for code style and potential issues:
   ```bash
   poetry run flake8
   ```

2. Use isort to sort your imports properly:
   ```bash
   poetry run isort .
   ```

By following these steps, you can maintain code quality, consistency, and meaningful commit messages while working on the project.
