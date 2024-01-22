week_days = [
    "Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"
]
def solution(S, K):
    start_index = week_days.index(S)
    movement = K % (len(week_days))
    end_index = (start_index + movement) % len(week_days)
    return week_days[end_index]