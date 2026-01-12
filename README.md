# Myntra Review Scraper

An end-to-end project that scrapes product reviews from Myntra, stores the data in MongoDB, and presents interactive insights through a Streamlit dashboard.

---

## 🚀 Project Overview

This project performs the following tasks:

- **Scrapes** product reviews from Myntra.
- **Cleans and processes** review data.
- **Stores** data in MongoDB for scalability.
- **Visualizes** insights using a Streamlit dashboard.
- **Adapts UI** automatically for single or multiple products.

---

## 🛠️ Tech Stack

* **Language:** Python
* **Web Framework:** Streamlit
* **Database:** MongoDB
* **Data Handling:** Pandas, NumPy
* **Visualization:** Plotly
* **Scraping:** Selenium / Requests / BeautifulSoup
* **Version Control:** Git & GitHub

---

## 📂 Project Structure

```text
myntra_review_scrapper/
│
├── app.py                      # Main entry point for Streamlit
├── pages/
│   └── generate_analysis.py    # Dashboard analysis page
│
├── src/
│   ├── cloud_io/
│   │   ├── mongo_io.py         # MongoDB I/O operations
│   │   └── database_connect/
│   │       └── mongo_operation.py
│   │
│   ├── data_report/
│   │   └── generate_data_report.py
│   │
│   ├── scrapper/
│   │   └── scrape.py           # Scraping logic
│   │
│   ├── constants/              # Project constants
│   ├── utils/                  # Helper functions
│   └── exception.py            # Custom exception handling
│
├── .gitignore
└── README.md
```

---

## 📊 Features

### 🔹 Scraping

- Dynamically scrapes product reviews from Myntra
- Data changes on every scrape and is not committed to Git

### 🔹 Data Storage

- Uses MongoDB for structured and scalable data storage

### 🔹 Dashboard

#### General Information Section
- Average ratings displayed using a donut chart  
- Average price comparison using a horizontal bar chart  
- Automatically hidden when only one product is present  

#### Product Sections
- Average price and rating per product  
- Positive and negative review highlights  
- Rating distribution  
- Clean, non-rigid grid-based layout  
- Fully dynamic UI that adapts to product count

---

## 📌 Notes

- Scraped data files such as `data.csv` are intentionally ignored via `.gitignore`
- Jupyter notebook files are excluded to keep the repository clean
- Python cache files (`__pycache__`, `.pyc`) are ignored as per best practices

---

## 🎯 Learning Outcomes

- Real-world web scraping
- Data cleaning and preprocessing
- MongoDB integration with Python
- Building scalable and flexible Streamlit dashboards
- Professional Git and repository management practices

---

## 👩‍💻 Author

**Ishita Sharma**  
CSE & AIML Student

---

## ⭐ Future Enhancements

- Sentiment analysis on reviews
- Product filtering and search
- Deployment on Streamlit Cloud
- Advanced analytics dashboards
