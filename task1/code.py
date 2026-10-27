
students = []

n = int(input("Enter number of students: "))

for i in range(n):
    print("\nEnter details of student", i + 1)

    name = input("Name: ")
    aggregate = float(input("Aggregate marks (%): "))

    print("Enter marks of 3 subjects:")
    s1 = float(input("Subject 1: "))
    s2 = float(input("Subject 2: "))
    s3 = float(input("Subject 3: "))

    attendance = float(input("Attendance (%): "))
    income = float(input("Annual family income (Rs.): "))

    eligible = (
        aggregate >= 75 and
        min(s1, s2, s3) >= 40 and
        attendance >= 75 and
        income <= 250000
    )

    if eligible:
        students.append({
            "name": name,
            "aggregate": aggregate,
            "attendance": attendance,
            "income": income
        })

# Rank by aggregate, attendance, income, then name
students.sort(
    key=lambda x: (
        -x["aggregate"],
        -x["attendance"],
        x["income"],
        x["name"].lower()
    )
)

print("\n--- SCHOLARSHIP RANK LIST ---")

if students:
    for rank, student in enumerate(students, start=1):
        print(
            rank, student["name"],
            "| Aggregate:", student["aggregate"],
            "| Attendance:", student["attendance"],
            "| Income:", student["income"]
        )
else:
    print("No eligible students.")

print("\nTotal eligible students:", len(students))

