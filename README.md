# 📘 TMD Analytical Model (Python)

> Analytical model developed for Master's thesis on Tuned Mass Dampers (TMD) — Hochschule Furtwangen University (HFU), 2025

---

## 🧠 Overview
This repository contains the complete Python implementation of the analytical model described in:

📄 **[Anna Keller – Master Thesis (PDF)](./AnnaKeller_MasterThesis_HFU_signed.pdf)**

The model investigates frequency response of a 2DOF mechanical system with a TMD, analyzing optimal parameters for damping.

---

## 📂 Structure

```bash
MasterThesis/
├── AnnaKeller_MasterThesis_HFU_signed.pdf    # Thesis PDF
└── Thesis.Py/                                # Python source code
    ├── frf.py
    ├── main.py
    ├── optimal_TMD.py
    ├── primeSystem.py
    └── solver.py
```

---

## 🧪 Files Explained

| File              | Description                                                                 |
|-------------------|-----------------------------------------------------------------------------|
| `main.py`         | Main script to run the model and produce output (plots, response, etc.)     |
| `solver.py`       | Solver logic for Lin equations                                               |
| `optimal_TMD.py`  | Calculates optimal damping/mass ratios for given system parameters (Den Hartog, Lin)          |
| `primeSystem.py`  | Act as a config file for input parameters                                          |
| `frf.py`          | Computes Frequency Response Function for an untuned system                                         
|

---

## 🚀 Run the Model

Use any Python environment (Python 3.9+ recommended):

```bash
cd Thesis.Py
python3 main.py
```

---

## 📈 Output

The model calculates optimal TMD configurations and visualizes the frequency response of the system.

---

## 📚 Related Work

This repository is based on analytical methods described in:
- **Chapter 7** of the thesis
- Classical mechanical vibration theory (2DOF systems)

---

## 👩‍🎓 Author

**Anna Keller**  
Master of Science in Mechatronics  
Hochschule Furtwangen University (HFU), 2025  

---

## 📄 License

This project is released under the MIT License. Feel free to reuse, cite, and extend it.

---
