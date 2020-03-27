class FASTA:
    def __init__(self, FASTA_str):
        self.FASTA_arr = FASTA_str.split("\n")

    def code(self):
        return self.FASTA_arr[0].strip()

    def dna(self):
        return self.FASTA_arr[1].strip()
