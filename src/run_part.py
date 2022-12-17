import argparse
import subprocess


def create_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Helper to bootstrap files for problems"
    )
    parser.add_argument("day", type=int, help="Day to run")
    parser.add_argument("part", type=str, help="Part to run (a or b)")
    parser.add_argument(
        "-d", "--dryrun", action="store_true", help="Do NOT attempt to submit"
    )
    parser.add_argument(
        "-f",
        "--force",
        action="store_true",
        help="Force execution of long-running solutions",
    )
    return parser


if __name__ == "__main__":
    args = create_parser().parse_args()
    command = f"pipenv run python -m src.days.day{args.day:02d}.{args.part}{' --dryrun' if args.dryrun else ''}{' --force' if args.force else ''}"
    subprocess.run(command)
