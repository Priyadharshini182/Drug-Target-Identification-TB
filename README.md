# Drug Target Identification - Tuberculosis 🧬💊

## Overview
Computational identification and characterization of 
InhA protein as a validated drug target in 
Mycobacterium tuberculosis using Python, Biopython and R.

## Disease
Tuberculosis (TB) - WHO Global Priority Disease

## Target Protein
**InhA (Enoyl-ACP Reductase)**
- UniProt ID: P9WGR1
- Organism: Mycobacterium tuberculosis H37Rv
- Length: 218 amino acids
- Existing Drug: Isoniazid (INH)

## Tools & Technologies
| Tool | Purpose |
|------|---------|
| Python 3 | Pipeline scripting |
| Biopython | Sequence analysis |
| ProtParam | Physicochemical properties |
| pandas | Data handling |
| NCBI/UniProt | Protein databases |
| BLAST | Sequence similarity |
| R + ggplot2 | Visualization |

## Project Files
| File | Description |
|------|-------------|
| step1_fetch_sequence.py | Protein sequence retrieval |
| step2_analyze_sequence.py | Physicochemical analysis |
| step3_blast_search.py | BLAST similarity search |
| step4_visualization.R | R chart generation |
| step5_report.py | Final report generation |
| data/inha_protein.fasta | Protein sequence |
| data/aa_composition.csv | Amino acid composition |
| data/protein_properties.csv | Physical properties |
| data/blast_results.csv | BLAST results |

## Key Results

### Protein Properties
| Property | Value | Interpretation |
|----------|-------|----------------|
| Molecular Weight | 22938.81 Da | Medium-sized protein |
| Isoelectric Point | 6.06 | Slightly acidic |
| Instability Index | 23.21 | STABLE (< 40) |
| GRAVY Score | -0.1055 | HYDROPHILIC |

### BLAST Results
| Metric | Value |
|--------|-------|
| Best Identity | 100% (M. tuberculosis H37Rv) |
| M. bovis Identity | 99.3% |
| E. coli Identity | 46.3% |
| Average Identity | 74.3% |

## Visualizations
1. Amino acid composition bar chart
2. BLAST sequence identity chart
3. E-value significance plot

## How to Run

### Step 1: Install dependencies
```bash
pip install biopython pandas
Step 2: Run Python scripts
python step1_fetch_sequence.py
python step2_analyze_sequence.py
python step3_blast_search.py
python step5_report.py
Step 3: Run R visualization
install.packages(c("ggplot2","dplyr"))
source("step4_visualization.R")
Conclusion
InhA is confirmed as a validated drug target because:
Protein is STABLE (low instability index)
Protein is HYDROPHILIC (accessible for drug binding)
Highly conserved across Mycobacterium species
Low similarity with human proteins (safe drug target)
Already targeted by existing TB drug Isoniazid
Author
Priyadharshini A
B.Tech Biotechnology| DSU Trichy
priyadharshinidharshini16378@gmail.com
