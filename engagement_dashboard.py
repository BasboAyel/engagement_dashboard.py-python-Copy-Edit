import pandas as pd
import matplotlib.pyplot as plt

# Step 1: Simulate data
data = {
    'article': [
        'AI in Education', 'Campus Sustainability', 'Sports Recap',
        'Student Spotlight', 'Tuition Policy Change', 'Career Fair Preview',
        'DSU Hacks', 'Mental Health Awareness', 'Alumni Interview', 'Dorm Decor Tips'
    ],
    'views': [320, 240, 410, 150, 500, 270, 380, 310, 190, 250],
    'shares': [30, 20, 40, 15, 55, 25, 35, 33, 18, 22],
    'avg_time_minutes': [4.5, 3.2, 5.0, 2.0, 6.1, 3.8, 4.7, 4.0, 2.8, 3.0]
}

df = pd.DataFrame(data)

# Step 2: Engagement score
df['engagement_score'] = (df['views'] * 0.5) + (df['shares'] * 2) + (df['avg_time_minutes'] * 10)

# Step 3: Sort and display top articles
df_sorted = df.sort_values(by='engagement_score', ascending=False)
print("Top Articles by Engagement:\n")
print(df_sorted[['article', 'engagement_score']])

# Step 4: Plot
plt.figure(figsize=(10, 6))
plt.barh(df_sorted['article'], df_sorted['engagement_score'], color='skyblue')
plt.xlabel('Engagement Score')
plt.title('Top Performing Articles')
plt.gca().invert_yaxis()
plt.tight_layout()
plt.show()
📄 File 2: README.md
markdown
Copy
Edit
# Engagement Analytics Dashboard

This project simulates article performance at a student newspaper and ranks content based on engagement. It visualizes which articles resonate most using a custom scoring metric.

## Features
- Synthetic dataset with article views, shares, and read time
- Calculates engagement score using a weighted formula
- Visualizes top-performing content with a horizontal bar chart

## Tools Used
- Python
- pandas
- matplotlib
