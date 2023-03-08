import pickle


# Load the ML model
filename = 'shoe_size_prediction_model.pkl'
with open(filename, 'rb') as file:
    loaded_model = pickle.load(file)

# Use the loaded model to make predictions
new_X = [[165], [170], [175]]
predictions = loaded_model.predict(new_X)
print(predictions)
