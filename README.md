# 🩺 Patient Vitals Tracker and Analyzer

A data visualization project to analyze patient vitals like temperature, blood pressure, and heart rate using Python libraries: **Pandas**, **Matplotlib**, and **Seaborn**.

---

## 📌 Project Overview

This project helps in tracking and analyzing health data of multiple patients over a period of time. It uses visualizations to give insights into:

- Temperature trends
- Blood pressure comparisons
- Heart rate variations
- Health status distribution
- Vital signs correlation
## 📁 Dataset

**Filename:** `vitals.csv`

**Sample Columns:**
- `Day`: Day of recording
- `Patient`: Patient's name
- `Age`: Age of the patient
- `HeartRate`: Pulse rate
- `BP_Sys`: Systolic Blood Pressure
- `BP_Dia`: Diastolic Blood Pressure
- `Temperature`: Body temperature (F)
- `Status`: Health condition (`Normal`, `Alert`, `Critical`)
## 📊 Visualizations Used

| Chart Type     | Description                                 |
|----------------|---------------------------------------------|
| 📈 Line Chart  | Temperature vs Health Status                |
| 📉 Bar Chart   | Systolic vs Diastolic BP Comparison         |
| 📦 Box Plot    | Heart rate variance analysis                |
| 🥧 Pie Chart   | Health status distribution overview         |
| 🌡️ Heatmap     | Correlation between vital parameters        |

---

## 🚀 How to Run

1. Clone this repo or download the `.py` file and `vitals.csv`
2. Install required libraries (if not installed):

```bash
pip install pandas matplotlib seaborn
