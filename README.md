# 🎬 Sentiment Analysis App with LSTM + Streamlit + Hugging Face CI/CD

This project demonstrates a **Sentiment Analysis system** built using Deep Learning (LSTM) on the IMDB movie reviews dataset. The app is developed with **Streamlit** for an interactive web interface and deployed with **Hugging Face Spaces** using **CI/CD automation** via GitHub Actions.

---

## 🚀 Features

✅ LSTM-based sentiment classification  
✅ Trained on IMDB movie review dataset  
✅ Clean and interactive UI using **Streamlit**  
✅ Real-time predictions with confidence score  
✅ Dynamic sentiment bar chart visualization using **streamlit-echarts**  
✅ Model and tokenizer saved and reused efficiently  
✅ CI/CD workflow using **GitHub Actions**  
✅ One-click deployment on Hugging Face Spaces  

---

## 🧠 How It Works

1. The user enters a movie review.
2. The review is **tokenized and padded** using a pre-trained Keras `Tokenizer`.
3. The LSTM model makes a binary prediction:  
   - **Positive** (1) or  
   - **Negative** (0)
4. The result is displayed with a confidence score and an animated bar chart.

---

## 🏗️ Tech Stack

| Technology      | Purpose                              |
|-----------------|---------------------------------------|
| **Python**      | Core language                         |
| **TensorFlow/Keras** | LSTM model and tokenizer              |
| **Streamlit**   | Web interface                         |
| **streamlit-echarts** | Visualization charts                 |
| **Hugging Face Spaces** | Deployment platform               |
| **GitHub Actions** | CI/CD automation                     |
| **IMDB Dataset** | Training data (text + sentiment)      |

---

## 📊 Model Architecture

```python
model = Sequential()
model.add(Embedding(input_dim=5000, output_dim=128, input_length=200))
model.add(LSTM(128, dropout=0.2, recurrent_dropout=0.2))
model.add(Dense(1, activation='sigmoid'))

Embedding Layer: Converts words to vector representations

LSTM Layer: Learns long-term dependencies in text

Dense Layer: Outputs probability (0 = negative, 1 = positive)




💡 How to Run Locally
# Clone the repo
git clone https://github.com/your-username/sentiment-streamlit-app.git
cd sentiment-streamlit-app

# Install dependencies
pip install -r requirements.txt

# Run the app
streamlit run app.py

🛰️ Deployment (Hugging Face Spaces)
This project is also deployed at:
👉 Live Demo on Hugging Face

🔄 CI/CD with GitHub Actions
Every push to GitHub triggers:

✅ Linting and Testing

✅ Auto-build of the Streamlit app

✅ Auto-deployment to Hugging Face Spaces

deploy.yml manages this flow via GitHub Actions.

📈 Example Predictions
Review Text	Predicted Sentiment	Confidence
"This movie was fantastic. I loved it!"	😃 Positive	0.94
"This was the worst movie I’ve ever seen."	😞 Negative	0.88
"It was average, not great but not terrible."	😞 Negative	0.52

🙋‍♂️ Author
Syed Mohammad Anas
📫 Connect on LinkedIn
💻 Explore more on GitHub

⭐ If you liked this project, give it a star!
