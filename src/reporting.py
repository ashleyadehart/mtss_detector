from __future__ import annotations
import pandas as pd


def save_report(df: pd.DataFrame, output_csv: str) -> None:
    df.to_csv(output_csv, index=False)


def save_summary(df: pd.DataFrame, output_md: str) -> None:
    tier_counts = df["tier"].value_counts().sort_index()
    tier_pct = (tier_counts / len(df) * 100).round(1)

    # explode reason codes
    reasons = (
        df.assign(reason=df["reason_codes"].str.split("|"))
          .explode("reason")
    )
    reasons = reasons[reasons["reason"].notna() & (reasons["reason"] != "none")]
    reason_counts = reasons["reason"].value_counts()

    top_high = df[df["tier"] == 3].head(10)

    lines = []
    lines.append("# MTSS Detector Summary\n")
    lines.append(f"Total students: **{len(df)}**\n")

    lines.append("## Tier Distribution\n")
    for t in [1, 2, 3]:
        c = int(tier_counts.get(t, 0))
        p = float(tier_pct.get(t, 0.0))
        lines.append(f"- Tier {t}: **{c}** students ({p}%)")

    lines.append("\n## Top Reason Codes\n")
    if len(reason_counts) == 0:
        lines.append("- (none)")
    else:
        for reason, count in reason_counts.head(10).items():
            lines.append(f"- {reason}: **{int(count)}**")

    lines.append("\n## Top Tier 3 Students (first 10)\n")
    if len(top_high) == 0:
        lines.append("- (none)")
    else:
        for _, r in top_high.iterrows():
            lines.append(f"- {r['student_name']} (Reasons: {r['reason_codes']})")

    with open(output_md, "w", encoding="utf-8") as f:
        f.write("\n".join(lines) + "\n")
