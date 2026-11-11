# ds-starter

A simple starter project for Python data science. It uses [uv](https://docs.astral.sh/uv/) to manage Python and packages, git to track changes, and pytest to test the code. Nothing else.

> **This README is a template.** Every section below is one your own project's README should have. When you start your analysis, keep the headings and replace the contents with your own. Each section ends with a ✏️ note telling you what to write.

## About this project

This project takes a small file of made-up sales orders, cleans it, and saves a summary of revenue for each region. It exists to show a good project layout and three ways to run the same code: as a script, in the Python REPL, and in a Jupyter notebook.

✏️ *Replace with: the question your analysis answers, who it is for, and what it produces. Two or three sentences.*

## Requirements

- [git](https://git-scm.com/downloads)
- [uv](https://docs.astral.sh/uv/getting-started/installation/)

You do not need to install Python yourself. uv downloads the right version for you.

Install uv on macOS or Linux:

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

Install uv on Windows (PowerShell):

```powershell
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

Close and reopen your terminal, then check both tools work:

```bash
git --version
uv --version
```

✏️ *Replace with: anything a person needs before they start, such as access to a database or a data file they must download.*

## Setup

**1. Make your own copy on GitHub.** On this repo's GitHub page, click **Use this template → Create a new repository**, give it a name, and click **Create repository**. You now have your own repo that you can push to.

**2. Clone your copy and install.**

```bash
git clone <url-of-your-repo>
cd <your-repo-name>
uv sync
```

`uv sync` creates a virtual environment in `.venv/` and installs everything listed in `pyproject.toml`. Run it again whenever you pull new changes.

**3. Save your work back to GitHub** whenever you finish a piece of work:

```bash
git add .
git commit -m "Describe what you changed"
git push
```

Git will ask you to sign in to GitHub the first time you push.

<details>
<summary>No "Use this template" button?</summary>

Create a new, empty repository on GitHub (do not tick "Add a README"), then run:

```bash
git clone <url-of-this-repo> <your-repo-name>
cd <your-repo-name>
git remote set-url origin <url-of-your-new-repo>
git push -u origin main
uv sync
```

`git remote set-url` points your local copy at your new repo instead of this one.

</details>

**4. Excluding files from git / GitHub**

Any files you don't want tracked by git (and uploaded to GitHub) can be excluded by listing them in the .gitignore file. This is standard practice for large or sensitive data.

✏️ *Replace with: just the clone and `uv sync` commands with your repo's URL and folder name, plus any extra setup steps.*

## Project structure

```
ds-starter/
├── data/
│   ├── raw/                 # Original data. Never edit these files by hand.
│   │   └── sales.csv
│   └── processed/           # Outputs created by the pipeline. Not tracked by git.
├── notebooks/
│   └── 01_example.ipynb     # For exploring. Number notebooks so they stay in order.
├── scripts/
│   └── run_pipeline.py      # Reads data, runs the pipeline, saves the result.
├── src/ds_starter/          # Reusable code, imported by scripts and notebooks.
│   ├── config.py            # File paths, kept in one place.
│   ├── helpers.py           # Small functions that each do one job.
│   └── pipeline.py          # The orchestrator that calls the helpers in order.
├── tests/                   # Checks that the code in src/ does what it should.
│   ├── test_helpers.py
│   └── test_pipeline.py
├── pyproject.toml           # Project settings and the list of packages.
├── uv.lock                  # Exact package versions. Created by uv; do not edit.
└── README.md
```

The rule of thumb: explore in `notebooks/`, and once code works and you want to reuse it, move it into a function in `src/ds_starter/`.

✏️ *Replace with: your own tree. Update it when you add folders or important files.*

## Data

`data/raw/sales.csv` holds 202 made-up orders from January to June 2026.

| Column       | Description                                      |
| ------------ | ------------------------------------------------ |
| `order_id`   | Unique order number                              |
| `order_date` | Date of the order (`YYYY-MM-DD`)                 |
| `region`     | Sales region: North, South, East or West         |
| `product`    | Product name                                     |
| `units`      | Number of units sold                             |
| `unit_price` | Price of one unit in dollars                     |

The file is messy on purpose: some regions are in lower case or have extra spaces, a few rows are missing `units`, and two orders appear twice.

✏️ *Replace with: where your data came from, when you got it, what each column means, and any known problems. If the data is too large or too sensitive for git, say how to get it.*

## How to run

Run every command from the project folder. Starting a command with `uv run` means "run this using the project's environment", so you never need to activate anything.

### 1. As a script

```bash
uv run scripts/run_pipeline.py
```

This reads `data/raw/sales.csv`, runs the pipeline, and saves `data/processed/sales_summary.csv`.

### 2. In the Python REPL

The REPL lets you run code one line at a time, which is handy for quick checks. Start it:

```bash
uv run python
```

Then type each line at the `>>>` prompt:

```python
import pandas as pd
from ds_starter.config import RAW_SALES_PATH
from ds_starter.pipeline import run_pipeline

raw_sales = pd.read_csv(RAW_SALES_PATH)
raw_sales.head()

summary = run_pipeline(raw_sales)
summary
```

Type `exit()` to leave.

### 3. In a Jupyter notebook

```bash
uv run jupyter lab
```

JupyterLab opens in your browser. Open `notebooks/01_example.ipynb` and run each cell with Shift + Enter. To stop JupyterLab, press Ctrl + C in the terminal.

✏️ *Replace with: the exact commands to reproduce your results, in the order they must be run.*

## How the pipeline works

```
scripts/run_pipeline.py          src/ds_starter/pipeline.py        src/ds_starter/helpers.py

pd.read_csv(...)  ──────────▶    run_pipeline(raw_sales)  ───────▶  clean_sales(df)
                                                                    add_revenue(df)
summary.to_csv(...)  ◀───────    returns summary  ◀──────────────   summarise_by_region(df)
```

1. **The script** reads the raw CSV with pandas.
2. **The orchestrator** (`run_pipeline`) receives the DataFrame and decides which helpers run, in what order.
3. **The helpers** each take a DataFrame, do one small job, and return a new DataFrame.
4. The result is returned to the script, which saves it with pandas.

Only the script touches files. The orchestrator and helpers just take data in and hand data back, which is why the same functions work in the script, the REPL and the notebook.

✏️ *Replace with: the steps of your own analysis, in order, and which file each step lives in.*

## Tests

A test is a small function that runs your code on an example and checks the answer. Tests catch mistakes early, and tell you straight away if a later change breaks something that used to work. This project uses [pytest](https://docs.pytest.org/).

Run every test:

```bash
uv run pytest
```

A dot means a test passed and an `F` means it failed. When a test fails, pytest shows the line that failed and the values it compared.

Other useful ways to run tests:

```bash
uv run pytest -v                        # show the name of each test
uv run pytest tests/test_helpers.py     # run one file
uv run pytest -k revenue                # run tests with "revenue" in the name
```

A test follows three steps: set up some data, run your function, check the result with `assert`.

```python
def test_add_revenue_multiplies_units_by_unit_price():
    df = pd.DataFrame({"units": [2, 4], "unit_price": [3.0, 4.5]})

    result = add_revenue(df)

    assert result["revenue"].tolist() == [6.0, 18.0]
```

To add your own, follow two naming rules so pytest can find them: files are named `tests/test_*.py` and functions are named `test_*`. Use tiny DataFrames you type out by hand, so you can work out the right answer yourself. Aim for at least one test for each helper function.

✏️ *Replace with: the command to run your tests and a sentence on what they cover.*

## Outputs

| File                               | Description                                             |
| ---------------------------------- | ------------------------------------------------------- |
| `data/processed/sales_summary.csv` | Orders, units, revenue and average order value by region |

Files in `data/processed/` are not tracked by git, because anyone can recreate them by running the pipeline.

✏️ *Replace with: each file, table or chart your project produces and what it shows.*

## Everyday commands

| Task                               | Command                                      |
| ---------------------------------- | -------------------------------------------- |
| Install or update the environment  | `uv sync`                                    |
| Add a package                      | `uv add matplotlib`                          |
| Remove a package                   | `uv remove matplotlib`                       |
| Run a script                       | `uv run scripts/run_pipeline.py`             |
| Open the REPL                      | `uv run python`                              |
| Open JupyterLab                    | `uv run jupyter lab`                         |
| Run the tests                      | `uv run pytest`                              |
| See what you have changed          | `git status`                                 |
| Save your changes                  | `git add .` then `git commit -m "message"`   |
| Send your changes to GitHub        | `git push`                                   |

Always use `uv add` instead of `pip install`. It records the package in `pyproject.toml` and `uv.lock`, so everyone who clones the project gets the same versions. Commit both files.

✏️ *Replace with: keep this table, and add any commands specific to your project.*

## Making this project your own

1. Rename the folder `src/ds_starter/` to your project's name. Use lower case and underscores, for example `src/housing_analysis/`.
2. In `pyproject.toml`, change `name` to match, using hyphens instead of underscores (`housing-analysis`), and update `description`.
3. Change `ds_starter` to your new name in the `import` lines in `scripts/`, `notebooks/`, `tests/` and `src/`.
4. Run `uv sync`.
5. Put your data in `data/raw/` and delete `sales.csv`.
6. Replace the example helpers, pipeline, script, notebook and tests with your own.
7. Rewrite each section of this README for your project, then delete this section and the note at the top.

✏️ *Delete this section when you are done.*
