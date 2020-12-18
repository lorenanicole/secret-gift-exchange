# Secret Gift Exchange Name Drawer

Python 3.7+ script to:

- Generate name pairings
- Output pairings to csv
- Generate email messages to pairings

## Usage

1. Load a `names.csv` file with headers `adhs,Email Address,Name,Email,"Address (street, city, country and zip code)",Please provide some choices of things you want to receive` into the project root
2. Run `python secret_exchange_pairings.py`

The pairings will be available in `secret_exchange_pairings.csv` and messages at `messages.txt`.