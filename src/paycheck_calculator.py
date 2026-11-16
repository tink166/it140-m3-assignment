# Get input from user

Input:
    hours_worked_str = input("Enter the number of hours worked this week: ")
    try:
        hours_worked = float(hours_worked_str)
    except ValueError:
        print("Invalid input. Please enter a numeric value for hours worked.")
        return

Process:
    Calculate regular and overtime pay based on hours worked, determine total weekly earnings, and handle invalid input.

Output:
Hours worked: 45  
Regular pay (40 hrs × $20/hr): $80000  
Overtime pay (5 hrs × $30/hr): $150.00  
Total weekly earnings: $950.00

Typical usage example:  
Hours worked: 42  
Regular pay (40 hrs × $20/hr): $800.00  
Overtime pay (2 hrs × $30/hr): $60.00  
Total weekly earnings: $860.00: Replace with an original hours-worked input example.
    
"Hours worked: 38  
Regular pay (38 hrs × $20/hr): $760.00  
Overtime pay (0 hrs × $30/hr): $0.00  
Total weekly earnings: $760.00

# === Constants ===
REGULAR_RATE = 20
OVERTIME_RATE = 30
REGULAR_HOURS_LIMIT = 40


# === Main Function ===
def main() -> None:
    """Run the optional paycheck calculator practice program."""

ReplHours worked: 44  
Regular pay (40 hrs × $20/hr): $800.00  
Overtime pay (4 hrs × $30/hr): $120.00  
Total weekly earnings: $920.00

Hours worked: 50  
Regular pay (40 hrs × $20/hr): $800.00  
Overtime pay (10 hrs × $30/hr): $300.00  
Total weekly earnings: $1,100.00

print(f"Total weekly earnings: ${hours_worked * REGULAR_RATE if hours_worked <= REGULAR_HOURS_LIMIT else (REGULAR_HOURS_LIMIT * REGULAR_RATE + (hours_worked - REGULAR_HOURS_LIMIT) * OVERTIME_RATE):.2f}")


# === Main Guard ===
if __name__ == "__main__":
    main()


# === References ===
