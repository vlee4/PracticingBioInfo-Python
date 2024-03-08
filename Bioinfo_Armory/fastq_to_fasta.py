# FASTQ is an extension of a FASTA string which not only includes the sequence identifier and sequence, but also quality scores denoting Phred scores (scores representing confidence in the accuracy of the read base), offset by 33 and encoded by symbols from the ASCII table

#Given a FASSTQ file, this script will print the corresponding FASTA records

from Bio import SeqIO
try:
  from StringIO import StringIO # Python 2
except ImportError:
  from io import StringIO # Python 3

result = StringIO("")
SeqIO.convert("Bioinfo_Armory/fastq.txt", "fastq", result, "fasta")

print(result.getvalue())

# Test Input: 
# @SEQ_ID
# GATTTGGGGTTCAAAGCAGTATCGATCAAATAGTAAATCCATTTGTTCAACTCACAGTTT
# +
# !*((((***+))%%%++)(%%%%).1***-+*****))**55CCF>>>>>>CCCCCCC65

# Test output: 
# >SEQ_ID
# GATTTGGGGTTCAAAGCAGTATCGATCAAATAGTAAATCCATTTGTTCAACTCACAGTTT