# AlphaFold Structural Confidence & PAE Matrix Evaluator 🧬⚡️

[![Domain](https://img.shields.io/badge/Domain-Structural%20Biology-00f0ff?style=flat-square)](#)
[![API Data Source](https://img.shields.io/badge/API-AlphaFold%20EBI%20DB-7000ff?style=flat-square)](https://alphafold.ebi.ac.uk/entry/P04637)
[![Python](https://img.shields.io/badge/Python-3.9%20%7C%203.10%20%7C%203.11-green?style=flat-square)](#)
[![CI Test Suite](https://github.com/YuliaNuzhnenko/alphafold3-complex-docking/actions/workflows/ci.yml/badge.svg)](https://github.com/YuliaNuzhnenko/alphafold3-complex-docking/actions)
[![License](https://img.shields.io/badge/License-MIT-blue.svg?style=flat-square)](LICENSE)

A structural bioinformatics evaluation module that fetches real 3D prediction confidence metadata directly from the **EMBL-EBI AlphaFold DB REST API**.

Parses predicted aligned error (PAE) matrices to evaluate domain-specific confidence, structured core rigidity, and intrinsically disordered protein regions.

> [!NOTE]
> **Scope & Positioning Notice**: This repository is a lightweight Python evaluation toolkit for parsing predicted aligned error (PAE) matrices and domain confidence metadata from AlphaFold DB / AlphaFold predictions. It does NOT execute GPU-heavy molecular docking or AlphaFold server model generation locally.

---

## 📑 Table of Contents

- [Public Dataset \& API Source](#-public-dataset--api-source)
- [Usage \& Executable Python API](#-usage--executable-python-api)
- [Actual Executed Console Output](#-actual-executed-console-output)
- [Domain Metrics Breakdown](#-domain-metrics-breakdown)
- [License](#-license)

---

## 🔗 Public Dataset & API Source

- **Target Protein**: Human Cellular Tumor Antigen p53 (`UniProt ID: P04637`).
- **AlphaFold DB Record**: [`AF-P04637-F1`](https://alphafold.ebi.ac.uk/entry/P04637)
- **Direct PAE JSON API URL**: [`https://alphafold.ebi.ac.uk/files/AF-P04637-F1-predicted_aligned_error_v6.json`](https://alphafold.ebi.ac.uk/files/AF-P04637-F1-predicted_aligned_error_v6.json)

---

## 💻 Usage & Executable Python API

```python
from scripts.evaluate_af3_complex import fetch_alphafold_pae_matrix, analyze_domain_pae

# Fetch real 393x393 PAE matrix from EBI AlphaFold DB for UniProt P04637
pae_matrix = fetch_alphafold_pae_matrix("P04637")

# Analyze domain-specific PAE confidence scores (in Angstroms)
metrics = analyze_domain_pae(pae_matrix)

print(f"Overall Mean PAE: {metrics['overall_mean_pae']:.2f} Angstroms")
print(f"DBD Core Domain PAE: {metrics['dbd_core_pae']:.2f} Angstroms")
print(f"TAD Disordered Domain PAE: {metrics['tad_disordered_pae']:.2f} Angstroms")
```

---

## 🖥 Actual Executed Console Output

When running `python scripts/evaluate_af3_complex.py`:

```text
==================================================
 AlphaFold DB Structural PAE Evaluator
==================================================
Fetching real PAE confidence matrix from AlphaFold EBI DB for UniProt P04637...
Target Protein: Human Tumor Suppressor p53 (UniProt: P04637)
Sequence Length: 393 residues
PAE Matrix Dimensions: 393 x 393
Minimum PAE Error: 0.00 Angstroms
Overall Mean PAE Error: 20.59 Angstroms
DNA-Binding Domain (DBD 93-292) Mean PAE: 3.69 Angstroms (Structured Core)
Transactivation Domain (TAD 1-92) Mean PAE: 22.43 Angstroms (Intrinsically Disordered)
```

---

## 📊 Domain Metrics Breakdown

- **DNA-Binding Domain (DBD, Residues 93-292)**: Low PAE (**3.69 Å**), indicating high structural rigidity and folded core stability.
- **Transactivation Domain (TAD, Residues 1-92)**: High PAE (**22.43 Å**), quantitatively identifying intrinsically disordered N-terminal activation domain.

---

## 📄 License

Distributed under the MIT License. See [`LICENSE`](LICENSE) for details.
