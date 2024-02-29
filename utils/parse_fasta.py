__all__ = ['fasta_to_list', 'fasta_to_dict']
'''
These util functions are used to convert a string of combined fasta strings into another structure of fasta strings.
'''
import re


def parse_fasta_str(str, delim=">Rosalind_\d+"):
  s = str.splitlines()
  joined = "".join(s)
  split_list = filter(None, re.split(delim, joined))
  return split_list


def fasta_to_list(str, delim=">Rosalind_\d+"):
  parsed = parse_fasta_str(str, delim)
  return (list(parsed))


def fasta_to_dict(str, delim=">Rosalind_\d+"):
  fasta_dict = {}
  parsed = parse_fasta_str(str, delim)

  for dna in parsed:
    key = dna[0:13]
    val = dna[13::]
    fasta_dict[key] = val

  return fasta_dict


#### Testing

# fasta_strs = open('./String_Algos/consensus_fasta.txt', 'r')
# fasta_strings = fasta_strs.read()
# fasta_strs.close()

# print(fasta_to_list(fasta_strings))
