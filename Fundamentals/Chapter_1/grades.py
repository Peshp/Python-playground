grade = float(input())

def solve(grade):
    if grade >= 2.0 and grade <= 2.99:
        return "Fail"
    elif grade >= 3.00 and grade <= 3.49:
        return "Poor"
    elif grade >= 3.5 and grade <= 4.49:
        return "Good"
    elif grade >= 4.5 and grade <= 5.49:
        return "Very good"
    elif grade >= 5.5 and grade <= 6.0:
        return "Excellent"
    
print(solve(grade))
