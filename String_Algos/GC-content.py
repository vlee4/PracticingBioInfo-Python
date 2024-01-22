# Given up to 10 DNA strings in FASTA format (of <= 1kbp each)
# Return the ID of the string with the HIGHEST GC-content and the GC-content of the string

fasta_strs = open('./String_Algos/fasta_strings.txt', 'r')
fasta_strings = fasta_strs.read()

highest_GC = {
  "str_name": "",
  "GC_content": 0,
}


# Function to find string
def formatStr(gc_strings):
  # remove new lines
  gc_str = gc_strings.splitlines()
  # combine into string
  joined = "".join(gc_str)
  #splits the string at '>' and filters out any empty strings
  split_list = filter(None, joined.split(">"))

  # Since filter() returns an iterator, you need to call list() to consume the iterator and create the final list.
  return list(split_list)


# Function to calculate GC-content & compare with highest value yet
def calculate_GC(str_arr):
  for fasta in str_arr:
    DNA = fasta[13:]  # Just look at DNA part of FASTA string
    # print("DNA", DNA)
    count = 0

    for lt in DNA:
      if lt == "G" or lt == "C":
        count += 1

    percentage_GC = (float(count) / float(len(DNA))) * 100

    if percentage_GC > highest_GC['GC_content']:
      highest_GC['GC_content'] = percentage_GC
      highest_GC['str_name'] = fasta[:13]


# Print highest value
def getHighestGC():
  print(highest_GC['str_name'])
  print(highest_GC['GC_content'])


formatted_strings = formatStr(fasta_strings)
calculate_GC(formatted_strings)
getHighestGC()

fasta_strs.close()
