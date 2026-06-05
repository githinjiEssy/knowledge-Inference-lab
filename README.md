# Student Academic Advisor Reasoning Engine

## Introduction
This repository contains a, rule-based Academic Advisor Expert System designed for **APT 3020: Knowledge-Based Systems**. The application uses forward chaining data inferencing mechanisms to evaluate student academic metrics, financial status, and behavioral history to generate contextual academic recommendations automatically.

## Problem Statement
University academic advising bodies often handle high volumes of student evaluation requests regarding scholarship matching, graduation clearances, honors listings, and probationary tracking. Manual compliance review is time-consuming and prone to human oversight. This project automates decision processing by building a data-driven reasoning framework to handle compliance mapping accurately based on configured criteria.

## Knowledge Base & Rules Implemented
The system maps domain attributes into clear categories using a decoupled architecture powered by `knowledge_base.json`. The engine tracks the following operational policies:
* **Scholarship Rule**: Triggers if a student maintains a GPA Above 3.5, Attendance Above 80%, and has No Disciplinary Cases.
* **Graduation Rule**: Triggers if a student has a GPA Above 3.0, Completed Prerequisites, and has No Outstanding Fees.
* **Probation Rule**: Triggers if a student falls Below a 3.0 GPA threshold.
* **Registration Rule**: Activates a registration block if any outstanding fee balances are present.
* **Dean's List Rule**: Candidates must maintain a GPA Above 3.5 alongside Attendance Above 80%.

## Reasoning Method Used
The platform leverages **Data-Driven Forward Chaining**. The reasoning process begins with raw user metrics, immediately deriving matching state configurations (e.g., converting a numeric 3.7 GPA into the string assertion `Above 3.5`). The production system then loops systematically through all conditional clauses, matching the derived states against each rule. This approach allows the system to discover all valid conclusions in a single pass.

## Project Structure
```
    APT3020-Reasoning-Inferencing-Lab/
    ├── README.md
    ├── reasoning_engine.py
    ├── knowledge_base.json
    ├── diagrams/
    │   └── inference_flow.png
    ├── screenshots/
    │   ├── test_case1.png
    │   ├── test_case2.png
    │   └── test_case3.png
    └── docs/
        └── explanation_report.pdf
```

## How to run the project
Ensure Python is installed
Place files in the correct structure
Run:
```
    python reasoning_engine.py

```
Enter required inputs when prompted 

## Sample input
- GPA: 3.6 
- Attendance: 
- 80 Disciplinary: 
- no Prerequisites: yes 
- Fees: no

