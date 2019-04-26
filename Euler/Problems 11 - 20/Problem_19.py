from datetime import datetime

def Problem_19():
    return sum(1 if datetime(x, y, 1).weekday() == 6 else 0 for y in range(1, 13) for x in range(1901, 2001))