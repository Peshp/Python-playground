country = input()
type_stick = input()

hardnes = 0
trying = 0

if country == "Russia":
    if type_stick == "ribbon":
        hardnes = 9.1
        trying = 9.4
    if type_stick == "hoop":
        hardnes = 9.3
        trying = 9.8
    if type_stick == "rope":
        hardnes = 9.6
        trying = 9
elif country == "Bulgaria":
    if type_stick == "ribbon":
        hardnes = 9.6
        trying = 9.4
    if type_stick == "hoop":
        hardnes = 9.55
        trying = 9.75
    if type_stick == "rope":
        hardnes = 9.6
        trying = 9.4
elif country == "Italy":
    if type_stick == "ribbon":
        hardnes = 9.2
        trying = 9.5
    if type_stick == "hoop":
        hardnes = 9.45
        trying = 9.35
    if type_stick == "rope":
        hardnes = 9.7
        trying = 9.15

final_grade = hardnes + trying
if final_grade < 20:
    print(f"The team of {country} get {final_grade:.3f} on {type_stick}.")
    print(f"{((20 - final_grade) / 20) * 100}")