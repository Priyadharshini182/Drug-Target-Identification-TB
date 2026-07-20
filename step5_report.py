import pandas as pd
from datetime import date

print("=" * 55)
print("GENERATING FINAL PROJECT REPORT")
print("=" * 55)

aa_data    = pd.read_csv("data/aa_composition.csv")
props_data = pd.read_csv("data/protein_properties.csv")
blast_data = pd.read_csv("data/blast_results.csv")

print("\n")
print("=" * 55)
print("DRUG TARGET IDENTIFICATION - PROJECT REPORT")
print("=" * 55)
print(f"Date          : {date.today()}")
print(f"Disease       : Tuberculosis (TB)")
print(f"Target Protein: InhA (Enoyl-ACP Reductase)")
print(f"Organism      : Mycobacterium tuberculosis")

print("\n--- PROTEIN PROPERTIES ---")
for _, row in props_data.iterrows():
    print(f"  {row['Property']:30s}: {row['Value']}")

print("\n--- TOP 5 AMINO ACIDS ---")
for _, row in aa_data.head(5).iterrows():
    print(f"  {row['AminoAcid']}: {row['Percentage']:.2f}%")

print("\n--- BLAST RESULTS ---")
print(f"  Best Identity : {blast_data['Identity_pct'].max()}%")
print(f"  Avg Identity  : {blast_data['Identity_pct'].mean():.1f}%")
print(f"  Total Hits    : {len(blast_data)}")

print("\n--- CONCLUSION ---")
print("  InhA is a validated drug target in M. tuberculosis.")
print("  Stable, hydrophilic protein conserved across species.")
print("  Existing drug Isoniazid targets this protein.")
print("=" * 55)

report_text = f"""
DRUG TARGET IDENTIFICATION - PROJECT REPORT
Date: {date.today()}
Disease: Tuberculosis (TB)
Target Protein: InhA (Enoyl-ACP Reductase)

PROTEIN PROPERTIES:
Molecular Weight: {props_data.iloc[0]['Value']} Da
Isoelectric Point: {props_data.iloc[1]['Value']}
Instability Index: {props_data.iloc[2]['Value']}
GRAVY Score: {props_data.iloc[3]['Value']}

BLAST RESULTS:
Best Identity: {blast_data['Identity_pct'].max()}%
Avg Identity: {blast_data['Identity_pct'].mean():.1f}%
Total Hits: {len(blast_data)}

CONCLUSION:
InhA is a validated drug target in M. tuberculosis.
Stable, hydrophilic protein conserved across species.
Isoniazid targets this protein.
"""

with open("output/project_report.txt", "w") as f:
    f.write(report_text)

print("\n✅ Report saved to output/project_report.txt")
print("✅ PROJECT COMPLETE!")