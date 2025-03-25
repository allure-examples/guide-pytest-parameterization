# Allure Report with Pytest parameterization

This repository is a part of Allure Report documentation and contains code examples for integrating Allure Report with Pytest parameterized tests. You can find the original documentation:

- [English version](https://allurereport.org/docs/guides/pytest-parameterization/)
- [Spanish version](https://allurereport.org/es/docs/guides/pytest-parameterization/)

## Preparation

1. Make sure you have installed:

    - [Python](https://www.python.org/downloads/) version 3.9 or higher
    - [Allure Report](https://allurereport.org/docs/install/)

1. Clone the repository via HTTPS:

    ```shell
    git clone https://github.com/allure-examples/guide-pytest-parameterization.git
    ```

    or SSH:

    ```shell
    git clone git@github.com:allure-examples/guide-pytest-parameterization.git
    ```

1. In the shell of your choice, navigate to the repository directory:

    ```shell
    cd path/to/guide-pytest-selenium-screenshots
    ```

## Run tests

The repository provides automatic scripts that install the virtual environment, and necessary packages, and run the tests. Run the script that corresponds to your operating system. For Linux and MacOS:

```
./run.sh
```
For OS Windows:
```shell
.\run.bat
```

Alternatively:
1. Create a Python virtual environment manually:

    ```shell
    python -m venv venv
    ```

1. Activate the virtual environment (Linux and MacOS):

    ```shell
    source venv/bin/activate
    ```

    OS Windows:

    ```powershell
    .\venv\Scripts\Activate.ps1
    ```

1. Install the packages used in the project:

    ```
    pip install -r requirements.txt
    ```

1. Run Pytest:

    ```
    pytest
    ```

## Run Allure Report

1. To start a local Allure Report server, in the project root directory run:

    ```shell
    allure serve -p <port-of-your-choice>
    ```

1. Browse the Allure Report page on `http://127.0.0.1:<port-of-your-choice>`
