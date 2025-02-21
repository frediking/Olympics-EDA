# **EDA Olympics**

## **Overview**  
**Exploratory Data Analysis (EDA)** on the Olympic dataset sourced from **Kaggle** ([Dataset Link](https://www.kaggle.com/datasets/bhanupratapbiswas/olympic-data)). The dataset contains information on Olympic athletes, including their age, height, weight, sport, medals won, and more.  

The goal of this project is to uncover key insights about the Olympics using **Python**, **Pandas**, **Seaborn**, and **Matplotlib**.

## **Dataset Description**  
The dataset consists of **70,000 records** and the following columns:  

| Column Name | Description |
|-------------|------------|
| `ID` | Unique identifier for the athlete |
| `Name` | Athlete’s name |
| `Sex` | Gender (M/F) |
| `Age` | Age of the athlete |
| `Height` | Height in cm |
| `Weight` | Weight in kg |
| `Team` | Country/Team representation |
| `NOC` | National Olympic Committee code |
| `Games` | Year and season of the Olympics |
| `Year` | Year of the event |
| `Season` | Summer or Winter Olympics |
| `City` | Host city |
| `Sport` | Sport category |
| `Event` | Specific event |
| `Medal` | Type of medal won (Gold, Silver, Bronze) or NaN if none |

## **Exploratory Analysis Performed**  
The project covers:  
✅ **Data Cleaning & Preprocessing**  
   - Handling missing values  
   - Removing duplicates  

✅ **Descriptive Statistics**  
   - Summary of numerical & categorical variables  

✅ **Data Visualization**  
   - Gender distribution (`countplot`)  
   - Age, height, and weight distribution (`histplot`)  
   - Medal distribution (`countplot`)  
   - Athlete height vs weight (`scatterplot`)  
   - Medal counts over the years (`heatmap`)  
   - Country-wise performance in the Olympics (`barplot`)  

✅ **Key Insights**  
   - Most awarded country  
   - Tallest and shortest athletes  
   - Oldest and youngest participants  
   - Sports with the highest median height  
   - Countries with the most gold medals  

## **Installation & Requirements**  
Ensure you have the following Python libraries installed:  

```bash
pip install pandas numpy seaborn matplotlib
```

## **How to Run This Project**  

1️⃣ **Clone the repository (or download the script)**  
```bash
git clone https://github.com/your-repo/eda-olympics.git
cd olympics-EDA
```

2️⃣ **Download the dataset from Kaggle**  
   - [Olympic Dataset](https://www.kaggle.com/datasets/bhanupratapbiswas/olympic-data)  
   - Place `dataset_olympics.csv` in the project folder  

3️⃣ **Run the Python script**  
```bash
python EDA Olympics.py
```

or, if running in a Jupyter Notebook:  
```python
jupyter notebook
```
Open `EDA Olympics.ipynb` and run the cells.

## **Project Structure**  
```
📂 EDA-Olympics
 ├── 📄 README.md
 ├── 📄 EDA Olympics.py
 ├── 📂 dataset
 │   ├── dataset_olympics.csv
 ├── 📂 images (visualization outputs)
 └── 📂 notebooks
     ├── EDA Olympics.ipynb
```

## **Contributions**  
Feel free to fork this repo and improve the EDA by adding:  
- More visualizations  
- Machine learning models for medal prediction  
- Interactive dashboards  

## **License**  
This project is for educational/ practice purposes only. The dataset belongs to **Kaggle**.  
