print("==================================================")
print("  Welcome to the university scholarship planner!")
print("==================================================")
print("")
TUITION_COST = int(input("Please tell me your annual tuition cost before any discounts: "))
MONTHLY_RENT = int(input("Please tell my your monthly rent: "))
TRANSPORTATION_COST = int(input("Please tell me you monthly  transport cost: "))
print("")
discount_1 = 999
while discount_1 > 100 or discount_1 < 0:
    discount_1 = int(input("Enter your scholarship discount in percentage: "))
    if discount_1 > 100 or discount_1 < 0:
        print("Discount should be between 0 and 100!")

final_tuition_cost = round(TUITION_COST - (TUITION_COST * (discount_1 / 100)), 2)
MONTHS_IN_YEAR = 12
monthly_cost_1 = round((final_tuition_cost / MONTHS_IN_YEAR) + MONTHLY_RENT + TRANSPORTATION_COST, 2)

student_name = input("Please enter your student name: ")
student_id = "STU-" + student_name[:3].upper() + "-2026"
print("Your Student ID:", student_id)
print("")

discount_2 = 999
while discount_2 > 100 or discount_2 < 0:
    discount_2 = int(input("Enter your second scholarship discount in percentage: "))
    if discount_2 > 100 or discount_2 < 0:
        print("Discount should be between 0 and 100!")

final_tuition_cost_2 = round(TUITION_COST - (TUITION_COST * (discount_2 / 100)), 2)
monthly_cost_2 = round((final_tuition_cost_2 / MONTHS_IN_YEAR) + MONTHLY_RENT + TRANSPORTATION_COST, 2)

best_case_cost = min(monthly_cost_1, monthly_cost_2)
backup_case_cost = max(monthly_cost_1, monthly_cost_2)
monthly_difference = round(backup_case_cost - best_case_cost, 2)

print("")
print("========================================")
print("               SUMMARY                  ")
print("========================================")
print(f"Student ID:             {student_id}")
print(f"Best-Case Monthly Cost: {best_case_cost:.2f}")
print(f"Backup Monthly Cost:    {backup_case_cost:.2f}")
print(f"Monthly Difference:     {monthly_difference:.2f}")
print("========================================")