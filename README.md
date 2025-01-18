# Student Quiz Performance Analyzer

## What This Project Is About

This project helps students prepare better by analyzing their quiz performance. It looks at how they've done in recent quizzes, identifies patterns, and gives tips to improve. The focus is on recognizing weak spots, figuring out strengths, and providing clear, personalized recommendations to make studying more effective.

## Cool Things It Does

### Understands Performance:
- Combines data from recent quizzes and past performance.
- Highlights topics and question types where students need help.

### Gives Smart Tips:
- Suggests topics to focus on.
- Points out which difficult questions to practice.
- Lists questions students got wrong for review.

### Creates Student Profiles:
- Labels students as "High Achiever," "Average Performer," or "Needs Improvement" based on their scores.

## How to Get Started

### Requirements:
- Python.
- I Installed the following Python libraries:
  - `requests`
  - `pandas`
  - `tabulate`

### Steps:
1. Download or copy the project files.
2. Install the required libraries by running:
   ```bash
   pip install requests pandas tabulate

## How It Works

### Data Sources:
- **Quiz Info**: Details about quizzes, such as their topic and difficulty.
- **User Answers**: Data on what students answered in their most recent quiz.
- **Past Performance**: How students scored in their previous quizzes.

### Step-by-Step Process:

1. **Getting the Data**:
   - Fetch data from the provided web links.
   - Check to ensure the data is correct.

2. **Merging the Data**:
   - Combine quiz answers with past performance information.
   - Add additional details like topics and difficulty levels.

3. **Finding Patterns**:
   - Identify weak areas, such as topics where students score below 50%.
   - Analyze which difficulty levels are the most challenging.
   - Calculate how frequently students answer questions correctly.

4. **Giving Advice**:
   - Suggest topics and question types to focus on.
   - Provide a list of questions that students should review.

5. **Creating Profiles**:
   - Group students by their performance.
   - Label them as "High Achiever," "Average Performer," or "Needs Improvement."
## Example Results

### Recommendations

| Category              | Suggestions                            |
|-----------------------|----------------------------------------|
| Topics to Focus On     | ['Structural Organisation in Animals'] |
| Practice Hard Questions | ['Advanced Genetics']                 |
| Review Wrong Answers   | [43]                                   |

### Student Profiles

| User ID                          | Topic                               | Score | Label              |
|----------------------------------|-------------------------------------|-------|--------------------|
| 7ZXdz3zHuNcdg9agb5YpaOGLQqw2 | Structural Organisation in Animals | 32.0  | Needs Improvement |


