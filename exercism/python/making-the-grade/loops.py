"""Functions for organizing and calculating student exam scores."""


def round_scores(student_scores):
    return [round(num) for num in student_scores]


def count_failed_students(student_scores):
    return sum(1 for bal in student_scores if bal <= 40)
    


def above_threshold(student_scores, threshold):
    return [bal for bal in student_scores if bal >= threshold]


def letter_grades(highest):
    left = 41
    right = int((highest - 40) / 4)
    return [left + num*right for num in range(4)]


def student_ranking(student_scores, student_names):
    return [f"{num+1}. {student_names[num]}: {student_scores[num]}" for num in range(len(student_scores))] 


def perfect_score(student_info):
    return next((bal for bal in student_info if bal[1] == 100), [])
