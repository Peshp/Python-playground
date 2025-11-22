minutes = int(input())
seconds = int(input())
metres = float(input())
seconds_hundred = int(input())

error = 0
if metres > 120:
    error = metres / 120 * 2.5

result = seconds_hundred * (metres / 100) - error
control_time = minutes * 60 + seconds

if result < control_time:
    print(f"His time is {result}")
else:
    print(control_time - result)