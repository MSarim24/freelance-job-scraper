# Freelance Job Scraper

A Python script that scrapes freelance job listings from Truelancer based on a keyword provided via the command line. The scraper saves results in CSV and Excel format and runs daily using `schedule`.

## 💡 Features

- Command-line search keyword
- Scrapes job title, budget, skills, and link
- Saves results to CSV and Excel
- Automatically filters results by keyword
- Automatically runs daily at a specific time
- Supports real-time job tracking

## 📦 Requirements

Install dependencies:
```bash
pip install -r requirements.txt
```
## 📊 Output

The script generates two files:

- `freelance_<keyword>.csv` – Clean CSV file  
- `freelance_<keyword>.xlsx` – Excel version of the same data

**Example:**

These files will always contain the **most up-to-date jobs**, because each time the script runs, it **overwrites** the previous ones.  
This ensures you only get **currently available jobs** without any outdated listings.

---

## 📁 Sample

Check the [`samples/`](samples/) folder (if available) for example output files.

> 💡 Tip: You can open the Excel file in **Microsoft Excel** or **Google Sheets** to easily browse job titles, budgets, and required skills.

---

## 🔧 Schedule Automation

This scraper is scheduled to **run daily at a specific time** using the `schedule` module.

```python
schedule.every().day.at("16:35").do(dailytask)
```

---


