# import pickle
import streamlit as st
from PIL import Image


def predictShoeSize(height):
    predicted_shoe_size = 999
    # Load the ML model
    # filename = 'shoe.size.prediction.model.pkl'
    # with open(filename, 'rb') as file:
    #     loaded.model = pickle.load(file)

    # # Use the loaded model to make predictions
    # new.X = [[height]]
    # predicted_shoe_size = loaded.model.predict(new.X)
    # print(predicted_shoe_size)

    return predicted_shoe_size

st.markdown("***")
st.markdown("# Let's Predict your Shoe Size from your Height")
st.markdown("***")

height_row, space, shoe_size_row = st.columns([2,1,2])

with height_row:
    st.image("https://drive.google.com/uc?id=17A15LbY0ldA3uP3tDG-mAOBtZAeW6OJ7", use_column_width=True) 

    

with shoe_size_row:
    height = st.number_input('Insert your height (cm):')
    predicted_shoe_size = predictShoeSize(height)
    st.markdown("  ")
    st.markdown("  ")
    st.markdown("Your shoe size is:")
    st.markdown("# " + str(predicted_shoe_size))
    st.markdown("  ")
    st.markdown("  ")




st.markdown("***")