import datetime
# year, month, day = (int(i) for i in input().split())
input_time = datetime.date(*[int(item) for item in input().split()])
# print(input_time, input_time.year, input_time.day, input_time.month)
input_delta = int(input())
result_time = input_time + datetime.timedelta(days = input_delta)
print(result_time)


# from datetime import date, timedelta

# data = date(*(map(int, input().split()))) + timedelta(int(input()))

# print(data.year, data.month, data.day)