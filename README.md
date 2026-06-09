# 🚀 ETL Pipeline - Data Engineering Journey

> A modern data pipeline project following Extract, Transform, Load principles. Built by an aspiring cloud data engineer starting their journey.

---

## 📋 Overview

This repository implements the **Extract-Transform-Load (ETL)** architecture, a fundamental pattern in cloud data engineering. Currently featuring the **Extract** phase, with Transform and Load components coming soon.

**Extract Phase**: Seamlessly reads data from CSV sources with robust error handling and structured data parsing.

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
├── Transform-Data.py        # Phase 2: Data cleaning & transformation (coming soon)
├── Load-Data.py             # Phase 3: Data loading to destinations (coming soon)
├── README.md
└── requirements.txt
```

---

## 🔧 Phase 1: Extract

**File**: `Extract-Data.py`

The Extract phase handles data ingestion from CSV files with:
- CSV file parsing using Python's `csv` module
- Dictionary-based row reading for structured data access
- Error handling for missing files
- Clean data return for downstream processing

### Usage Example
```python
from Extract-Data import Extract

# Load data from CSV
data = Extract("data/student.csv")

# Access parsed rows
for row in data:
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
**README & Documentation**: Written by Copilot

---

## 📅 Roadmap

- [x] Extract Phase (CSV parsing)
- [ ] Transform Phase (Data cleaning & aggregation)
- [ ] Load Phase (Database/Cloud storage)
- [ ] Add unit tests
- [ ] Docker containerization
- [ ] CI/CD pipeline

---

## 💡 What's Next?

Stay tuned! The Transform and Load phases are coming soon. Follow the repository to stay updated.

---

**Let's build something amazing! 🎉**
