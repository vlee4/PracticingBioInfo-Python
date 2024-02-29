# Given DNA strings in FASTA format, <= 10kbp
# Return the adjacency list, Ok, k = 3,
# (where a nodes, s and t are adjacent and the last k bases of s are the same as the first k bases of t)
# eg) one pair could be s= AAATAAA and t = AAATTTT
#                              ^^^         ^^^

# Approach 1: (After parsing) with the first string compare the last 3 bases with every other strand's 1st 3 bases. Repeat for each strand. Time O(n^2)

#Approach 2: Go thru all strings 1 time, making dictionaries of start seq and end seq, listing the FASTA id as values. Then, go thru all end strings, to see if there's matches with start seq. Pair those in an array. Transform the array and print. Time... a lot worse... O(n+n^3) not including parsing
import re
from utils.parse_fasta import fasta_to_dict

fasta = open('./Graph_algo/graph_fasta.txt', 'r')
fasta_strs = fasta.read()
fasta.close()

def compare_strings(fasta_dictionary):
  overlaps = ""
  for (key, val) in fasta_dictionary.items():
    suffix = val[-3::]
    for (next_key, next_val) in fasta_dictionary.items():
      prefix = next_val[0:3]
      if key != next_key:
        if prefix == suffix:
          overlaps = overlaps + f"{key} {next_key}\n"
  print("OVERLAPS", overlaps)


# start_seqs = {}
# end_seqs = {}

# def create_str_dicts(fasta_dictionary):
#   for (key, val) in fasta_dictionary.items():
#     prefix = val[0:3]
#     suffix = val[-3::]
#     # if prefix != suffix:
#     if not prefix in start_seqs:
#       start_seqs[prefix] = [key]
#     else:
#       start_seqs[prefix].append(key)
#     if not suffix in end_seqs:
#       end_seqs[suffix] = [key]
#     else:
#       end_seqs[suffix].append(key)

#   print("start", start_seqs)
#   print("end", end_seqs)

# def create_pairs(starts, ends):
#   overlaps = ""
#   for (end_key, end_val) in end_seqs.items():
#     if end_key in start_seqs:
#       start_strings = start_seqs[end_key]
#       for end in end_val:
#         for start in start_strings:
#           if start != end:
#             overlaps = overlaps + f" {end} {start} \n"

#   print("OVERLAPS", overlaps)
#   return overlaps

## Consider restructuring start_seqs and end_seqs for easier access
fasta_dict = fasta_to_dict(fasta_strs, delim=">")
compare_strings(fasta_dict)
# print(create_str_dicts(fasta_dict))
# print(create_pairs(start_seqs, end_seqs))
