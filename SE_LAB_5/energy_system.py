"""Manage energy meter readings, billing, and data persistence."""

import json
from datetime import datetime

RATE_TIER_1 = 3.5
RATE_TIER_2 = 5.0
RATE_TIER_3 = 7.5
SPIKE_LIMIT = 500


def record_reading(meter_id, units, meters, history=None):
    """Record a meter reading and update cumulative units."""
    if history is None:
        history = []
    history.append((meter_id, units, str(datetime.now())))
    meters[meter_id] = meters.get(meter_id, 0) + units
    return history


def compute_bill(meter_id, tier_rates, meters):
    """Calculate the bill using tiered rates."""
    units = meters[meter_id]
    if units <= 100:
        return units * tier_rates[0]
    if units <= 300:
        return 100 * tier_rates[0] + (units - 100) * tier_rates[1]
    return (
        100 * tier_rates[0]
        + 200 * tier_rates[1]
        + (units - 300) * tier_rates[2]
    )


def raise_rates(rates, percent):
    """Increase all tier rates by the specified percentage."""
    factor = 1 + percent / 100
    return tuple(rate * factor for rate in rates)


def flag_spikes(meters):
    """Return meter IDs whose cumulative units exceed the spike limit."""
    return [
        meter_id
        for meter_id, units in meters.items()
        if units > SPIKE_LIMIT
    ]


def load_meter_data(file="meters.json"):
    """Load meter data from a JSON file."""
    try:
        with open(file, "r", encoding="utf-8") as f:
            return json.load(f)
    except (OSError, json.JSONDecodeError):
        return {}


def save_meter_data(meters, file="meters.json"):
    """Save meter data to a JSON file."""
    with open(file, "w", encoding="utf-8") as f:
        json.dump(meters, f)


def main():
    """Run the energy meter billing demonstration."""
    meters = {}
    history = []
    rates = (RATE_TIER_1, RATE_TIER_2, RATE_TIER_3)

    record_reading("M-01", 120, meters, history)
    record_reading("M-02", 640, meters, history)
    record_reading("M-03", -50, meters, history)

    print("Readings stored so far:", len(history))

    rates = raise_rates(rates, 10)

    print(f"Bill M-01: {compute_bill('M-01', rates, meters):.2f}")
    print(f"Bill M-03: {compute_bill('M-03', rates, meters):.2f}")
    print("Spikes:", flag_spikes(meters))

    adjustment = input(
        "Extra units for M-01 (Enter for 0): "
    ) or "0"

    try:
        adjustment = int(adjustment)
        record_reading("M-01", adjustment, meters, history)
    except ValueError:
        print("Invalid input. Please enter a whole number.")

    save_meter_data(meters)
    meters = load_meter_data()

    print(
        f"Bill M-01 after reload: "
        f"{compute_bill('M-01', rates, meters):.2f}"
    )


if __name__ == "__main__":
    main()
