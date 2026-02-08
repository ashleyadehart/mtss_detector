from __future__ import annotations

def indicator_band(value: float, t3_lt: float, t2_lt: float) -> str:
    """
    Return 'T1', 'T2', or 'T3' based on cutoffs.
    - T3 if value < t3_lt
    - T2 if value < t2_lt
    - else T1
    """
    if value < t3_lt:
        return "T3"
    if value < t2_lt:
        return "T2"
    return "T1"


def assign_tier(attendance_rate: float, grade_percent: float, completion_rate: float) -> tuple[int, list[str]]:
    """
    Returns (tier_number, reason_codes)

    Threshold bands (defaults):
    Attendance: T3 < 0.80, T2 < 0.90
    Grade:      T3 < 65,   T2 < 75
    Completion: T3 < 0.60, T2 < 0.80

    Combination rules:
    Tier 3 if:
      - 2+ indicators in T3, OR
      - grade is T3 AND (attendance is T2/T3 OR completion is T2/T3)

    Tier 2 if:
      - 1 indicator in T3, OR
      - 2+ indicators in T2

    Else Tier 1
    """
    reasons: list[str] = []

    a_band = indicator_band(attendance_rate, t3_lt=0.80, t2_lt=0.90)
    g_band = indicator_band(grade_percent,    t3_lt=65.0, t2_lt=75.0)
    c_band = indicator_band(completion_rate,  t3_lt=0.60, t2_lt=0.80)

    # Reason codes (specific)
    if a_band == "T2":
        reasons.append("attendance_tier2")
    elif a_band == "T3":
        reasons.append("attendance_tier3")

    if g_band == "T2":
        reasons.append("grade_tier2")
    elif g_band == "T3":
        reasons.append("grade_tier3")

    if c_band == "T2":
        reasons.append("completion_tier2")
    elif c_band == "T3":
        reasons.append("completion_tier3")

    t3_count = sum(b == "T3" for b in (a_band, g_band, c_band))
    t2_count = sum(b == "T2" for b in (a_band, g_band, c_band))

    # Tier decision
    if t3_count >= 2:
        return 3, reasons
    if g_band == "T3" and (a_band in ("T2", "T3") or c_band in ("T2", "T3")):
        return 3, reasons
    if t3_count == 1:
        return 2, reasons
    if t2_count >= 2:
        return 2, reasons
    return 1, reasons
