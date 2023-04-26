class DNA:
    def __init__(self, dna_seq):
        self.a = "a"
        self.t = "t"
        self.u = "u"
        self.g = "g"
        self.dna_seq = dna_seq

    @property
    def bases(self):
        bases = {char.upper():self.dna_seq.count(char) for char in set(self.dna_seq)}
        return bases

    def __len__(self):
        return len(self.dna_seq)

    def __str__(self):
        return f"dna sequence is {len(self)} bases long"
    
    def __add__(self, other):
        return "algo"

    def get_base_percentage(self):
        percentage = {char.upper():f"{(self.bases[char]/len(self))*100:.1f}%" for char in sorted(self.bases)}
        return percentage


def get_dna_seq(path):
    with open(path) as f:
        dna_seq = "".join(line.strip() for line in f.readlines())
        return dna_seq
    
dna_seq = get_dna_seq("dna_seq.dat")

ayoze = DNA(dna_seq)
print(ayoze.bases)
print(ayoze)
print(ayoze.get_base_percentage())