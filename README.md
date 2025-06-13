# 📘 TMD Analytical Model (Python)

> Analytical model developed for Master's thesis on Tuned Mass Dampers (TMD) — Hochschule Furtwangen University (HFU), 2024

---

## 🧠 Overview
This repository contains the complete Python implementation of the analytical model described in:

📄 **[Anna Keller – Master Thesis (PDF)](./7Chapter_AnalyticalModel.pdf)**

The model investigates frequency response of a 2DOF mechanical system with a TMD, analyzing optimal parameters for damping.

---

## 🔬 Model Summary

### Goal

Design and optimize a TMD system for a vibrating medical device by:

- Calculating **optimal mass ratio (μ)** and **damping ratio (ζ)**
- Comparing effects of different TMD configurations on system stability
- Visualizing FRF (Frequency Response Function)

### Analytical Foundation

The primary system is modeled as a **1DOF system** and extended to a **2DOF system** when a TMD is attached. This is reflected in the governing equations and FRF formulations.

#### 📊 1DOF and 2DOF Systems

| System Type | Diagram |
|-------------|---------|
| 1DOF System | ![Figure 48](./figures/figure_48_1dof.png) |
| 2DOF with TMD | ![Figure 49](./figures/figure_50_2dof.png) |


---

## 📂 Repository Structure

```bash
├── README.md                          # Project description and instructions
├── requirements.txt                   # Python dependencies
├── figures/                           # Simulation output figures
│   ├── fixed_k2.png
│   └── den_hartog_vs_lin.png          # Comparison plot (Den Hartog vs Lin)
├── MasterThesis/
│   └── AnnaKeller_MasterThesis_HFU_signed.pdf  # Full thesis PDF
├── Thesis.Py/                         # Python source code
│   ├── main.py                        # Main script (runs all logic & plots)
│   ├── frf.py                         # Frequency response functions
│   ├── optimal_TMD.py                 # TMD optimization algorithms
│   ├── primeSystem.py                 # System input parameters
│   └── solver.py                      # Equation solver used in Lin method

```

---

## 🧪 Files Explained

| File              | Description                                                                 |
|-------------------|-----------------------------------------------------------------------------|
| `main.py`         | Main simulation script. Plots multiple FRFs using various TMD configs.                      |
| `solver.py`       | Solver logic for Lin equations                                                              |
| `optimal_TMD.py`  | Calculates optimal TMD parameters using Den Hartog, Lin methods                             |
| `primeSystem.py`  | Act as a config file for input parameters of the primary system (mass, stiffness, damping)  |      
| `frf.py`          | Contains functions for calculating Frequency Response Functions                             |

---

## 📐 Example Formulae

**Undamped 1DOF System:**
![Undamped 1DOF](figures/formula_1dof.png)

**Tuned with TMD (2DOF):**
![Tuned with TMD](figures/formula_2dof.png)


These formulas are used to calculate the frequency response functions shown in the simulation output.

---

## 🚀 Run the Model

1. Install dependencies (`numpy`, `matplotlib`, `scipy` and `math`)
```bash 
pip install requirements.txt
```
OR

```bash
pip install numpy matplotlib scipy math
```

2. Change the default input parameters in `primeSystem.py`

3. Use any Python environment (Python 3.9+ recommended) to run `main.py`:

```bash
cd Thesis.Py
python3 main.py
```

---

## 📈 Output

The script generates the following results:

- **Frequency Response of the Primary System (Untuned):**  
  Shows the baseline dynamic behavior without any vibration absorber.

- **Tuned System Responses Using:**
  - **Den Hartog Method:** for a range of mass ratios
  - **Lin Method:** for the same range of mass ratios
  - **Fixed Stiffness:** using both Den Hartog and Lin approaches

Each plot illustrates the vibration suppression effect of the TMD compared to the baseline system.  
The amplitude of the system's response is visualized over a frequency range from 100 to 600 Hz.

### 📉 Sample Output Plots

#### Den Hartog vs. Lin (Variable Mass Ratio \( \mu \))
![Den Hartog vs Lin](./figures/den_hartog_vs_lin.png)

#### Fixed Stiffness \( k_2 \) – TMD Optimization
![Fixed k2 Comparison](./figures/fixed_k2.png)



---

## 📚 Reference

This repository is based on analytical methods described in:
- **Chapter 7** of the thesis
- Classical mechanical vibration theory (2DOF systems)
- Den Hartog, J. P. (1956)
- Lin et al. tuning methods

---

## 👩‍🎓 Author

**Anna Keller**  
Master of Science in Biomedical Engineering  
Hochschule Furtwangen University (HFU), Germany 2024  

---
