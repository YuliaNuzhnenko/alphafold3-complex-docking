#!/usr/bin/env python3
"""
AlphaFold DB 3D Structure & PAE Error Matrix Evaluator
Real Data Processor for Human Tumor Suppressor p53 (UniProt ID: P04637)
Author: Yulia Nuzhnenko
"""
import os
import json
import urllib.request
import numpy as np

UNIPROT_ID = "P04637"
PAE_URL = "https://alphafold.ebi.ac.uk/files/AF-P04637-F1-predicted_aligned_error_v6.json"

def fetch_alphafold_pae_matrix(uniprot_id=UNIPROT_ID):
    """
    Downloads real predicted aligned error (PAE) JSON matrix directly from AlphaFold EBI DB API.
    """
    req = urllib.request.Request(PAE_URL, headers={'User-Agent': 'Mozilla/5.0'})
    with urllib.request.urlopen(req) as res:
        data = json.loads(res.read().decode('utf-8'))[0]
    pae_matrix = np.array(data["predicted_aligned_error"], dtype=float)
    return pae_matrix

def analyze_domain_pae(pae_matrix):
    """
    Analyzes domain-specific PAE confidence for Human p53 (393 amino acids):
    - Transactivation Domain (TAD): Residues 1 - 92
    - DNA-Binding Domain (DBD Core): Residues 93 - 292
    - Tetramerization Domain (TET): Residues 325 - 356
    """
    dbd_pae = np.mean(pae_matrix[92:292, 92:292])
    tad_pae = np.mean(pae_matrix[0:92, 0:92])
    overall_pae = np.mean(pae_matrix)
    min_pae = np.min(pae_matrix)
    
    return {
        "overall_mean_pae": float(overall_pae),
        "min_pae": float(min_pae),
        "dbd_core_pae": float(dbd_pae),
        "tad_disordered_pae": float(tad_pae),
        "seq_len": pae_matrix.shape[0]
    }

def main():
    print("==================================================")
    print(" AlphaFold DB Structural PAE Evaluator")
    print("==================================================")
    print(f"Fetching real PAE confidence matrix from AlphaFold EBI DB for UniProt {UNIPROT_ID}...")
    pae = fetch_alphafold_pae_matrix(UNIPROT_ID)
    metrics = analyze_domain_pae(pae)
    
    print(f"Target Protein: Human Tumor Suppressor p53 (UniProt: {UNIPROT_ID})")
    print(f"Sequence Length: {metrics['seq_len']} residues")
    print(f"PAE Matrix Dimensions: {pae.shape[0]} x {pae.shape[1]}")
    print(f"Minimum PAE Error: {metrics['min_pae']:.2f} Angstroms")
    print(f"Overall Mean PAE Error: {metrics['overall_mean_pae']:.2f} Angstroms")
    print(f"DNA-Binding Domain (DBD 93-292) Mean PAE: {metrics['dbd_core_pae']:.2f} Angstroms (Structured Core)")
    print(f"Transactivation Domain (TAD 1-92) Mean PAE: {metrics['tad_disordered_pae']:.2f} Angstroms (Intrinsically Disordered)")

if __name__ == "__main__":
    main()
