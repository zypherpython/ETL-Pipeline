# 🚀 ETL Pipeline - Data Engineering Journey

> A modern data pipeline project following Extract, Transform, Load principles. Built by an aspiring cloud data engineer starting their journey.

**📌 Learning Project** - This repository demonstrates fundamental ETL concepts and data engineering practices.

---

## 📋 Overview

This repository implements the **Extract-Transform-Load (ETL)** architecture, a fundamental pattern in cloud data engineering. Currently featuring **Extract** and **Transform** phases, with Load component coming soon.

- **Extract Phase**: Reads data from CSV sources with robust error handling
- **Transform Phase**: Cleans, validates, and deduplicates data

---

## 🎯 Project Goals

- ✅ Build a scalable, modular ETL pipeline from scratch
- ✅ Master data extraction, transformation, and loading techniques
- ✅ Apply cloud data engineering best practices
- ✅ Create a portfolio project for cloud data engineering roles
- 🔄 Learn industry-standard tools and patterns

---

## 📁 Project Structure

```
ETL-Pipeline/
├── Extract-Data.py          # Phase 1: Data extraction from sources
├── Transform-Data.py        # Phase 2: Data cleaning & transformation
├── Load-Data.py             # Phase 3: Data loading to destinations (coming soon)
├── README.md
└── requirements.txt
```

---

## 🔧 Phases

### Phase 1️⃣: Extract

**File**: `Extract-Data.py`

The Extract phase handles data ingestion from CSV files with:
- CSV file parsing using Python's `csv` module
- Dictionary-based row reading for structured data access
- Error handling for missing files
- Clean data return for downstream processing

### Phase 2️⃣: Transform

**File**: `Transform-Data.py`

The Transform phase processes extracted data with:
- **Data Validation**: Removes records with invalid grades (> 100)
- **Missing Data Handling**: Filters out records with missing age values
- **Deduplication**: Eliminates duplicate records based on (name, age, grade)
- **Data Cleaning**: Ensures data quality before loading

### Usage Example
```python
from Transform-Data import extract, transformation

# Extract data from CSV
data = extract("data/student.csv")

# Transform and clean the data
clean_data = transformation(data)

# Process cleaned records
for row in clean_data:
    print(row)
```

---

## 🛠️ Tech Stack

- **Language**: Python 3.x
- **Libraries**: csv (standard library)
- **Upcoming**: Pandas, Apache Spark, SQL databases

---

## 📚 About the Developer

👨‍💻 **17-year-old Cloud Data Engineer in Training**

This project represents the beginning of my cloud data engineering journey. I'm passionate about:
- Data pipelines and cloud infrastructure
- Building scalable solutions
- Learning modern data technologies
- Contributing to the open-source community

---

## 🤝 Contributing

Contributions, ideas, and feedback are welcome! Feel free to:
- Fork the repository
- Open issues with suggestions
- Submit PRs with improvements

---

## 📝 Documentation & Credits

**Code Architecture**: Designed and implemented by myself  
**README & Documentation**: Enhanced by Copilot

---

## 📅 Roadmap

- [x] Extract Phase (CSV parsing)
- [x] Transform Phase (Data cleaning & deduplication)
- [ ] Load Phase (Database/Cloud storage)
- [ ] Add unit tests
- [ ] Docker containerization
- [ ] CI/CD pipeline

---

## 💡 What's Next?

The **Load phase** is coming soon! Stay tuned and follow the repository for updates.

---

**Let's build something amazing! 🎉**