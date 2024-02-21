# PyShiny Express: Tips Dashboard

- Repository: [pyshiny-tips-dashboard-express](https://github.com/denisecase/pyshiny-tips-dashboard-express)
- Live App: [Tips Dashboard (Express)](https://denisecase.github.io/pyshiny-tips-dashboard-express/)

Run and publish interactive apps using PyShiny Express and GitHub Pages.

## Source

From <https://shiny.posit.co/py/docs/user-interfaces.html#altogether-now>

## Prerequisites

Before you start, have the following installed:

- **Python**: Install the most recent version from [python.org](https://www.python.org/downloads/).
- **Git**: Download and install Git from [git-scm.com](https://git-scm.com/downloads).
- **Visual Studio Code (VS Code)**: Download from [code.visualstudio.com](https://code.visualstudio.com/).
- **VS Code Extensions**: Install the Python extension for VS Code.

### Configurations

- **Configure Git**: Set up your user name and email with Git using the following commands in your terminal:

  ```shell
  git config --global user.name "Your Name"
  git config --global user.email "youremail@example.com"

## Set up the Project

### Verify Installations

1. Open project folder in VS Code.
2. Open a new terminal (on Windows, ensure the terminal type is PowerShell (not the old cmd)
3. Run the following commands in the terminal one at a time::

```shell
py --version
git --version
git config user.name
git config user.email
```

## Python Project Virtual Environment

1. Create a virtual environment for the project:

  ```shell
  py -m venv .venv`
  ```

2. Activate the virtual environment

On Windows:

  ```shell
  .venv\Scripts\Activate
  ```

On macOS and Linux:

  ```shell
  source .venv/bin/activate
  ```

Install packages:

First, upgrade pip and wheel for good measure.
Then, install the project-specific required packages:

```shell
py -m pip install --upgrade pip wheel
py -m pip install --upgrade -r requirements.txt
```

## Run the App

With your project virtual environment activated in the terminal and the necessary packages installed, run the app with live reloading and automatically open it in the browser:

```shell  
shiny run --reload --launch-browser tips/app.py
```

While the app is running, that terminal is fully occupied.
Open a new terminal to run other commands.

## Build the App

With your project virtual environment activated in the terminal and the necessary packages installed, remove any existing assets and use shinylive export to build the app in tips folder to the docs folder:

```shell
shiny static-assets remove
shinylive export tips docs
```

## Publish the App with GitHub Pages

1. Git add/commit/push changes to the main branch:

```shell
git add .
git commit -m "Your commit message"
git push -u origin main
```

2. Go to the repository on GitHub and navigate to the Settings tab.
3. Scroll down to the GitHub Pages section and select the main branch as the source for the site.
4. Publish from the docs folder.
5. Click Save and wait for the site to build.
