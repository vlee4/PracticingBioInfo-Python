# Given 2 DNA strings, s & t, where t is a substring of s
# Return all locations of t as a substring of s
# Position within s should be 1-based, meaning that the 1st char in s would be s[1]


def findMotif(s, t):

  occurances = ""
  t_length = len(t)
  i = 0
  while i + t_length <= len(s):

    if s[i:i + t_length] == t:
      occurances = occurances + f' {str(i + 1)}'
    i += 1

  return occurances


a = "CAGGAACCGAGGAACCTGAGGAACCCTTAATTAGGAACCCTAGGAACCAGGAACCATCTAGGAACCAAGGAACCGTCCGAAGGAACCAGGAACCGAGGAACCAGGAACCTGCCGCAGGAACCTTGTCGGAGGAACCAAGGAACCTAGGAACCATTGTACAGGAACCGCCGAGGAACCAAGGAACCTGCCAGGAACCTAGGAACCAGGAACCAGTCCAGGAACCGCCCAAGAACAGGAACCAGCTAGGAACCAGGAACCGACGAAGGAACCAGAGGAACCAGCTAATAGGAACCTCCTTAGGAACCCCGTTGAGGAACCGCAGGAACCTTGTGAGGAACCTGACCCTGAGGAACCATAGACAGGAACCATGGGAAGGAACCAGGAACCGAGGAACCAGGAACCCAGGAACCTTGGGTCGGCTGAGGAACCAGGAACCCACTCAGGAACCGCTCGAGGAACCAGGAACCAAAAGGAACCAGGAACCCAGGAACCTTAGGAACCGGCGAACAGGAACCTCCAGGAACCTCTCCAGGAACCCAGAGGAACCTTTAGGAACCCTGGTTAGAGGAACCGACCCAGGAACCAAGGAACCTGGAAGACTATTAGGAACCAGGAACCAGTTAGGAACCAGGAACCAGGAACCTTCACGAGGAACCGGTAGGAACCCAGGAACCTCAGGAACCCGAGGAACCCAGGAACCTGAGGAACCGCGACCGAAGGAACCGCTCATAATGAGGAACCCAGGAACCCAAGGAACCAGGAACCTACTTTAGGAACCGAGGAACCCAGGAACCCGCAGCAGAGTGGTCACAGGAACCAGGGAAGGAACCGCAAGGAACCCTCCAGGAACCTAGGAACCAGGAACCGAGGAACCAGGAACCTGGCCTAGGAACCTTAAGGAACCTCGCAGAATGCCGAGGAACCAAGGAACCACAGGAACCGAGATTAGAAAGGAACCGCA"
b = 'AGGAACCAG'

print(findMotif(a, b))
