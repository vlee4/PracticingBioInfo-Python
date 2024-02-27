# Given 10 DNA strings of equal length, <=10kbp in FASTA format
# Return a consensus string and profile matrix for the collection. (If there's several possible consensus strings possible, than return any of them)
import re
from utils.parse_fasta import fasta_to_list

# Read & parse FASTA strings

fasta_strs = open('./String_Algos/consensus_fasta.txt', 'r')
fasta_strings = fasta_strs.read()
fasta_strs.close()

# Create dictionary of strings representing the occurance of each nt at i position in the given dna strings
def create_profile(dna_strs):
  profile = {
    'A': [0 for x in range(len(dna_strs[0]))],
    'C': [0 for x in range(len(dna_strs[0]))],
    'G': [0 for x in range(len(dna_strs[0]))],
    'T': [0 for x in range(len(dna_strs[0]))]
  }

  for dna in dna_strs:
    for i in range(0, len(dna)):
      lt = dna[i]
      profile[lt][i] += 1

  return profile


# From the profiled dna strings, create a consenus string that reports the most frequent nt at each position
def reach_consensus(profile):
  # print("prof", profile)
  consensus = []
  key = {0: "A", 1: "C", 2: "G", 3: "T"}
  for i in range(0, len(profile['A'])):
    column_list = [
      profile['A'][i], profile['C'][i], profile['G'][i], profile['T'][i]
    ]
    max_lt = column_list.index(max(column_list))
    consensus.append(key[max_lt])

  consensus = ''.join(consensus)
  return consensus


# Display profile matrix by letter with space-separated occurances
def format_profile(profile):
  for key, value in profile.items():
    joined_val = " ".join(str(n) for n in value)
    print(f'{key}: {joined_val}')


# Parse and clean given FASTA strings so we can have an iterable list
parsed = fasta_to_list(fasta_strings)

prof = create_profile(parsed)
print("consensus", reach_consensus(prof))
print(format_profile(prof))
