def validate_interval(a, b):
    if a >= b:
        raise ValueError(f"Invalid interval: a ({a}) must be less than b ({b}).")
