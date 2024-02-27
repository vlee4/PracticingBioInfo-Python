__all__ = ['fasta_to_list']

'''
This script takes in a string containing fasta strings and returns a list of the fasta strings with the pre-fixing ">Rosalind_XXXX" label removed.
'''
import re

def fasta_to_list(str):
  delim = ">Rosalind_\d+"
  s = str.splitlines()
  joined = "".join(s)
  split_list = filter(None, re.split(delim, joined))
  return (list(split_list))

#### Testing

# fasta_strs = open('./String_Algos/consensus_fasta.txt', 'r')
# fasta_strings = fasta_strs.read()
# fasta_strs.close()

# print(fasta_to_list(fasta_strings))