"""
- Within the Biopython module, Entrez is a data retrieval system that allows you (via the .efetch method) to search any of NCBI's databases.
- .efetch takes a variety of arguments including "db" and "term" argument, referring to the DB you want to search (nucleotide = GenBank; pubmed = PubMed), and the query you want to search for, respectively.
- .efetch can also take an "id" argument which is a list of IDs to search for, and a "rettype" argument that takes the data format to be returned.

- The SeqIO module provides an interface to input & output methods for different file formats. Its .parse() method takes a "handle" and format name and returns SeqRecords
"""
from Bio import Entrez
from Bio import SeqIO
from utils.str_to_list import space_sep_to_list
from utils.format_str import char_limit_per_line

# Finds the fasta shortest sequence given a list of Genbank access IDs
def find_shortest_fasta(db="nucleotide", id=[], rettype="fasta", showSeq=False):
  Entrez.email = "your_name@your_mail_server.com"
  handle = Entrez.efetch(db=db, id=id, rettype=rettype)
  records = list(SeqIO.parse(
    handle, "fasta"))  #we get the list of SeqIO objects in FASTA format

  #Note to self: "*" before an iterable unpacks all the elem of the seq into individual args and prints them on separate lines
 
  shortest_len = float('inf')
  shortest_record = ""
  
  for record in records:
    seq_length = len(record.seq)
    
    if seq_length<shortest_len:
      shortest_len = seq_length
      shortest_record = record
     
    if showSeq:
      print("Sequence: ", record.seq)

  print("Shortest fasta", f"\n>{shortest_record.description}\n{char_limit_per_line(shortest_record.seq)}")

input_list = space_sep_to_list("JX069768 JX469983 JX469984")
find_shortest_fasta(id=input_list, showSeq=False)
