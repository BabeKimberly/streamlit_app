import numpy as np
import pickle
from sklearn.ensemble import RandomForestClassifier

# Load the saved model
loaded_model = pickle.load(open('C:/Users/LENOVO/Documents/dissertation research/Predictive Model/trained_model (1).sav', 'rb'))

# Get the number of features from the loaded model
num_features_expected = loaded_model.n_features_in_

# Example input data (this should be your actual input data)
input_data = np.array([28, 12, 157, 70, 27.606336560126255, 87, 127, 14.510683434664765, 
                       38.21512468306882, 2.439556477109007, 356, 1.2740403802347329, 
                       26.504275495862228, 17.322949333947648, 1.0973753982010117, 
                       95.61152865293266, 269.8123420700398, 1, 0, 1, 1, 2, 1, 2])  
# Changing the input_data to a numpy array
input_data_as_numpy_array = np.asarray(input_data).reshape(1, -1)

# Reshape the array as we are predicting for one instance
prediction = loaded_model.predict(input_data_as_numpy_array)

print(prediction)

if (prediction[0] == 0):
    print('The person does not have Preeclampsia')
else:
    print('The person had Preeclampsia')