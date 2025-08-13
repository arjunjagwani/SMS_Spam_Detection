# SMS Spam Detection

A Streamlit-based web application for detecting SMS spam using a machine learning model powered by an Extra Trees Classifier.

---

##  Live Demo

Access the working app at:  
https://smsspamdetection-130825.streamlit.app

---

##  Project Overview

This project demonstrates a simple yet effective approach to SMS spam detection using a supervised machine learning model.

Key highlights:
- Model: **Extra Trees Classifier**
- **Accuracy**: 97.38%
- **Precision**: 1.0
- Already tested **Naïve Bayes** and several other models — Extra Trees Classifier outperformed them by a significant margin.
- Includes **text preprocessing** steps like stemming, stopword removal, and punctuation cleaning.

---

##  Features

- **User-Friendly Interface**: Built with Streamlit, allowing easy input of SMS messages and instant feedback—“Spam” or “Not Spam”.
- **Efficient and Accurate**: High precision ensures that flagged spam is truly spam, minimizing false positives.
- **Optimized Preprocessing**: Includes stemming and stopword reduction to improve model performance.

---

##  Installation & Setup

1. **Clone the repository**  
   ```bash
   git clone https://github.com/arjunjagwani/SMS_Spam_Detection.git
   cd SMS_Spam_Detection


2. **Create and activate a virtual environment (optional but recommended)**

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

---

## How to Use

Run the Streamlit app:

```bash
streamlit run app.py
```

Then, go to the displayed URL (usually [http://localhost:8501](http://localhost:8501)) in your browser to access the interface.

---

## Project Structure

* `app.py`: Main Streamlit application file.
* `model.pkl`: Pre-trained Extra Trees Classifier model.
* `vectorizer.pkl`: Text vectorizer (e.g., TF-IDF / Count Vectorizer) for preprocessing messages.
* `requirements.txt`: List of required Python libraries.
* `runtime.txt`: Runtime environment specification (for deployment platforms like Heroku, if used).

---

## Model Performance Metrics

| Metric    | Score  |
| --------- | ------ |
| Accuracy  | 97.38% |
| Precision | 1.0    |

These results indicate a strong model performance, particularly in minimizing false positives.

---

## Future Enhancements

* Expand to include metrics like **Recall**, **F1-score**, and **confusion matrix** for a more comprehensive evaluation.
* Explore additional ensemble models and deep learning approaches.
* Improve UI by adding:

  * Batch message input (e.g., CSV file upload).
  * Colored indicators or icons for dynamic visual feedback.

---

## Contributing

Contributions are welcome! Feel free to submit:

* Bug reports or improvement suggestions via Issues.
* Pull requests for features, performance tuning, or UI refinements.

---

## License

Specify your chosen license here (e.g., MIT License) or indicate "All rights reserved" if applicable.

---

## Contact

For questions or feedback, reach out via GitHub or your preferred contact method.

---

**Enjoy building smarter spam detection!**

```


