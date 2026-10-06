import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn import metrics

# 1. Load and Clean
df = pd.read_csv('Advertising.csv')
if 'Unnamed: 0' in df.columns:
    df = df.drop(columns=['Unnamed: 0'])
df.dropna(inplace=True)

print("--- Starting AI Analysis ---")

# 2. Visuals (EDA)
# Plot 1: TV vs Sales
plt.figure(figsize=(8, 5))
sns.scatterplot(data=df, x='TV', y='Sales')
plt.title('TV Advertising vs Sales')
plt.savefig('scatter_plot.png')
plt.show()

# Plot 2: Correlation Heatmap
plt.figure(figsize=(8, 6))
sns.heatmap(df.corr(), annot=True, cmap='coolwarm')
plt.title('Correlation Heatmap')
plt.savefig('heatmap.png')
plt.show()

# 3. Linear Regression Model
X = df[['TV', 'Radio', 'Newspaper']]
y = df['Sales']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = LinearRegression()
model.fit(X_train, y_train)
predictions = model.predict(X_test)

# 4. Final Results
r2 = metrics.r2_score(y_test, predictions)
print(f"Model R² Score: {r2:.4f}")
print("\nCONCLUSION:")
print("The analysis shows that TV advertising has the strongest impact on sales.")