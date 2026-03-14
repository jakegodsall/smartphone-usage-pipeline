from pathlib import Path
import pandas as pd
from sklearn.model_selection import train_test_split

input_path = "/opt/ml/processing/input/data.csv"
train_path = "/opt/ml/processing/train/train.csv"
test_path = "/opt/ml/processing/est/test.csv"

df = pd.read_csv(input_path)

train, test = train_test_split(df, test_size=0.2, random_state=42)

train.to_csv(train_path, index=False)
test.to_csv(test_path, index=False)