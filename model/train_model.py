import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
import pickle

# Load dataset
df = pd.read_csv("../dataset/istanbul_satilik_evler_2023.csv")

# Clean and preprocess data
df.columns = df.columns.str.strip()
df['Price'] = pd.to_numeric(df['Price'].str.replace(",", "").str.strip(), errors='coerce')
df['Room'] = df['Room'].str.split('+').str[0].str.strip()
df['Room'] = pd.to_numeric(df['Room'], errors='coerce')
df['Area'] = pd.to_numeric(df['Area'], errors='coerce')
df['Age'] = pd.to_numeric(df['Age'], errors='coerce')
df['Floor'] = pd.to_numeric(df['Floor'], errors='coerce')
df.dropna(inplace=True)

# Define features and target variable
X = df[['Room', 'Area', 'Age', 'Floor']]
y = df['Price']

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Create and train the model
model = LinearRegression()
model.fit(X_train, y_train)

# Save the model to a file
with open("regression_model.pkl", 'wb') as file:
    pickle.dump(model, file)

# Make predictions and evaluate the model
y_pred = model.predict(X_test)
mse = mean_squared_error(y_test, y_pred)
rmse = mse ** 0.5
print("Root Mean Squared Error:", rmse)
