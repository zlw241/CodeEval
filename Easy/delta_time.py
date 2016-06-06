


def seconds_to_timestamp(seconds):
    m, s = divmod(seconds, 60)
    h, m = divmod(m, 60)
    return "%02d:%02d:%02d" % (h,m,s)


def time_delta(time):
    first, second = time.split(' ')
    first_time = first.split(':')
    second_time = second.split(':')
    first_hours, first_minutes, first_seconds = [int(t) for t in first_time]
    second_hours, second_minutes, second_seconds = [int(t) for t in second_time]
    first_total_seconds = (first_hours*60*60) + (first_minutes*60) + first_seconds
    second_total_seconds = (second_hours*60*60) + (second_minutes*60) + second_seconds
    return seconds_to_timestamp(abs(second_total_seconds-first_total_seconds))


test_cases = ["14:01:57 12:47:11", "13:09:42 22:16:15", "08:08:06 08:38:28", "23:35:07 02:49:59", "14:31:45 14:46:56"]

for test in test_cases:
    print(time_delta(test))





