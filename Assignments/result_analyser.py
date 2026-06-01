import pandas as pd

# Read Excel files
questions = pd.read_excel("Questions.xlsx")
responses = pd.read_excel("Student_Responses.xlsx")

# Create answer key and subject mapping
answer_key = {}
subject_map = {}

for _, row in questions.iterrows():

    q_no = f"Q{row['Q.No']}"

    answer_key[q_no] = row["Correct Answer"]
    subject_map[q_no] = row["Subject"]

# Process each student

for _, student in responses.iterrows():

    name = student["Name"]

    correct = 0
    total = len(answer_key)

    subject_correct = {}
    subject_total = {}

    for q, correct_answer in answer_key.items():

        subject = subject_map[q]

        if subject not in subject_total:
            subject_total[subject] = 0

        if subject not in subject_correct:
            subject_correct[subject] = 0

        subject_total[subject] += 1

        if student[q] == correct_answer:

            correct += 1
            subject_correct[subject] += 1

    percentage = (correct / total) * 100

    # Grade calculation

    if percentage >= 90:
        grade = "A"

    elif percentage >= 75:
        grade = "B"

    elif percentage >= 60:
        grade = "C"

    else:
        grade = "D"

    print("\n")
    print("=" * 40)

    print("Student:", name)
    print("Total Questions:", total)
    print("Correct Answers:", correct)
    print("Percentage:", round(percentage, 2), "%")
    print("Grade:", grade)

    print("\nSubject-wise Performance")

    subject_scores = {}

    for subject in subject_total:

        score = (
            subject_correct[subject]
            / subject_total[subject]
        ) * 100

        subject_scores[subject] = score

        print(
            subject,
            ":",
            round(score, 2),
            "%"
        )

    best_subject = max(
        subject_scores,
        key=subject_scores.get
    )

    weak_subject = min(
        subject_scores,
        key=subject_scores.get
    )

    print("\nStrongest Subject:", best_subject)
    print("Needs Improvement:", weak_subject)
