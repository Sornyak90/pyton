"""Functions for organizing and calculating student exam scores."""


def round_scores(student_scores):
    return [round(num) for num in student_scores]


def count_failed_students(student_scores):
    return sum(1 for x in student_scores if x <= 40)
    


def above_threshold(student_scores, threshold):
    return [x for x in student_scores if x >= threshold]


def letter_grades(highest):
    a = 41
    b = int((highest - 40) / 4)
    return [a + i*b for i in range(4)]


def student_ranking(student_scores, student_names):
    return [f"{i+1}. {student_names[i]}: {student_scores[i]}" for i in range(len(student_scores))] 


def perfect_score(student_info):
    return next((bal for bal in student_info if bal[1] == 100), [])
