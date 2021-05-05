import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import os
path = os.getcwd()

df = pd.read_csv(f"{path}\\data\\data_netflix.csv",sep=',')

# Instantiate Count Vectorizer
cv = CountVectorizer()

# Convert text of the `features_1` column, which contain directors, cast, country, rating and listed_in
# information into a matrix of tokens count
cv_f2 = cv.fit_transform(df['features_2'])

# Now we will get the cosine similarity
cs = cosine_similarity(cv_f2)

# Save the cosine similarity matrix (numpy.ndarray)
np.save(f"{path}\\data\\cv_f2.npy", cs)