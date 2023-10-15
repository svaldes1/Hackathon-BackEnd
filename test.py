import numpy as np
from tensorflow import keras
from tensorflow.keras import layers

# Sample data (replace with real dataset)
input_data = np.array([[65, 0.5, 1, 16, 11, 15,12],  # Example of high phone, middle accessory, high plan, and low home preference
                       [0, 30, 1, 0.5, 10, 90, 4],
                       [0.5, 0, 1, 10, 1 ,1 , 2]])
output_data = np.array([[1, 0, 0, 0],  # Example of recommending the first product
                        [0, 1, 0, 0],
                        [0, 0, 0, 1]])

# Define the model
model = keras.Sequential()

# Add input layer
model.add(layers.Input(shape=(7,)))

# Add hidden layers (modify as needed based on data complexity)
model.add(layers.Dense(32, activation='relu'))
model.add(layers.Dense(32, activation='relu'))

# Add output layer (assuming 3 product recommendations)
model.add(layers.Dense(4, activation='softmax'))  # Softmax for multi-class classification

# Compile the model
model.compile(optimizer='adam',
              loss='categorical_crossentropy',
              metrics=['accuracy'])

# Train the model (use actual training data here)
model.fit(input_data, output_data, epochs=50, batch_size=32, validation_split=0.2)

def recommend_product(preferences):
    # Convert preferences into appropriate format
    processed_input = np.array([preferences])  # Assuming preferences is a list like [1, 0.5, 0, 1]
    prediction = model.predict(processed_input)
    print(prediction)
    top_product = np.argsort(prediction[0])[-1:][::-1]
    return top_product

# Test the recommendation function
customer_input = [1, 15, 0, 1,14,65,9]  # Example input
recommended_product = recommend_product(customer_input)
print(f"Recommended product: {recommended_product}")