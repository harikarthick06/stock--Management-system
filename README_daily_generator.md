# Daily Project Generator

This script (`daily_project_generator.py`) helps you automatically create a new repository with a small starter project each time you run it. A random template is selected from simple examples (React, HTML/CSS/JS, C++, or a basic machine learning snippet) and pushed to your GitHub account.

## Requirements

- Python 3
- `git` installed and in your `PATH`
- A GitHub personal access token with `repo` permissions

## Usage

1. Export your GitHub username and token as environment variables:
   ```bash
   export GITHUB_USERNAME=yourusername
   export GITHUB_TOKEN=ghp_yourtoken
   ```

2. Run the script:
   ```bash
   python3 daily_project_generator.py
   ```

The script creates a new directory, initializes a git repository, creates a remote repository on GitHub, and pushes the code. Run it once per day (e.g., via `cron`) to add a small project daily to your account.
