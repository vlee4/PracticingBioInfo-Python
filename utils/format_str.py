__all__ = ['char_limit_per_line']

def char_limit_per_line(string, limit=70):
  str_len = len(string)
  i = 0
  formatted_str = ""

  while i < str_len:
    formatted_str += f"{string[i:i+limit]}\n"
    i += limit

  return formatted_str

# test_str = "ATGGCATCCACAAGCAGCAGCAGCAGAATCAACAACAACCGCCATGCCGTCAGGTCATCAGCCTCTTCAGCGTTCACCCAGCGACTGCTAATCGGCCTGCTGGTCTGCACCCTGGTGCTGGATCTTAGCTGCCTGACCGAGGCCCGGCCCCAGGACGATCCCACCTCCGTCGCCGAAGCCATCCGACTGCTGCAGGAGCTGGAAACCAAGCACGCCCAACATGCCCGACCAAGATTCGGAAAACGTGGCTATCTCCAGCCGGCAAGTTACGGCCAGGACGAACAGGAGCGAAACTATTACAGGATGATTGGCAGGATTCAGCGTTTTCAAGATGAACAGAACGCCGTACTCAACTAA"
# print(char_limit_per_line(test_str))