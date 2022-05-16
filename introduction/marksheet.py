# MARKSHEET OF STUDENT
ACTIVITES_WEIGHTAGE = 30.0
SPORTS_WEIGHTAGE = 20.0
EXAMS_WEIGHTAGE = 50.0
EXAMS_TOTAL = 200.0
ACTIVITIES_TOTAL = 60.0
SPORTS_TOTAL = 50.0

exams_score1 = float(input('\nEnter the marks in 1st examination(out of 100) : '))
exams_score2 = float(input('\nEnter the marks in 2nd examination(out of 100) : '))
sports_score = float(input('\nEnter the score obtained in sports activities (out of 50) : '))

activities_score1 = float(input('\nEnter the marks in 1st activity(out of 20) : '))
activities_score2 = float(input('\nEnter the marks in 2st activity(out of 20) : '))
activities_score3 = float(input('\nEnter the marks in 3st activity(out of 20) : '))

exam_total = exams_score1 + exams_score2 
activities_total = activities_score1 + activities_score2 + activities_score3

exam_percent = float(exam_total * EXAMS_WEIGHTAGE / EXAMS_TOTAL)
sports_percent = float(sports_score * SPORTS_WEIGHTAGE / SPORTS_TOTAL)
activities_percent = float(activities_total * ACTIVITES_WEIGHTAGE / ACTIVITIES_TOTAL)
total_percent = exam_percent + sports_percent + activities_percent

print('\n********************RESULTS********************')
print('\nTotal percent in examnination : ', exam_percent)
print('\nTotal percent in sports : ', sports_percent)
print('\nTotal percent in activities : ', activities_percent)
print('\n----------------------------------------------')
print('\nTotal percentage\n', total_percent)