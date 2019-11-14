# Cookiecutter Digdag

A cookiecutter for digdag project, including py> operator, and td> operator.

## Requirements to use the cookiecutter template:

- Python 3.5 or later
- [Cookiecutter Python package](http://cookiecutter.readthedocs.org/en/latest/installation.html)

```sh
$ pip install --user cookiecutter
```

## To start a new project, run:

```sh
cookiecutter https://github.com/chezou/cookiecutter-digdag
```

## The output directory structure

```text
my_project
├── README.md
├── config
│   ├── params.test.yml     <- Configuration file for run through test. Mirror params.yml except for `td.database`
│   └── params.yml          <- Configuration file for production
├── awesome_workflow.dig    <- Main workflow to be executed
├── ingest.dig              <- Data ingestion workflow
├── py_scripts              <- Python scripts directory
│   ├── __init__.py
│   ├── data.py             <- Script to upload data to Arm Treasure Data
│   └── my_script.py        <- Main script to execute e.g. Data enrichment, ML training
├── queries                 <- SQL directory
├── run_test.sh             <- Test shell script for local run through test
└── test.dig                <- Test workflow for local run through test
```
