from datetime import timedelta, time, datetime


def check_pump(start, end, count, pump_work, is_day):
    if is_day:
        difference = (timedelta(hours=int(end[:2]), minutes=int(end[3:5])) - timedelta(hours=int(start[:2]), minutes=int(start[3:5]))).seconds
        t = time(hour=int(start[:2]), minute=int(start[3:5]))
    else:
        difference = (timedelta(hours=int(start[:2]), minutes=int(start[3:5])) - timedelta(hours=int(end[:2]), minutes=int(end[3:5]))).seconds 
        t = time(hour=int(end[:2]), minute=int(end[3:5]))  

    delay = int((difference / 60) / count)

    d = datetime.now().date()
    if not is_day:
        new_day = datetime.combine(d, time(hour=int(end[:2]), minute=int(end[3:5])))
        if new_day > datetime.now():
            d = d - timedelta(days=1)

    combo = datetime.combine(d, t)
    array_result = []
    for array in range(count):
        array = []
        array.append(combo)
        array.append(combo + timedelta(minutes=int(pump_work)))
        array_result.append(array)
        combo = combo + timedelta(minutes=delay)
        
    return array_result