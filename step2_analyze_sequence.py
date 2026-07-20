from Bio import SeqIO
from Bio.SeqUtils.ProtParam import ProteinAnalysis
import pandas as pd

print("=" * 55)
print("STEP 2: PROTEIN SEQUENCE ANALYSIS")
print("=" * 55)

record = SeqIO.read("data/inha_protein.fasta", "fasta")
sequence = str(record.seq)

print(f"\nProtein : {record.description[:55]}")
print(f"Length  : {len(sequence)} amino acids\n")

analysis = ProteinAnalysis(sequence)

print("-" * 40)
print("AMINO ACID COMPOSITION:")
print("-" * 40)

aa_composition = analysis.amino_acids_percent

for aa, percent in sorted(aa_composition.items(),
                           key=lambda x: x[1], reverse=True):
    bar = "█" * int(percent * 100)
    print(f"{aa}: {percent*100:5.2f}%  {bar}")

aa_df = pd.DataFrame({
    "AminoAcid": list(aa_composition.keys()),
    "Percentage": [v * 100 for v in aa_composition.values()]
})
aa_df = aa_df.sort_values("Percentage", ascending=False)
aa_df.to_csv("data/aa_composition.csv", index=False)

print("\n" + "-" * 40)
print("PROTEIN PHYSICAL PROPERTIES:")
print("-" * 40)

mol_weight = analysis.molecular_weight()
isoelectric = analysis.isoelectric_point()
instability = analysis.instability_index()
gravy = analysis.gravy()

print(f"Molecular Weight  : {mol_weight:.2f} Da")
print(f"Isoelectric Point : {isoelectric:.2f}")
print(f"Instability Index : {instability:.2f}")
print(f"GRAVY Score       : {gravy:.4f}")

print("\n📊 INTERPRETATION:")
if instability < 40:
    print("✅ Protein is STABLE")
else:
    print("⚠️ Protein is UNSTABLE")
if gravy < 0:
    print("✅ Protein is HYDROPHILIC (good drug target)")
else:
    print("⚠️ Protein is HYDROPHOBIC")

props_df = pd.DataFrame({
    "Property": ["Molecular Weight (Da)", "Isoelectric Point",
                  "Instability Index", "GRAVY Score", "Sequence Length"],
    "Value": [round(mol_weight, 2), round(isoelectric, 2),
               round(instability, 2), round(gravy, 4), len(sequence)]
})
props_df.to_csv("data/protein_properties.csv", index=False)

print("\n✅ Data saved to data/")
print("✅ STEP 2 COMPLETE!")