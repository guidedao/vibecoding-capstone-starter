import argparse


TASKS = [
    {"title": "написать спеку", "done": True},
    {"title": "ревью диффа", "done": False},
]


def list_tasks():
    for task in TASKS:
        mark = "x" if task["done"] else " "
        print(f"[{mark}] {task['title']}")


def main(argv=None):
    parser = argparse.ArgumentParser()
    sub = parser.add_subparsers(dest="command")
    sub.add_parser("list")
    args = parser.parse_args(argv)

    if args.command == "list":
        list_tasks()
    else:
        parser.print_help()


if __name__ == "__main__":
    main()

