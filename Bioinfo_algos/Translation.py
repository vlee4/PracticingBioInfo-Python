# Given an RNA string, s, corresponding to a strnd of mRNA, <=10kbp
# Return the protein str encoded by s

codon_table = {
  "UUU": "F",
  "UUC": "F",
  "UUA": "L",
  "UUG": "L",
  "UCU": "S",
  "UCC": "S",
  "UCA": "S",
  "UCG": "S",
  "UAU": "Y",
  "UAC": "Y",
  "UAA": "",
  "UAG": "",
  "UGU": "C",
  "UGC": "C",
  "UGA": "",
  "UGG": "W",
  "CUU": "L",
  "CUC": "L",
  "CUA": "L",
  "CUG": "L",
  "CCU": "P",
  "CCC": "P",
  "CCA": "P",
  "CCG": "P",
  "CAU": "H",
  "CAC": "H",
  "CAA": "Q",
  "CAG": "Q",
  "CGU": "R",
  "CGC": "R",
  "CGA": "R",
  "CGG": "R",
  "AUU": "I",
  "AUC": "I",
  "AUA": "I",
  "AUG": "M",
  "ACU": "T",
  "ACC": "T",
  "ACA": "T",
  "ACG": "T",
  "AAU": "N",
  "AAC": "N",
  "AAA": "K",
  "AAG": "K",
  "AGU": "S",
  "AGC": "S",
  "AGA": "R",
  "AGG": "R",
  "GUU": "V",
  "GUC": "V",
  "GUA": "V",
  "GUG": "V",
  "GCU": "A",
  "GCC": "A",
  "GCA": "A",
  "GCG": "A",
  "GAU": "D",
  "GAC": "D",
  "GAA": "E",
  "GAG": "E",
  "GGU": "G",
  "GGC": "G",
  "GGA": "G",
  "GGG": "G"
}


def translation(s):
  print("len", len(s))
  protein_str = ""
  stop_codons = ["UAA", "UGA", "UAG"]
  for i in range(0, len(s) - 1, 3):
    codon = s[i:i + 3]
    if codon in stop_codons:
      print("STOP", i)
      return protein_str
    protein_str = protein_str + codon_table[codon]

  return protein_str


mRNA = "AUGUUUGAUUUAUUGGGAAUUGCGGAUUUAAAGUUACUGUUGUCGGCCGUGGGGGCUAUUCUCCAACCGGGCAGUGGCAGUAGGCGUCAUACUCCUAUCCUCGGCCAAGCAUACAUCACGCCCAAAUAUUUCCCGUUUGAGUCUAGGCGGUCUCGAGACGGUCGUUGCAUUCUGUCUUUUGAUUACAUCAGCUGCGACGAGAGAUGCAGGUCAUCGGUACCGCGGUUGCCCUCUAGUUCGGGCGCAUUGUUCUCACUUUUGUUUUUCAUCGUUCUAUCUUAUUCUAAGCUGCUCCUUUACUUAUCCGUGAUCCCAGCUGAGCUUGUAAGCUUAGUGAACUUACGGAAUGCUAGCACCCGCCAAGUGACGCAUGGUUUCUAUGCCCAGACCUUCCAUGCUUCCAACAUACGUGUGGACCGGCACCACCACGUCUCCGGACAUCAUGCAGUGAAGAUUAGAUUCGCUACCCAAGCAUGUAUUGUAUCAAUAGGAUGGUCAAUCCGGAUGCCCGGCAAGGAGGAACGUGAGGGACUACUACUCGUAUUUCUGGAGAUCCUUUUGCCCAAAUCCGGAUGUCCGCCUUACCUUCAAAAGUCGGUGCGCAUGCGCGCUCCCCGUUGCCCAGUAGACGGAACCAAUUGCCGGAACGGGUAUAGCCUGGUUACCGUGUACCCAAGCGUUUCUGUACCAAUAGAUGGUCCCGCGGGUGCUACAAUAUCAAGGUAUCCACCAUCAAUACUGUAUUUUGUUUUUCUUUACCCCCACACAGCCCAUUCAUAUCCGCGGCCAUGCGGUGAAAACCAGCGAACGCAUUACCGUCCAAUAUCUUAUAGAGGAAAGGGUGCGCGUUGGAGCACGACUCCGAACAUAUGUACAGGAGCCGUACGGCUAGUGUAUCGCAUGUGCUGCUCAAUGAAUUUCUCGUUGCGCCAACAAUACUCCGAGUGCAUUCGUUUCUGCAAGAAUCCAGAUGUGGACAACUGCGGAAAAAUGACCCCCGCUCGUACGCUCAAAUUAUGCCAUUUAACGAAUCCGAGCCCUAAUCGUCCAUUCUGGGAGUGUUCAACGGUUCCACGCGAAUACUAUACUGGCUGGCAGAACUCCAAAUCUUCCUUUCCCGACUUUCCGCAGGAUAUUCGAAGCGAGACGGGAGUUUGCCGUUCCCGCAGGUCUGAGUGCAAAUGUGCCCCGCGACUCUGCAUGACGGCUAACCAUGUCAGAGAUAUACGGCUGCCCAGUCCUGACUCGACCCCGACGUGCGGGCCGCGUGAGAAAGUACGCCCAACCAGGAUCGAUCCGUUAAUAGUGGUUAUCGAGGAAUGCGGUUGUGAGUCGGCUAAUCUCUUCCAUUUUUAUACAACGGCAAUGGGAUGUGCACAGCCGGACACCUAUACUAUUUCCACGAGCUACUAUUGCCCCGUAUUUCCGCGAUACGGUGGGUAUUGUAAUCUGGCAGGUAGGGCCAAGUGUCGGAUCAGGACGAUAACUACGAUGCCGGUCAAGUGCGUUGCGUCAUGGCAGUUAUACCCUUUGAACAGGCGAGCCAAGCGAAGUCUACGCACUAUUAAGACGUUAUGUCGCAACCGACUCAAUGUGCGGACAAAGGGAAGACAGGAGGUCAGUGUUAGAGUGCAGCAGCGCUUUAUCGCUAGACCACUUACACCUUACAGCGUGAAGUUUGCGGUCGACCAGGUAACAUGUUAUUGCACCACGCCUGUUAUCAUGCCUCGCGUUUUCUUUACCACGAGUCGGGCAUUGAUCAGGCUUUUAGAACGGGUAGCUGUCUCGAUUUUAUGCUCGCGGCCCGUCGUGCUCGGGCUGUCAGCUCACAGCGGAUCCUUAGAAAGGGCUUCACUUGGUUCUAAAUACAGCAGUCGGCUUCCACUUCGUACAGUCACAGUUGUCGACACUAUCGGACUCAACGGAGUAACUUCCGAGUUGACCACACGCUAUUUCGUAAGUACUCCACCAACACGGACUACGGGGUUGGGUACUGCUUCCUUUCUGGGUGAAAAGGUUCGCGGAAGGGCUAGCGCGAACUCGAAUUUCGGGGCUGAACCCAUUUGGAACCUCGACGAUAGGAUUCUGUCCCCUGAUGUCUGCAUUGGACGUUUAACUCCGAACACUGUUACAUCGCUUACGACCCGAAUAGGACUCUUCGGCAACGCCGACUCGAAGGACGGUAUGUUCGAAGCCAUGGGCGACUGCCGCCUAUAUGAUUGUGUCCAGCCGGAGGAACAGGUAACUCCUCUUGCCUAUGCCUCUAAGAACCUAACGUUCAUGAGGGCUUUUGUUAAGAGUCGGGUCUACACACACGCGGCCGGUAGAUCUAGGCGAGCCGCUGACCGGUUUCAUCGUAUACGUUACUCGGUCCGUCGUAGUUCAGUGUUCAUUGGAAUGCCCAGCAGGGAACCUGAACCUAGUACCGCAAUGGUUCUCCAGAGACGAUGCCCCAAGAAUCUGGAUUGCACGAAUGAACUUCGUCUGCAAAAUCAUGUCGCCAGGCCGUGCUCGGUUGCUGCAAAAAUGCUGACGCGGCAGGUCAGGAGAACAGACUCAACUCCUACUUCGGGCAUGGCAUGGGGCAGCCGCUUUCUAUAUUGUCCGGGAGUAGAGGCGAAUCUGUCUCGAAGGCCAAGGGACUUCACUCGCUCUCGUAUAGUCAGGUUCAAUUUGAUUCAGCCGCGCCGUCGCAUGGAAAGCCGUGCUGAUUUAACAGCGCCGAGUGCGCUUUGCUUUCUUACUUGCCUGUCUCAUAUAGCCCACUACGGUGCCGCCCUAAGGGAUUAUGGCGAAAGCCAACUUAUGCCGCUUGAGAGGUCUAAUACAAGUGCAUCACAAGACAUCAAUCAAAACCAAUUAAUUCGGUUUGCUGCACUUUUAUUAUUGGCCGGAUUAAAACAGUCGGAUUGCCUAAAGUUGAUUUCUUGGAAGUGUGCAUGGACAAAUGAUGCGGCAAAGCACGUCACAUCUCGGACUACAACCACACGCGCAUCCGGAGCCGACGGAGAUAUAUGUAACGGAAUAAGAAGAAGAGUGAUAUACCAACUACGCCCUCGACUUCUAGGAUGUGCUAUACUAGCAAGCCAGGUCACACCUCAGUAUGUACCCGCAGUCUCAUCCUCCACUUUUUUAUGUGUCAUGCAACUAUCAGGUAAAAAGUGCGUGCGCCCCGUAGUGCCUCAACCCUACCGACUCCCGUGUCUUGGUAAUAUGAGAACCACAGCCCUUGAUUUCAAUCGCACGGCCUUCUGUAUUAUGUCCUUUUUUAGGAAGCCACCUGAACGAGAAUGCAUAACGGGGCCACUCAGCAAUCAAGUUUAUUCAAGGUGCUUGACAUCCACCGUAACCCAUAACAUAAAACGACGGCAUAUGAGUCUUUCUACUGCCUCAAUCUCGUUCCUCCUUGUACGGGGCUCCCUUCUACACUCAUCGUCGUCGGAAGGGACAAUUCGCAAGGCCUGGAACGUUUCCGUACAAUUCCUAACAUCCUCGUUGUUGCGCCGGGGUAAGGACUUUGCCCAGCCCCCCAGCCGGACUACGUGCCUCCCGCAGGAGGAGCGGGGGUGGGGCAGAUUCCUUGAAAAAUCAAAUGAGCUUGCAUGGAUUCGGGAUUUAGAAAGCGUCAACCGUCCCUUGGUAGCCGUGGUAGGGUCCCGUCGAAAAGCGUGCUCCGUACUGGGACUGGUGGAUAGCCCCGGUGAUAAAAACUACAGCCUCCCACCCAGAUGCACAGUGUUCGUCUCCGGCGUCAUCUUGCGAGCUCGAAUAAGGCGUUUAGAGAACCUCGACUUUUACGCUAAACUCUGUGGAAACCGAUCCUUACAUCACGGCGGGUUGAAAGUUAUGUUUGAAGCGGACGGCAGAGGGUCUCGAUGGAGCCGAGCCUUACGAGAGAACAGGUCAUUAGUACGGCUUACUAGGUGCCCUUGGAUAUUGAUCUCGGAUGGGCCUGUUUCGGCGUCAGCAUUGUGGUCGGAUUUCCGCAAUCGCCUCUACCUAUGUUCUAUGAGCCAACUCGACCGCUACCUCGGUACCGCUGAGACUAGGCGCAGAACCCACCUCAACCUGUUCCCAGUUUUACAAUUCACAGUAUACCCCAUUGGCAGCCCUAUGGAGAACAAUCAGCUGCUCACGGAUAGCCUCGCAAGUGAUCAACCGGGAGACAAUCAUCUGCUGUUAGGGACUACGGCUAUCGACUGUGACUCGCUACAUUCUAUUGUCAGAAUUCUACAGCAGCUAAACACAGCAAAUCGUGCACUCUUAAGAGACUCGAGUGAUCCUGUCGAAGCUGCCCGUGCAGGCAAAGGGCGGAUCCUUAUUCACGAAAAUGAAAAGCCGUGGCGGAGGAGUAGCAGUGCAUCACUUAGGAACGCUCACUCAUAUGCAGUGAAGCCGUCAUUGGGCCUCAUUAACGUACAGCUGCCUUGUCGCGUACGCCGCUUAGUAAUAUUCUGUGGGACAAAUAUUAUGCGCCCAGCCGGCAGCAGAAUAAGACCAAAUAGGGGUCGACACUUAGCGUCUACACUGUGUAGCCUGCUAAUGACAAAUCUCGUGUCAGAACUGAUGGGGCUACGCCGUGCGUCAGUAUAUGGCGUUUCUUCUUUCCCCGCCAGGCAUUCGGCUUAUAACGGCCAAGAUGCCCCUCCUCGUCCCGGACGGCUCGUCCCUAAUAUCCAACAAUUUAUCCUCAUAACCAUAAGCGGACGCCCUCGAAGACAUUUUCACUUGGGUGAACCACCCUCGUGUCGGCCGAGCUACUUAACGGAAAAUCAACCAGGUCCGAUUUUUGAUCGCCGAAGGCGGCGGAGACCUCUUUCGGAAUGGGCUGUGCGGGGUCUAUUCGCGGCCAAUUUCAUGGGUACAAUGGACAUUGGAAGGAUCGUUAGCCGUGAUCAUCACGCCGACCGGAGAAACCCCAUGACCGGUGUUAAUGAUUCCGCUGCUUUAGUCAAUACAGGCUAUAUUAUUGUGGGCCCGAGUCUGCAGGGAUUUAGAUUAUACCAAUCCGCGUACUACACGGCGGCAUAUCGUCCCGAUAGAUGGAGGAGCCAGCCGUUGCUAUAUAGGGUCCAUACGUGUAAGCAAGGCCUAAACGACCUCGUUCGGCGCUCUGUAUCAGGUUGGUGGGUACCCCCAGGCAGAGUGAUUAAUCGAUAUAAUUCUCCAUCUAGAAUCUCCUCUGAAUCUAUCUCAGCAUCUGAACGUACACAUGACUCUGUGGACUUUGAUUGUGGGACACAGCGCGGCGAAGUAGAAGCCAAUUCCGAUCUUUAUGGUGUACCCCCUUAUCUACAGGAUUCGAAUUGUUACAGUUUGCUUCCACCGAAUAGAUUCAUAGACUACCUGUCUCGGCUUCGUAGGGUAGUAACAGGUUCCGGUAAGCCUUACGACAACAGACACUAUAGGGUGAACCUGUUCGGGAAGCAAUAUUCGAGGAGAAUGCGAGACUCCUCAUUAGUCUCCCGAGGGCUACCCGUGUCGGAAACGAGUAUUCAAUCAGUAGACCGCCGGGAUACGCCGUGGAGCAGAGUUGGUGCAAACGGGGACGUUGAAACGAAACUGCAACUCGACCCAAGCUAUAUCUCAUUUGCGUUUGCGGCCGAUAUACGGUGUCAGGCCGACCGACCAGCGGCGCAAAGGUAUCGUUCCACCGUAGAGUCUAAAUUGCAACAUACGCUGAAGGAGGACACCUGGCCAUUAAAGUAUGGGUCUAUUAUGUCCGUGAUCCGGUGCGACACCGCUCAGAGUUGGCUUUCGUGGCGACGAAGAGAGAUCUCUUCGGGGGUUGUCAGUUAUUUACUAUCGAACUUAUUACCAUACCACAUACCUCACCCAUCACAACAACAGUUCCCAGCAUCGUACACAGGCCUACGCACGUCAAAUGGGCUGUGGCGGUCUGUAAUGAGUUGUCUAACAUACGACGGCGUGCGUGCUAAAACAGCAUCAGUGCUCUAUACUCGGAACACGGACCAUAAGGCUCUUGACGACGAGGCAAUAAUGCCAGGCUCUAAGGGCCCAAAUAGACCACCUGGAGCCCGACUUGGCCAGUGCUUCCGCGUAGUCUUUGUAACCCUAGGUCUGGCAGCUGCCCAGUUGUCACCUGCCCUUCACGUGCAGAUCCUUACUGCACUCAAAUCUUGCGAUUUUACAUACACAGAGAGUGGACAGGACCCCUCAAUUAGUCGUGGGAGUAGGGUCAUAUUCAGUCCAGAUCAAAUUAGAUACCGGGUUGCAUACGAACUAACUACCAGCGGCGAAAUUCCCUUACCUUCUUCAAAGCCAUCUUCAUGUAGGCCACCCAUCCGCGGACGUGUCGACUUAGGAGGGAUGCUGAUUCAUACUAAUAAACUAUCACCUCUGACACCGUCUUUCUUAAACUGUUAUCUCCACGAUCUCAGUGCGCUUAGCUGGGCCUUGCCGAUGACCAAUCGAGGACGAUAUGAUCGAGAUAUAAGUACAUUCUAUGUAGCAGUAGUGAAUCAUUCAGGGAGGUGUGGAGCUCGCGGGAUGUCCGUGGUGUUUACGGCUCGCACCCAAGUAGUUUCCGAGUCCUUUCAUCAGCACGGAUCGUUCGUUACGCUAGUGUUCUCUUUGAAGGUUAUUAGAACAUUAUUCAGGCCCUUUACUUUCCGCCAUUUUGGGAACCGUUUGCUCUAUGAGACCUGUCGUAGGAUGCAACCCGAAUUUAAGUCGGUUAGCCUCUCUACCACCAGAAGCAGUUCGCGGCUAAGUUGUAGUGCAUCCUCGGUGCAUUCUUUGUUCUUGGGUUUCAUUCUCCUAACUAAGGGCCCCGUUCACGUUUUCCUAUUUCUUAGCCCAAGGCGGGGGAUGCGUGAACCCGGGUGUGAUACAGCCGGGUUCGGUUGUGGCUACAUGAAGCUCGCUCCGAUAGAGAAGGUUCGUCAUCACGCGGGCCAUGGGUGCUUUAAGACGCUUUGGCAACCGCACAGGAGCCCGGGCGUCGCUCGUGGCCACGAUCAGACGACAGAUCCUUUCGUAAGCAUGCCUGCAAAUACAAACCGCUCAGGCUUCUAUAAACAAAUUGAGAGCACCUCCUCCGUGGUAAGAGCUAGAAACGCGUUUCGAAUUAAAAAAGUGCACAUUCAUCGCGCACCGCGACUUGGCUGCUCUGGACCGUGUGACGAAUCAGGGGCAACCUGUCGGGACUUACAUCUGGACACGAGUAAAUUCCUCAGGGUGGGUAUAUUUUUUAUUAACCGACGGUGUGUUCCGCUUGGUCUACUCGGGGGAACUUCAGACCUCGUAAAUAAUACUGACAGGCGAUCGUCCAUAACAAAUGGUGCAACUGGGGAAGCCAACACCAAGUUGGCUUGGCGGGAUCUCGGGAACUUUCUUGUCAGGCCGCUAUCAUCACAAACGUACGUUCUUUUGGUAAGGCGUAACCCAGCAAACGAGAGACCGAUGGGUCAUCCGCAGGAGGACCCUUGGGUAAUAUCGACUCUCCAUUAUCCCUUCGACUCUCAUCAUUGCUUGCGCCAUUCCUUAGUUUUCCAUGGUCCCUUCACUGUGACGUCGAUCCGGCAGGAGCUUCAGACGCGACCACUUUUGGCGUACCGGAAUGUAACCGAACCGACUAAAGUCGCCAAACCGUCGUAUUGUAUCAUUCAAUCGCAUAGAUAUUUAUUUGCUUCUAGCAGUGACACUCUUGACCCCCAACGAAACACCCAUCUCCAAGUAGAAGCUCAACGCAGAGCUGACCCACAGGUACAGGUGCUUAGAAACCCAGUCCUGGUGGUCCGAGCGGCAGCCUUCACCCCGCGAAGGGUCUCUGUAUCUUCUAGCGCAAUCUAUGCUAAGGCCGACGUCCGAGAUCAGCAGGCUUUGUUACCCAUCAAUAUUGUGUCACCACGCAUACUCACGUGUUCGCGCGACUGUAGCCGCCCUGAAUUCGCUACCAUGGUUGUCCACACUGAAGUAACGUGGCCACUACGCGUUUCAACCCACGAUAGAGGCGGAUUCCGCGGUCAAUCCGGACACGGAAUCAUUAUAACAAGUCUACCUAAUCUGGAUGUUCCACCACACUCCCAUGAGGGUUCUACAGCCGGUAGCUGGGGCUCUCUACCUCCCUUUUACGUCGCACCCUUUAUUGAUGUGGGAAAUAGGGGCCCAAUCCCGGAAUCCCCGCGUAUCCCACCGAUCAAUACUCCACUAGGAGUUGUCAAGUGGAUCCAGAUAAUAUUACUGCCCUGCAUUGGCGCAUCUGAUCAAUAUAACAUCGUUUCUCCUACGGCUUCCGCGUGGAAUAAGAUGUUCUCUUGUCUUAAUAAGAGGUUCACUUGCCGGUGCACUACAGCCACGAACAUCUUAAUGACAUGGUCACUGGGUCAACAAUUCGUCCAUAUGUUACCAUACGUCUUUGAGGCCGUACUAGCUCCUUACACAGUUUAUAAGUAUGGACGUAACCCUCCAUGUAGGCCCCGACUGAAUGCAAAGAGUGAGUACCCACUCCACUCCCGAUUCCAUAAGUCGCAUUGUGAUUCCGGUCUCAUGCUAGGUUGCCACGCGCACAACGGUUGUAUCUCGCCUAAAAGCUAUGAUUGUUGGGGCAGGAAACUGCACGCCCUGGUGCCUAGCACGCUGACGCUUGGGCGGGACACCACUCAAAUAGCGUACGGCGUGACAAAGAUGCAUAAGACGCAGAUAUUGUGUAUUAGGCUGCUGUCUCCUUCAUACCGUCAAGAAGAGCAACACAUUUUCAAACUGUAUGCAGCUGGGACCGAAUCGAGAAACGAGCGAUAUUAUAAGCCUUUUACUUGGAACUGCUCACCUCAGAUCCCUACUUCAUUGGGGGACGCAUACCGCGGUAGUCGCCUCUCGCUCAUACUACGUAUGUCCAAUCACGGUCAGAGAGUUACUUUGCCGGAUAGAUCCAAGUUCAUGGGGCCUGUGUUUCUUUCACUACUCGCCUCAUCGCUAGAAGCGGGGACGGAGAGAGUGUCGCUAGGCCGCUUGGAACGCUGCUUGGAUGGCUAUUCUUUCCUCCUGAUCUCUGACCUCUGCAACCUAAAACUUGUGAAGGUUGCCAAAAAACGUACAAACCAAGAGCAACGCAUCAAACGACUCCCCCGAAAUACCGGGACACAGGCUCGCGGUCAAAUCGCCUGGCACGAACCGCCUCGUUAUUUUGACUAG"

print(translation(mRNA))
