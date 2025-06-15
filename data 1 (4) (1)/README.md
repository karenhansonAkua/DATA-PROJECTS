
# 📘 Term Deposit Subscription Prediction API

This project is a Flask API that predicts whether a bank client will subscribe to a term deposit, using a machine learning model trained on marketing campaign data.

---

## 📁 Project Structure

```
├── app.py                  # Flask API
├── model_pipeline.pkl      # Trained model + preprocessor (Pickle file)
├── requirements.txt        # Python dependencies
├── README.md               # You're here
```

---

## 🔧 Setup Instructions

### ✅ 1. Clone the repository

```bash
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name
```

### ✅ 2. Create a virtual environment (optional but recommended)

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### ✅ 3. Install dependencies

```bash
pip install -r requirements.txt
```

### ✅ 4. Run the API locally

```bash
python app.py
```

The API will run on:  
📍 `http://127.0.0.1:5000/`

---

## 🚀 API Usage

### ✅ Endpoint

```
POST /predict
```

### ✅ Example Input (JSON)

```json
{
  "age": 30,
  "job": "admin.",
  "marital": "married",
  "education": "secondary",
  "default": "no",
  "balance": 1200,
  "housing": "yes",
  "loan": "no",
  "contact": "cellular",
  "day": 15,
  "month": "aug",
  "duration": 300,
  "campaign": 1,
  "pdays": -1,
  "previous": 0,
  "poutcome": "unknown"
}
```

### ✅ Example Response

```json
{
  "subscription_probability": 0.3567
}
```

---

## 🌐 Deployment on Render

1. Push your code to GitHub.
2. Log in to [Render](https://render.com/).
3. Click **"New Web Service"** → Connect your GitHub repo.
4. Set the following:
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `python app.py`
   - **Runtime**: Python 3.x
   - **Port**: 5000 (Render detects this by default)

5. Upload your `model_pipeline.pkl` file to your repo if it’s not there already.

---

## 📦 Requirements (`requirements.txt`)

```txt
flask
pandas
scikit-learn
```

---

## 📬 Contact

For questions or collaboration:
- GitHub: [@your-username](https://github.com/your-username)
- Email: your.email@example.com
