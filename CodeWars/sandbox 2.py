def solution(Y, A, B, W):
    days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
    month_lengths = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    leap_year = Y % 4 == 0
    weeks = 0
    start_month_index = months.index(A)
    end_month_index = months.index(B)
    current_month_index = months.index(A)
    start_month_first_day = days.index(W)
    for x in range(0, start_month_index):
        if leap_year: start_month_first_day += (month_lengths[x] - 27)
        else: start_month_first_day += (month_lengths[x] - 28)
        start_month_first_day %= 7
    if start_month_first_day == 0: current_date = 0
    else: current_date = 1 + (7 - start_month_first_day)
    current_day = 0
    while current_month_index < end_month_index:
        while current_date + 7 < month_lengths[current_month_index]:
            weeks += 1
            current_date += 7
        if current_month_index + 1 <= end_month_index:
            current_month_index += 1
            current_date = (current_date + 7) % month_lengths[current_month_index - 1]
            weeks += 1
    return weeks

print(solution(2014, "April", "May", "Wednesday"))
