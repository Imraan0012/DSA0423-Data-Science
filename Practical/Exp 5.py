import numpy as np

student_scores = np.random.randint(50, 100, size=(15, 4))  # sample scores

avg_scores = student_scores.mean(axis=0)

subjects = ['Math', 'Science', 'English', 'History']
best_subject = subjects[np.argmax(avg_scores)]

print("Average Scores per Subject:", dict(zip(subjects, avg_scores)))
print("Subject with Highest Average:", best_subject)