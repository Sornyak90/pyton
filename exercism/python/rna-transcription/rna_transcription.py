def to_rna(dna_strand):
    dnk = ('G', 'C', 'T', 'A')
    rnk = ('C', 'G', 'A', 'U')
    result= ""


    if dna_strand != "":
        for dna in dna_strand:
            inx = dnk.index(dna)
            result += rnk[inx]

    return result


print(to_rna("ACGTGGTCTTAA"))
