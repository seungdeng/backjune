hour , minute , sec = map(int,input().split())
time = int(input())

hour += time//3600
time = time%3600
minute += time//60
time = time%60
sec += time

if sec>=60:
    minute += sec//60
    sec= sec%60
if minute>=60:
    hour += minute//60
    minute = minute%60
hour %= 24
print(hour,end=' ')
print(minute,end=' ')
print(sec)