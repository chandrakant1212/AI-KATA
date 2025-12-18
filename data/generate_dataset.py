import pandas as pd
import random

rows = []

num_students = 120
chapters = [1, 2, 3]

for i in range(1, num_students + 1):
    student_id = f"S{i:03d}"
    course_id = "C01"

    base_score = random.randint(55, 90)
    base_time = random.randint(20, 40)

    dropped = False

    for ch in chapters:
        score = max(40, base_score - ch * random.randint(2, 6))
        time_spent = base_time + ch * random.randint(5, 15)

        if score < 55:
            dropped = True

        completion_status = 0 if dropped else 1

        rows.append([
            student_id,
            course_id,
            ch,
            time_spent,
            score,
            completion_status
        ])

df = pd.DataFrame(rows, columns=[
    "student_id",
    "course_id",
    "chapter_order",
    "time_spent",
    "score",
    "completion_status"
])

df.to_csv("sample_large_learning_dataset_120.csv", index=False)
print("Dataset generated successfully.")
