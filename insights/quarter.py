def to_quarter(month: int):
    if month < 1 or month > 12:
        raise Exception
    return f"Q{((month - 1) // 3) + 1}"
