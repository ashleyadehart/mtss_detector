from __future__ import annotations
import argparse
import os

from src.detector import run_detector
from src.reporting import save_report, save_summary


def main() -> None:
    parser = argparse.ArgumentParser(description="MTSS Early Warning Student Risk Detector")
    parser.add_argument("--input", required=True, help="Path to input CSV")
    parser.add_argument("--output", default="outputs/mtss_reportS.csv", help="Path to output CSV")
    parser.add_argument("--summary", default="outputs/summary.md", help="Path to output markdown summary")
    args = parser.parse_args()

    os.makedirs(os.path.dirname(args.output), exist_ok=True)

    df = run_detector(args.input)
    save_report(df, args.output)
    save_summary(df, args.summary)

    print(f"Saved: {args.output}")
    print(f"Saved: {args.summary}")


if __name__ == "__main__":
    main()
