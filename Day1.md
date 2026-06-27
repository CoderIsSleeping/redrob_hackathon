# Day 1 - Project Initialization & Foundation

**Date:** 27 June 2026

---

# Objective

The primary objective for Day 1 was to establish the project's engineering foundation before integrating any AI components. Instead of directly developing ranking models, the focus was placed on understanding the dataset, designing the architecture, and building reusable preprocessing modules.

---

# Project Initialization

Completed the initial project setup with the following directory structure:

```text
agents/
app/
data/
models/
notebooks/
preprocessing/
scripts/
tests/
utils/
```

Configured:

* Virtual Environment
* Python dependencies
* Git repository
* `.gitignore`
* Project configuration file (`config.py`)

---

# Exploratory Data Analysis (EDA)

Performed an initial exploration of the Redrob candidate dataset.

The analysis included:

* Candidate count
* Experience distribution
* Industry distribution
* Company size distribution
* Open-to-work statistics
* Notice period analysis
* GitHub activity analysis
* Recruiter response rate analysis
* Missing value inspection

The results of this analysis have been documented separately in `Observation.md`.

---

# Feature Engineering

Implemented the first set of reusable feature engineering utilities.

Implemented functions:

* `calculate_notice_score()`
* `get_experience_bucket()`
* `has_github_profile()`
* `normalize_github_score()`
* `calculate_availability_score()`

These functions convert raw numerical recruiter signals into normalized features that can be directly used during candidate ranking.

---

# Candidate Intelligence Card

Designed and implemented the Candidate Intelligence Card.

Instead of allowing every module to directly access raw JSON, the project now converts every candidate into a standardized internal representation.

The Candidate Intelligence Card currently consists of:

## Semantic Information

* Headline
* Summary
* Career Text
* Skills Text

## Behavioral Information

* Notice Score
* Availability Score
* GitHub Score
* GitHub Availability
* Recruiter Response Rate

## Metadata

* Experience Bucket
* Industry
* Company Size

This standardized representation becomes the primary input for future AI modules.

---

# Dataset Preprocessing Pipeline

Implemented the preprocessing pipeline responsible for converting the complete raw dataset into Candidate Intelligence Cards.

Pipeline:

```text
Raw Dataset
        ↓
Candidate Card Builder
        ↓
Processed Dataset
```

The pipeline successfully processed all **100,000 candidate profiles** and generated a structured dataset inside:

```text
data/processed/
```

Future modules will consume the processed dataset rather than the raw candidate JSON.

---

# Evidence Extraction Module (Version 1)

Implemented the first version of the Evidence Extraction system.

The extractor analyzes candidate semantic information and converts technical keywords into recruiter-oriented capability groups.

Current capability groups:

* Backend Engineering
* Data Engineering
* AI / Machine Learning
* Cloud
* DevOps
* Leadership
* Product Engineering

Each capability currently returns:

* Capability score
* Supporting evidence

Example:

```text
Data Engineering

Score:
0.86

Evidence:
Spark
Kafka
Airflow
DBT
Snowflake
```

This provides an explainable representation of candidate capabilities instead of relying solely on raw keyword matching.

---

# Testing

Validated:

* Feature engineering utilities
* Candidate card generation
* Full preprocessing pipeline
* Evidence extraction on processed candidate cards

Successfully processed all candidate records without runtime errors after resolving package import and schema issues.

---

# Engineering Decisions

Several important architectural decisions were finalized during development.

* All AI modules will operate on Candidate Intelligence Cards rather than raw dataset records.
* Behavioral recruiter signals remain deterministic and do not require LLM reasoning.
* Semantic information is preserved separately for future embedding generation and LLM reasoning.
* Evidence extraction is implemented as an independent layer to support explainable candidate ranking.
* The processed dataset becomes the canonical input for downstream ranking modules.

---

# Current Project Status

Completed Modules

* Project setup
* Dataset exploration
* Feature engineering utilities
* Candidate Intelligence Card
* Dataset preprocessing pipeline
* Evidence Extraction (Version 1)

Current Repository Status

The project now contains a complete preprocessing pipeline capable of transforming raw candidate profiles into structured recruiter-oriented representations, providing the foundation required for semantic retrieval, LLM reasoning, and intelligent candidate ranking.
