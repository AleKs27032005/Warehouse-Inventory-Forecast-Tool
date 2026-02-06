# Smart Inventory System  
### Warehouse Inventory Forecast Tool (Python Application)

Smart Inventory System is a clean and professional Python-based application designed to analyze warehouse inventory data, forecast stock depletion, recommend reorder dates, and highlight inventory risk levels. The application uses historical sales data to provide actionable insights through an interactive Streamlit dashboard.

---

## 📦 Project Overview

The **Warehouse Inventory Forecast Tool** allows users to:
- Import inventory data from CSV or Excel files
- Analyze daily sales history
- Forecast inventory levels
- Identify items at risk of stock-out
- Determine optimal reorder dates based on lead time

The focus of the project is simplicity, clarity, and practical inventory decision support.

---

## ✨ Core Features

### Main Dashboard
- Upload CSV / Excel inventory file
- Select an item from a dropdown list
- Visualize sales history and inventory trends
- Display key insights:
  - Average Daily Demand
  - Days Until Stock-Out
  - Recommended Reorder Date
  - Lead Time
  - Risk Level

### Inventory Summary Table
A fully visible table showing:
- Item Name
- Current Stock
- Average Daily Sales
- Days Until Stock-Out
- Reorder Date
- Lead Time
- Risk Level

---

## 📊 Forecasting Logic

The forecasting calculations are based on simple, transparent rules:

1. **Average Daily Demand**  
total sales / number of days


2. **Days Until Stock-Out**  


current stock / average daily demand


3. **Recommended Reorder Date**  


today + (days left − lead time)


4. **Risk Levels**
- **High**: days left < lead time
- **Medium**: lead time ≤ days left < lead time + 3
- **Low**: days left ≥ lead time + 3

---

## 🧾 Input Data Format

The application expects a CSV (or Excel) file with the following columns:

item_name
current_stock
lead_time_days
day_1, day_2, day_3, ... day_14


Each `day_n` column represents sales for that day.

---

## 🛠️ Technical Stack

- Python 3.9+
- Streamlit (UI)
- pandas, numpy (data processing)
- matplotlib (visualization)
- openpyxl (Excel support)

---

## 🚀 Setup & Installation

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/AleKs27032005/Warehouse-Inventory-Forecast-Tool.git
cd smart-inventory-system

2️⃣ Create and Activate Virtual Environment
Windows
python -m venv venv
venv\Scripts\activate

macOS / Linux
python3 -m venv venv
source venv/bin/activate

3️⃣ Install Dependencies
pip install -r requirements.txt

▶️ Run the Application
streamlit run app.py


After running the command, Streamlit will open the application in your default web browser.
```

## Demo
<img width="1920" height="2081" alt="smart-inventory-application" src="https://github.com/user-attachments/assets/824bffca-5b19-4ba1-aa59-8c099d271e6a" />

