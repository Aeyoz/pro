from __future__ import annotations
from pathlib import Path

class DNA:
    ADENINE = "A"
    THYMINE = "T"
    CYTOSINE = "C"
    GUANINE = "G"
    nitrogenous_bases = [ADENINE, THYMINE, CYTOSINE, GUANINE]
    def __init__(self, dna_seq):
        self.sequence = dna_seq
    
    @property
    def bases(self):
        bases = {char.upper():self.sequence.count(char) for char in sorted(set(self.sequence))}
        return bases

    @property
    def adenines(self):
        return self.bases[DNA.ADENINE]

    @property
    def thymines(self):
        return self.bases[DNA.THYMINE]

    @property
    def cytosines(self):
        return self.bases[DNA.CYTOSINE]

    @property
    def guanines(self):
        return self.bases[DNA.GUANINE]

    def __len__(self):
        return len(self.sequence)

    def stats(self):
        percentage = {char:round((self.bases[char]/len(self))*100, 3) for char in self.bases}
        return percentage

    def __str__(self):
        return self.sequence
    
    def __add__(self, other: DNA) -> DNA:
        new_dna_seq = "".join(max(base, base2) for base, base2 in zip(self.sequence, other.sequence))
        if len(self) == len(other):
            return DNA(new_dna_seq)
        longuest_dna_seq = max(len(self), len(other))
        shortest_dna_seq = min(len(self), len(other))
        new_sequence = self.sequence if len(self) == longuest_dna_seq else other.sequence
        new_added_length = longuest_dna_seq - shortest_dna_seq
        new_dna_seq += new_sequence[new_added_length:]
        return DNA(new_dna_seq)

    def __mul__(self, other: DNA) -> DNA:
        return DNA("".join(base for base, base2 in zip(self.sequence, other.sequence) if base == base2))

    def __getitem__(self, index: int) -> str:
        return self.sequence[index]

    def __setitem__(self, index: int, value: str):
        value = self.ADENINE if value not in self.nitrogenous_bases else value
        dna_seq = list(self.sequence)
        dna_seq[index] = value
        self.sequence = "".join(dna_seq)

    @classmethod
    def build_from_file(cls, file_path: Path) -> DNA:
        with open(file_path) as f:
            dna_seq = "".join(line.upper().strip() for line in f.readlines())
        return DNA(dna_seq)

    def dump_to_file(self, file_path: Path):
        with open(file_path, "w") as f:
            f.write(self.sequence.upper())