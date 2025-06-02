import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt 
import seaborn as sns 
from sklearn import datasets 
from sklearn.model_selection import train_test_split 
from sklearn.svm import SVC 
from sklearn.metrics import classification_report, accuracy_score

import pandas as pd 
# Load dataset 
df = pd.read_csv("C:\\Users\\hp\\OneDrive\\Desktop\\spam.csv", encoding="latin-1") 
df = df[['v1', 'v2']]  # Retaining relevant columns 
df.columns = ['label', 'message'] 
# Display first few rows 
df.head() 