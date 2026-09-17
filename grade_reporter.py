# grade_reporter.py

scores = [72, 45, 90, 61, 38]

passed_count = 0
failed_count = 0
total_score = 0

# Loop through every score in the list
for score in scores:
    total_score += score
    
    # Determine the grade using if / elif / else
    if score >= 80:
        grade = 'A'
    elif score >= 70:
        grade = 'B'
    elif score >= 50:
        grade = 'C'
    else:
        grade = 'F'
        
    print(f"Score: {score} -> Grade: {grade}")
    
    # Count passes (50 or more) and fails (below 50)
    if score >= 50:
        passed_count += 1
    else:
        failed_count += 1

# Calculate the average and round to one decimal place
average = total_score / len(scores)
rounded_average = round(average, 1)

print("\n--- Summary Report ---")
print(f"Number of learners passed: {passed_count}")
print(f"Number of learners failed: {failed_count}")
print(f"Average score: {rounded_average}")