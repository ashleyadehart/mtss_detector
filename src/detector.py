from __future__ import annotations
import pandas as pd

from src.rules import assign_tier

REQUIRED_COLUMNS = [
    "student_id",
    "student_name",
    "days_present",
    "days_enrolled",
    "current_grade_percent",
    "assignments_submitted",
    "assignments_assigned",
]


def compute_rates(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()

    # Avoid division by zero
    df["attendance_rate"] = df["days_present"] / df["days_enrolled"].replace(0, pd.NA)
    df["completion_rate"] = df["assignments_submitted"] / df["assignments_assigned"].replace(0, pd.NA)

    return df


def apply_tiers(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()

    tiers = []
    reasons_joined = []

    for _, row in df.iterrows():
        tier, reasons = assign_tier(
            attendance_rate=float(row["attendance_rate"]),
            grade_percent=float(row["current_grade_percent"]),
            completion_rate=float(row["completion_rate"]),
        )
        tiers.append(tier)
        reasons_joined.append("|".join(reasons) if reasons else "none")

    df["tier"] = tiers
    df["tier_label"] = df["tier"].map({
        1: "Tier 1: Universal Support",
        2: "Tier 2: Targeted Intervention",
        3: "Tier 3: Intensive Intervention",
    })
    df["reason_codes"] = reasons_joined

    return df


def run_detector(input_csv: str) -> pd.DataFrame:
    df = pd.read_csv(input_csv)

    missing = [c for c in REQUIRED_COLUMNS if c not in df.columns]
    if missing:
        raise ValueError(f"Missing required columns: {missing}")

    df = compute_rates(df)
    df = apply_tiers(df)

    # Order columns nicely
    output_cols = [
        "student_id",
        "student_name",
        "attendance_rate",
        "current_grade_percent",
        "completion_rate",
        "tier",
        "tier_label",
        "reason_codes",
    ]
    return df[output_cols].sort_values(["tier", "student_name"], ascending=[False, True])
