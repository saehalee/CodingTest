h, m = list(map(int,input().split()))
time=int(input())
h += int(time/60)
m += time%60

if(m > 59):
  h += 1
  m -= 60
if(h > 23): 
  h -= 24
print(h, m)