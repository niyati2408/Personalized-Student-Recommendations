import requests
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from tabulate import tabulate

quiz_endpoint = "https://www.jsonkeeper.com/b/LLQT"
quiz_submission = "https://api.jsonserve.com/rJvd7g"
historical_endpoint = "https://api.jsonserve.com/XgAgFJ"

def fetch_data(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.json()
    except Exception as e:
        print(f"Error fetching data from {url}: {e}")
        return None

quiz_data = fetch_data(quiz_endpoint)
submission_data = fetch_data(quiz_submission)
historical_data = fetch_data(historical_endpoint)

if quiz_data is None or submission_data is None or historical_data is None:
    print("Data fetching failed.")
    exit()

quiz_df = pd.DataFrame(quiz_data)
submission_df = pd.json_normalize(submission_data)
historical_df = pd.DataFrame(historical_data)

merged_df = pd.merge(submission_df, historical_df, on='user_id', how='left')

topic_performance = merged_df.groupby('quiz.topic')['score_x'].mean()
weak_areas = topic_performance[topic_performance < 50]

difficulty_performance = merged_df.groupby('quiz.difficulty_level')['score_x'].mean()

def calculate_accuracy(response_map, correct_answers):
    if not response_map or not correct_answers:
        return 0
    correct_count = sum(
        1 for q_id, selected in response_map.items() if correct_answers.get(q_id) == selected
    )
    return correct_count / len(correct_answers) if correct_answers else 0

merged_df['accuracy'] = merged_df.apply(
    lambda row: calculate_accuracy(row.get('response_map', {}), row.get('quiz.correct_answers', {})),
    axis=1
)

recommendations = {
    "Topics to Focus On": weak_areas.index.tolist(),
    "Review Incorrect Responses": merged_df[merged_df['accuracy'] < 0.5]['quiz.id'].unique().tolist(),
}

if not difficulty_performance[difficulty_performance < 50].empty:
    recommendations["Practice High Difficulty Questions"] = difficulty_performance[difficulty_performance < 50].index.tolist()
else:
    recommendations["Practice High Difficulty Questions"] = []

print("Recommendations:")
print(tabulate(recommendations.items(), headers=["Category", "Recommendations"]))

persona_analysis = merged_df.groupby('user_id').agg({
    'quiz.topic': lambda x: x.mode().iloc[0] if not x.mode().empty else None,
    'score_x': 'mean'
}).reset_index()

def label_persona(score):
    if score >= 80:
        return "High Achiever"
    elif score >= 50:
        return "Average Performer"
    else:
        return "Needs Improvement"

persona_analysis['persona_label'] = persona_analysis['score_x'].apply(label_persona)

print("\nStudent Personas:")
print(tabulate(persona_analysis, headers="keys", tablefmt="pretty"))

plt.figure(figsize=(10, 6))
sns.barplot(x=topic_performance.index, y=topic_performance.values)
plt.title("Average Performance by Topic")
plt.xticks(rotation=90)
plt.xlabel("Topic")
plt.ylabel("Average Score")
plt.tight_layout()
plt.show()

plt.figure(figsize=(10, 6))
sns.histplot(merged_df['accuracy'], kde=True, bins=20)
plt.title("Accuracy Distribution of Students")
plt.xlabel("Accuracy")
plt.ylabel("Frequency")
plt.tight_layout()
plt.show()
