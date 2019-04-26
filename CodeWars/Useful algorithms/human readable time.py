def format_duration(seconds):
    if seconds == 0: return 'now'
    divisors = [60, 60, 24, 365]
    lengths = ['seconds', 'minutes', 'hours', 'days', 'years']
    time = [seconds]
    result = ''
    for x in divisors:
        time.append(time[-1] // x)
        time[-2] %= x
    index = 0
    while index <= len(time) -1:
        if time[index] == 0:
            time.pop(index)
            lengths.pop(index)
        elif time[index] == 1:
            time[index] = str(time[index]) + ' ' + lengths[index][:-1]
            index += 1
        else:
            time[index] = str(time[index]) + ' ' + lengths[index]
            index += 1
    index = len(time) - 1
    while index >= 0:
        if index == len(time) - 1:
            result += time[index]
            index -= 1
        elif index != 0:
            result += ', ' + time[index]
            index -= 1
        else:
            result += ' and ' + time[index]
            break
    return str(seconds) + ' seconds is ' + result

print(format_duration(343334))