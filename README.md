# PyShiny Express: Tips Dashboard

- Repository: [pyshiny-tips-dashboard-express](https://github.com/denisecase/pyshiny-tips-dashboard-express)
- Live App: [Tips Dashboard (Express)](https://denisecase.github.io/pyshiny-tips-dashboard-express/)

Run and publish interactive apps using PyShiny Express and GitHub Pages.

## Data Description

This app uses the Seaborn library to import the tips dataset. The dataset contains 244 records and 7 fields. The fields are:

Column names for the tips dataset include:

- total_bill: the bill amount (dollars)
- tip: the tip amount (dollars)
- sex: Male or Female
- smoker: Yes or No
- day: Day of the week
- time: Lunch or Dinner
- size: Size of the party

See: <https://github.com/mwaskom/seaborn-data/blob/master/tips.csv>

## Data Cleaning and Transformation

The tips dataset is a nice, clean dataset with no missing values.
Generally, no cleaning or transformation is needed.

## Source

From <https://shiny.posit.co/py/docs/user-interfaces.html#altogether-now>.
This version has been modified slightly for hosting with GitHub Pages.

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

Run the following commands in the terminal to set up a project virtual environment and install the necessary packages.
Run them from the root project folder (e.g. pyshiny-tips-dashboard-express).
Use PowerShell on Windows or the terminal on macOS and Linux.

### Create a Project Virtual Environment (generally one-time setup)

Create a project virtual environment in the .venv folder of the project root directory.

  ```shell
  py -m venv .venv`
  ```

### Activate the Project Virtual Environment (when you work on the project)

Once the project virtual environment exists,
 we activate the virtual environment to work on the project - or when we open a new terminal.
We can verify our environment is active when (.venv) appears in the terminal prompt.

On Windows:

  ```shell
  .venv\Scripts\Activate
  ```

On macOS and Linux:

  ```shell
  source .venv/bin/activate
  ```

We also need to select this project virtual environment in VS Code.
To do this, open the command palette (Ctrl+Shift+P) and search for "Python: Select Interpreter". Then, select the .venv folder in the project root directory.

### Install Packages into the Active Project Virtual Environment

When the project virtual environment is active,
install packages into the project virtual environment so they are available for use in the Python code.

NOTE:

- We **install** packages into the project virtual environment.
- We **import** packages into Python code (after they have been installed).

First, upgrade pip and wheel for good measure.
Then, install the project-specific required packages:

```shell
py -m pip install --upgrade pip wheel
py -m pip install --upgrade -r requirements.txt
```

## Run the App

With your project virtual environment activated in the terminal
 and the necessary packages installed, run the app with live reloading and
 automatically open it in the browser:

```shell  
shiny run --reload --launch-browser tips/app.py
```

While the app is running, that terminal is fully occupied.
Open a new terminal to run other commands.

## Build the App to Docs Folder and Test Locally

With your project virtual environment activated in the terminal
 and the necessary packages installed, remove any existing assets and use
 shinylive export to build the app in the tips folder to the docs folder:

```shell
shiny static-assets remove
shinylive export tips docs
```

After the app is built, serve the app locally from the docs folder to test before publishing to GitHub Pages.
In the terminal, run the following command from the root of the project folder:

```shell
py -m http.server --directory docs --bind localhost 8008
```

Open a browser (tested with Chrome) and navigate to [http://localhost:8008](http://localhost:8008) to view the app running locally.

## After Editing, Git Add/Commit/Push Changes to GitHub

After editing project files, use Git add/commit/push changes to the main branch of the repository.
Note that if a terminal is serving an app, it is not available for other commands.
Run the following commands from a new or available terminal to git add/commit/push changes to GitHub.
Replace "Your commit message" with a meaningful message about the changes you made to the project files.
Run commands one at a time and wait for each to complete before running the next.

```shell
git add .
git commit -m "Your commit message"
git push -u origin main
```

## Publish the App with GitHub Pages (one-time setup)

The first time you set up an app, you'll need to navigate to the repository on GitHub and configure the settings to publish the app with GitHub Pages.
After configuring the repository once, each time you push changes to the main branch, the app will automatically update.

1. Go to the repository on GitHub and navigate to the **Settings** tab.
2. Scroll down and click the **Pages** section.
3. Select branch **main** as the source for the site.
4. Select the **docs** folder to publish from.
5. Click Save and wait for the site to build.
6. Edit the "About" section of the repository to include a link to the live app.

## Resources

Example csv data from [tips.csv](https://github.com/mwaskom/seaborn-data/blob/master/tips.csv).
Used for review only. In the app, we import the data from the Seaborn library.
