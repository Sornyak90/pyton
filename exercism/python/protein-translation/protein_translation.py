def proteins(strand):
    DNA = {
            "AUG" : "Methionine", 
            "UUU" : "Phenylalanine",
            "UUC" :	"Phenylalanine",
            "UUA" : "Leucine",
            "UUG" :	"Leucine",
            "UCU" : "Serine",
            "UCC" : "Serine",
            "UCA" : "Serine",
            "UCG" :	"Serine",
            "UAU" : "Tyrosine",
            "UAC" : "Tyrosine",
            "UGU" : "Cysteine",
            "UGC" :	"Cysteine",
            "UGG" :	"Tryptophan",
            "UAA" : "STOP",
            "UAG" : "STOP",
            "UGA" : "STOP"
    }
    result = []
    for i in range(0,len(strand),3):
        if strand[i:i+3] in DNA and DNA[strand[i:i+3]] != "STOP":
            result.append(DNA[strand[i:i+3]])
        elif DNA[strand[i:i+3]] == "STOP":
            break

    return result
            
print(proteins("UGGUAGUGG"))
