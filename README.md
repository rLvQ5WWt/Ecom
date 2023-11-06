# Ecom
Tech Stack
Poetry Documentation
Django
Django Rest Framework
Tools
Recommended Editor: VSCode
Setting up the Development Environment
Clone the repo
Install poetry using pip install poetry
Run poetry install
To spawn the shell inside the virtual environment, run poetry shell
After spawning the shell inside the virtual environment, make sure dependencies are installed. If not, run poetry lock
To run the server, execute py manage.py runserver
Pre-commit Hooks
We use pre-commit hooks to ensure code quality and consistency before each commit. Follow these steps to set up pre-commit hooks:

Set up pre-commit hooks
poetry shell
pre-commit install
Now, pre-commit hooks will run automatically before each commit, checking for linting, formatting, and other code quality standards.

Using Commitizen for Commit Messages
To maintain consistent and meaningful commit messages, we use Commitizen. Commitizen prompts you for the type of change you're committing, whether it's a new feature, a bug fix, documentation changes, etc., and generates a commit message following a specific format.

To use Commitizen:

Install Commitizen using pip: pip install commitizen
Commit your changes using Commitizen: cz commit 
Commitizen will guide you through the process of creating a commit message.

