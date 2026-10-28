# Cloud Resource Inventory

A small, local Python project for practicing programming fundamentals with a cloud-themed example. The inventory is sample data; it does not connect to a cloud account or create billable resources.

## Run it

Requires Python 3.9 or newer. From this folder, run:

```bash
python main.py list
python main.py list --environment production
python main.py summary
```

Run the tests with:

```bash
python -m unittest -v
```

## What you will practice

- Lists and dictionaries for representing resource records
- Functions, filtering, loops, and calculating totals
- Reading structured JSON data from a file
- Command-line arguments with `argparse`
- Automated checks with `unittest`

## Learning path

1. Change a resource in `resources.json` and predict how the summary changes.
2. Add a resource field such as `region`, then display it in the list.
3. Add a `--type` filter and write a test for it.
4. Add a warning when the total cost is above a budget supplied on the command line.
5. Save a report to a file, then compare the inventory with another JSON file.
6. Once these feel comfortable, choose a cloud provider and learn its SDK using a test account and its cost controls. Keep credentials out of source code.
