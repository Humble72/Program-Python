def calculate_fuel_cost(liters: float, price_per_liter: float) -> float:

    if liters < 0 or price_per_liter < 0:
        raise ValueError("Ilość litrów i cena nie mogą być ujemne.")

    return round(liters * price_per_liter, 2)
