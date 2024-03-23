Machine Learning Wine Quality Prediction
==============================

Traditional wine quality assessment methods are subjective and inconsistent, highlighting the need for a more objective approach. 
This study introduces a machine learning-based model, utilizing the softmax classification, to predict the quality of Portuguese "Vinho Verde" wines from physicochemical properties. 
Our work promises to revolutionize wine quality evaluation, offering enhanced consistency and objectivity for producers and consumers alike.


# WineQualityPrediction

The following sections detail some general notes for working with `WineQualityPrediction`, including setup, and
various dependency requirements.

## Prerequisites

Install the following dependencies, ideally in a virtual environment such as
 [mamba](https://github.com/conda-forge/miniforge#install) (faster) or [miniconda](https://docs.conda.io/en/latest/miniconda.html#linux-installers) (slower).

***Please use python 3.8.***

```bash
# Recommended: use a virtual env (make sure the virtual env is installed on your machine)
mamba create -n WineQualityPrediction python=3.8
mamba activate WineQualityPrediction
# Install requirements
pip install -r requirements.txt
```

Project Organization
------------

    ├── README.md          <- The top-level README for developers using this project.
    ├── data
    │   ├── interim        <- Intermediate data that has been transformed.
    │   └── raw            <- The original, immutable data dump.
    │
    │
    ├── models             <- Trained and serialized models, model predictions, or model summaries
    │
    ├── notebooks          <- Jupyter notebooks. Naming convention is a number (for ordering),
    │                         the creator's initials, and a short `-` delimited description, e.g.
    │                         `1.0-jqp-initial-data-exploration`.
    │ 
    ├── reports            <- Generated analysis as HTML, PDF, LaTeX, etc.
    │   └── figures        <- Generated graphics and figures to be used in reporting
    │
    ├── requirements.txt   <- The requirements file for reproducing the analysis environment, e.g.
    │                         generated with `pip freeze > requirements.txt`
    │
    └── src                <- Source code for use in this project.
        ├── __init__.py    <- Makes src a Python module
        │
        ├── data           <- Scripts to download or generate data
        │   └── make_dataset.py
        │
        ├── features       <- Scripts to turn raw data into features for modeling
        │   └── build_features.py
        │
        ├── models         <- Scripts to train models and then use trained models to make
        │   │                 predictions
        │   ├── predict_model.py
        │   └── train_model.py
        │
        └── visualization  <- Scripts to create exploratory and results oriented visualizations
            └── visualize.py


--------

<p><small>Project based on the <a target="_blank" href="https://drivendata.github.io/cookiecutter-data-science/">cookiecutter data science project template</a>. #cookiecutterdatascience</small></p>
