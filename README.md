# Project Name

## Description
This project is a test automation framework for Twitch using Selenium and Playwright in Python. It includes test cases for various functionalities of the Twitch website, such as searching for games, selecting streamers, and handling popups.

## Project Structure
- **pages**: This directory contains page object classes representing different pages of the Twitch website.
- **utils**: This directory contains utility modules used in the project, such as logger setup and configuration management.
- **tests**: This directory contains the test cases implemented using pytest framework.
- **.env**: This file contains environment variables used for configuration, such as the Twitch URL.
- **requirements.txt**: This file lists all the dependencies required for running the project.
- **Dockerfile**: This file contains instructions to build a Docker image for the project.
- **README.md**: This file provides an overview of the project, its structure, and instructions for running the tests locally.

## Installation
1. Clone the repository: `git clone <repository-url>`
2. Install dependencies: `pip install -r requirements.txt`
3. Set up environment variables: Create a `.env` file and specify the Twitch URL.

## Usage
To run the tests locally:
```
pytest
```

## Additional Notes
- Make sure to have Chrome and/or Chromium browser installed on your system for running the tests.
- For running tests in headless mode, modify line 14 in `conftest.py`
```python
        browser = p.chromium.launch(headless=True, executable_path="/opt/google/chrome/chrome")
```

## GIF demo
![Demo GIF](./videos/output.gif)
