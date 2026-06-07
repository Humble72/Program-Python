import argparse
import sys
from logic.calculator import calculate_fuel_cost


def main():
    parser = argparse.ArgumentParser(description="Kalkulator kosztów paliwa (CLI).")
    parser.add_argument(
        "-l", "--liters", type=float, required=True, help="Ilość zatankowanego paliwa w litrach"
    )
    parser.add_argument("-p", "--price", type=float, required=True, help="Cena za jeden litr w PLN")

    args = parser.parse_args()

    try:
        total_cost = calculate_fuel_cost(args.liters, args.price)
        print(f"Całkowity koszt: {total_cost:.2f} PLN")
    except ValueError as e:
        print(f"Błąd: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
