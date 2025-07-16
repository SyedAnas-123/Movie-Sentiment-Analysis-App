import pickle
import tensorflow as tf
import numpy as np

# Load model and tokenizer
model = tf.keras.models.load_model("sentiment_model.keras")
with open("tokenizer.pkl", "rb") as f:
    tokenizer = pickle.load(f)

def predict_sentiment(text):
    seq = tokenizer.texts_to_sequences([text])
    padded = tf.keras.preprocessing.sequence.pad_sequences(seq, maxlen=200)
    prediction = model.predict(padded)
    return prediction[0][0]

def test_positive_sentiment():
    result = predict_sentiment("This movie was amazing and inspiring!")
    assert result > 0.5, "Expected positive sentiment"

def test_negative_sentiment():
    result = predict_sentiment("This was the worst and most boring movie ever.")
    assert result < 0.5, "Expected negative sentiment"
