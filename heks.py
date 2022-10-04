def maxPresentations(scheduleStart, scheduleEnd):
    start_time = sorted(scheduleStart)
    end_time = sorted(scheduleEnd)

    rooms = 0
    max_rooms = 0

    start = 0
    end = 0

    while start < len(start_time):
        if start_time[start] < end_time[end]:
            rooms += 1
            start += 1
            max_rooms = max(max_rooms, rooms)
        else:
            rooms -= 1
            end += 1
    return max_rooms


schedule([1, 1, 2], [3, 2, 4])
