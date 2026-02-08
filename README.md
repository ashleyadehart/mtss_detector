# MTSS Detector

## Project Overview
The **MTSS Detector** is a Python-based automation tool designed to support **Multi-Tiered Systems of Support (MTSS)** by identifying students who may require additional academic or engagement-based interventions.

The tool analyzes commonly available student data — attendance, grades, and assignment completion — and assigns students to **MTSS Tier 1, Tier 2, or Tier 3** using transparent, rules-based logic.  
Its goal is to help educators move from reactive to **proactive, data-informed decision making**.

---

## Problem Statement
Schools collect large amounts of student data, but often struggle to:
- Consistently identify students needing intervention
- Apply uniform criteria across teams and classrooms
- Review data efficiently at scale
- Align data review practices with MTSS/RTI frameworks

Manual review is time-intensive and prone to inconsistency.  
This project automates the **initial screening process**, allowing educators to focus on interpretation and intervention rather than data processing.

---

## MTSS Framework Alignment

### Tier 1: Universal Support (All Students)
**Focus:** High-quality core instruction and proactive supports  
**Goal:** Ensure 80–85% of students succeed without additional intervention  

Students in Tier 1 demonstrate strong attendance, satisfactory academic performance, and consistent assignment completion.

---

### Tier 2: Targeted Intervention (Some Students)
**Focus:** Moderate, targeted academic or engagement supports  
**Goal:** Address emerging concerns and return students to Tier 1  

Students in Tier 2 may show declining attendance, borderline grades, or inconsistent assignment completion.

---

### Tier 3: Intensive Intervention (Few Students)
**Focus:** Intensive, individualized academic or behavioral supports  
**Goal:** Remediate severe or chronic challenges  

Students in Tier 3 exhibit multiple high-risk indicators requiring urgent, individualized intervention.

---

## How the Automation Works
1. Reads student data from a CSV file
2. Calculates attendance and assignment completion rates
3. Evaluates each indicator against MTSS-aligned thresholds
4. Assigns each student to Tier 1, Tier 2, or Tier 3
5. Generates reason codes explaining tier placement
6. Outputs structured reports for review

All logic is **transparent, auditable, and explainable**.

---

## Input Data Requirements
The input CSV must include the following columns:

- `student_id`
- `student_name`
- `days_present`
- `days_enrolled`
- `current_grade_percent`
- `assignments_submitted`
- `assignments_assigned`

---

## Outputs

### MTSS Report (CSV)
Generated in the `/outputs` directory:
- Attendance rate
- Grade percentage
- Assignment completion rate
- MTSS Tier
- Tier description
- Reason codes

### Summary Report (Markdown)
Also generated in `/outputs`:
- Total student count
- Tier distribution percentages
- Most common risk indicators
- List of highest-need Tier 3 students

Generated output files are not committed to version control.

---

## Project Structure
```text
mtss_detector/
├─ data/
│  └─ input/
│     └─ students.csv
├─ outputs/
│  ├─ mtss_report.csv
│  ├─ summary.md
├─ src/
│  ├─ __init__.py
│  ├─ cli.py
│  ├─ detector.py
│  ├─ rules.py
│  ├─ io_utils.py
│  └─ reporting.py
├─ tests/
│  ├─ test_rules.py
│  └─ test_detector.py
├─ requirements.txt
├─ pytest.ini
└─ README.md
```

# MTSS Tiering CLI Tool

## Installation

### Prerequisites

- Python 3.10+
- pip

### Setup

```bash
python -m venv .venv
source .venv/Scripts/activate
pip install -r requirements.txt
```

---

## Running the Tool

From the project root:

```bash
python -m src.cli \
  --input data/input/students.csv \
  --output outputs/mtss_report.csv \
  --summary outputs/summary.md
```

---

## Testing

Unit tests validate tier logic and core pipeline behavior.

Run tests with:

```bash
pytest
```

---

## Configuration Philosophy

Thresholds are currently hard-coded to ensure clarity and auditability.

Future versions may allow JSON or YAML configuration, but defaults prioritize interpretability over complexity.

---

## Assumptions & Limitations

- Data is assumed to be accurate and up to date
- Tool does not account for qualitative context
- Does not replace MTSS team decision-making

---

## Data Ethics & Privacy

- No personally identifiable data is stored beyond runtime
- Outputs can be anonymized if needed
- Tool supports responsible, transparent data use
- Designed to reduce bias through consistent rules

---

## Why This Project Matters

This project demonstrates:

- Applied data analytics in education
- MTSS-aligned decision support
- Ethical, transparent automation
- Strong Python fundamentals (CLI, testing, reporting)
- Real-world problem solving

---

## Future Enhancements

- Configurable thresholds via JSON/YAML
- Subject-level academic analysis
- Risk trend tracking over time
- Dashboard-ready exports
- Student ID anonymization
- SIS integration

---

## Disclaimer

This tool is for educational decision support only. All intervention decisions should be made by qualified professionals using professional judgment.
