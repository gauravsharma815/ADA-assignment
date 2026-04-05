Task : Recurrence

call_count = 0

def T1(n):
global call_count
call_count += 1
if n <= 1:
return 1
return T1(n//2) + n

def T2(n):
global call_count
call_count += 1
if n <= 1:
return 1
return 2*T2(n//2) + n

call_count = 0
print("T(n)=T(n/2)+n:", T1(16), "Calls:", call_count)

call_count = 0
print("T(n)=2T(n/2)+n:", T2(16), "Calls:", call_count)
