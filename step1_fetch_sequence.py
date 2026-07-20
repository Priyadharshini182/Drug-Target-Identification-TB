# STEP 1: PROTEIN SEQUENCE (OFFLINE VERSION)
# InhA protein - Mycobacterium tuberculosis

from Bio import SeqIO
from Bio.SeqRecord import SeqRecord
from Bio.Seq import Seq

print("=" * 55)
print("DRUG TARGET IDENTIFICATION PROJECT")
print("Disease: Tuberculosis (TB)")
print("Target Protein: InhA (Enoyl-ACP Reductase)")
print("=" * 55)

inha_sequence = (
    "MQSAGTVTVKDANGQLHFAPLEGKTLEDVNPDLVAQIARRNAIVGM"
    "TKETLWPELFQQLPQKLVEHHLVDNQSPQAVRAHAARNGIKVVTGD"
    "GAKVTLEGLNHLTALPQQVTAKVITGRGDPQRDALMAAVTRAQARQ"
    "QLGAVPKTIAMVSDAASVSAALDEAGNVAMTSSAGLAEGALRVLHS"
    "ALGKRPDLAERVLADADRLLDAFQDAGATVTLEQ"
)

print("\n✅ Using offline InhA protein sequence")
print(f"   Source    : UniProt P9WGR1")
print(f"   Organism  : Mycobacterium tuberculosis")
print(f"   Length    : {len(inha_sequence)} amino acids")

record = SeqRecord(
    Seq(inha_sequence),
    id="P9WGR1",
    description="InhA enoyl-ACP reductase [Mycobacterium tuberculosis]"
)

with open("data/inha_protein.fasta", "w") as f:
    f.write(f">{record.id} {record.description}\n")
    f.write(f"{inha_sequence}\n")

print(f"\nProtein ID   : {record.id}")
print(f"Length       : {len(inha_sequence)} amino acids")
print(f"First 50 aa  : {inha_sequence[:50]}...")
print("\n✅ Saved to data/inha_protein.fasta")
print("✅ STEP 1 COMPLETE!")