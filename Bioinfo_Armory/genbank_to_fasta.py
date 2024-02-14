# Withini the Biopython module, Entrez is a data retrieval system that allows you (via the .efetch method) to search any of NCBI's databases
# .efetch takes a variety of arguments including "db" and "term" argument, referring to the DB you want to search (nucleotide = GenBank; pubmed = PubMed), and the query you want to search for, respectively.
# .efetch can also take an "id" argument which is a list of IDs to search for, and a "rettype" argument that takes the data format to be returned.

# The SeqIO module provides an interface to input & output methods for different file formats. Its .parse() method takes a "handle" and format name and returns SeqRecords

from Bio import Entrez
from Bio import SeqIO
from utils.str_to_list import space_sep_to_list

# Finds the fasta shortest sequence given a list of Genbank access IDs
def find_shortest_fasta(db="nucleotide", id=[], rettype="fasta", showSeq=False):
  Entrez.email = "your_name@your_mail_server.com"
  handle = Entrez.efetch(db=db, id=id, rettype=rettype)
  records = list(SeqIO.parse(
    handle, "fasta"))  #we get the list of SeqIO objects in FASTA format

  #Note to self: "*" before an iterable unpacks all the elem of the seq into individual args and prints   them on separate lines
  # print("all records: ", *records, sep="\n \n")  
  shortest_len = float('inf')
  shortest = ""
  shortest_record = ""
  for record in records:
    seq_length = len(record.seq)
    # print("each length:", seq_length)
    if seq_length<shortest_len:
      shortest_len = seq_length
      shortest = record.seq
      shortest_record = record
      # print("Record ID: ", record.id)
      # print("Sequence length: ", seq_length, end="\n \n")
      # print("Sequence: ", record.seq)
    if showSeq:
      print("Sequence: ", record.seq)
  # print(records[0].id)  #first record id
  # print(len(records[-1].seq))  #length of the last record

  print("Shortest record: ", shortest_record)
  print("Shortest length", shortest_len)
  print("Shortest sequence", shortest)
  print("Shortest fasta", f">{shortest_record.description} {shortest}")

input_list = space_sep_to_list("JX069768 JX469983 JX469984")
find_shortest_fasta(id=input_list, showSeq=False)

#TODO: Even though this function produces the correct value, the Rosalind site seems to want it in a more specific format

# Here's the answer it gave:
# >JX317645.1 Culex quinquefasciatus neuropeptide F mRNA, complete cds
# ATGGCATCCACAAGCAGCAGCAGCAGAATCAACAACAACCGCCATGCCGTCAGGTCATCAGCCTCTTCAG
# CGTTCACCCAGCGACTGCTAATCGGCCTGCTGGTCTGCACCCTGGTGCTGGATCTTAGCTGCCTGACCGA
# GGCCCGGCCCCAGGACGATCCCACCTCCGTCGCCGAAGCCATCCGACTGCTGCAGGAGCTGGAAACCAAG
# CACGCCCAACATGCCCGACCAAGATTCGGAAAACGTGGCTATCTCCAGCCGGCAAGTTACGGCCAGGACG
# AACAGGAGCGAAACTATTACAGGATGATTGGCAGGATTCAGCGTTTTCAAGATGAACAGAACGCCGTACT
# CAACTAA

#Here's the answer this funciton gave:
# >JX317645.1 Culex quinquefasciatus neuropeptide F mRNA, complete cds ATGGCATCCACAAGCAGCAGCAGCAGAATCAACAACAACCGCCATGCCGTCAGGTCATCAGCCTCTTCAGCGTTCACCCAGCGACTGCTAATCGGCCTGCTGGTCTGCACCCTGGTGCTGGATCTTAGCTGCCTGACCGAGGCCCGGCCCCAGGACGATCCCACCTCCGTCGCCGAAGCCATCCGACTGCTGCAGGAGCTGGAAACCAAGCACGCCCAACATGCCCGACCAAGATTCGGAAAACGTGGCTATCTCCAGCCGGCAAGTTACGGCCAGGACGAACAGGAGCGAAACTATTACAGGATGATTGGCAGGATTCAGCGTTTTCAAGATGAACAGAACGCCGTACTCAACTAA

# The difference seems to be Rosalind wants the fasta string with a new line after the descriptor and a new line after 70 characters of the sequence.