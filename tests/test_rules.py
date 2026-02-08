from src.rules import assign_tier

def test_tier1_student():
    tier, reasons = assign_tier(attendance_rate=0.95, grade_percent=85, completion_rate=0.90)
    assert tier == 1
    assert reasons == []

def test_tier3_multiple_indicators():
    tier, reasons = assign_tier(attendance_rate=0.70, grade_percent=60, completion_rate=0.50)
    assert tier == 3
    assert "attendance_tier3" in reasons
    assert "grade_tier3" in reasons
    assert "completion_tier3" in reasons
