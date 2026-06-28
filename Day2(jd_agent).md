# JD Intelligence Agent

## Objective

The purpose of the JD Intelligence Agent is to transform an unstructured Job Description into a structured Hiring Rubric that can be directly consumed by the Ranking Engine.

Unlike traditional keyword matching systems, the JD Agent performs semantic understanding of recruiter intent using Google's Gemini model.

---

# Why We Built This

Initially, the idea was to compare resumes directly with the Job Description using semantic similarity.

However, this approach has several limitations:

* Recruiters describe the same requirement in different ways.
* Technologies should be grouped into recruiter-level capabilities.
* Different skills should have different importance.
* The Ranking Engine should receive structured information instead of raw text.

Therefore, we introduced the JD Intelligence Agent as the first AI module in the pipeline.

---

# Initial Design

The first version returned only basic information.

Example:

```json
{
    "role": "",
    "experience": {
        "minimum": 0,
        "preferred": 0
    },
    "required_capabilities": [],
    "preferred_capabilities": [],
    "behavioral_traits": [],
    "negative_signals": [],
    "summary": ""
}
```

Although functional, this structure lacked explainability and weighting.

---

# Design Improvements

During implementation several improvements were introduced.

## Capability Importance

Instead of returning plain capability names,

Old

```json
[
    "backend",
    "cloud"
]
```

New

```json
[
    {
        "name": "backend",
        "importance": 10,
        "reason": "REST APIs, Python and production systems are mandatory."
    }
]
```

Benefits

* Importance can directly influence ranking.
* Every AI decision becomes explainable.
* Frontend can display recruiter reasoning.

---

## Behavioral Traits

Originally behavioral traits were returned as free-form English.

Example

```text
Excellent communication skills
```

This was replaced with canonical recruiter vocabulary.

Current values include

* communication
* leadership
* ownership
* teamwork
* adaptability
* problem_solving
* learning
* mentoring

This ensures consistency across the system.

---

## Search Query Generation

The JD Agent now generates a semantic search query.

Example

```text
backend python rest api docker aws kafka spark
```

Purpose

This query will later be embedded and used to retrieve candidate vectors from FAISS before invoking the Candidate Intelligence Agent.

This dramatically reduces the number of LLM calls.

---

## Explainable AI

Every inferred capability now includes a short explanation.

Example

```json
{
    "name": "devops",
    "importance": 8,
    "reason": "Docker and production systems indicate DevOps responsibilities."
}
```

This provides transparency during ranking and makes the system easier to justify to recruiters and judges.

---

# Pydantic Integration

The project migrated from plain dictionaries to strongly typed Pydantic models.

Implemented models

* Experience
* Capability
* BehavioralTrait
* HiringRubric

Benefits

* Automatic validation
* Better IDE autocomplete
* Type safety
* Easier FastAPI integration
* Cleaner project structure

---

# Prompt Engineering

The prompt was refined to improve consistency.

Rules added

* Return only valid JSON.
* Use predefined capability names.
* Use predefined behavioral traits.
* Assign importance values.
* Generate short reasoning.
* Ignore company names.
* Ignore salary.
* Ignore location.
* Ignore HR statements.
* Generate a semantic search query.

The agent therefore produces deterministic output while still leveraging Gemini's reasoning capabilities.

---

# Final Hiring Rubric Structure

The final output schema is

```text
HiringRubric

│

├── Role

├── Experience

│      ├── Minimum

│      ├── Preferred

│      └── Reason

│

├── Required Capabilities

│      ├── Name

│      ├── Importance

│      └── Reason

│

├── Preferred Capabilities

│

├── Behavioral Traits

│

├── Negative Signals

│

├── Search Query

│

└── Summary
```

---

# Test Results

The implemented JD Agent successfully analyzed a sample Backend Engineer Job Description.

Extracted Role

* Backend Engineer

Experience

* Minimum Experience: 3 Years

Required Capabilities

* Backend (Importance: 10)
* DevOps (Importance: 8)
* Cloud (Importance: 8)

Preferred Capability

* Data Engineering (Importance: 4)

Behavioral Traits

* Communication

Additional Outputs

* Semantic Search Query generated successfully.
* Recruiter Summary generated successfully.

All outputs passed Pydantic validation.

---

# Engineering Decisions

Several important architectural decisions were finalized during this module.

* The JD Agent is responsible only for understanding recruiter intent.
* Capability extraction is performed at the recruiter level rather than the technology level.
* AI-generated decisions must always include reasoning.
* Ranking weights originate from recruiter intent rather than hardcoded values.
* The Ranking Engine will consume structured Hiring Rubrics instead of natural language job descriptions.
* Search Query generation is integrated into the JD Agent to support semantic candidate retrieval.

---

# Final Status

The JD Intelligence Agent is considered Version 1 Complete.

It now converts natural language Job Descriptions into structured, explainable Hiring Rubrics that serve as the recruiter-facing intelligence layer of the recruitment system.
