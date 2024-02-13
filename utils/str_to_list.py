# Given a string of space separated values, return a list of strings of those values
__all__ = ['space_sep_to_list']

def space_sep_to_list(space_sep_str):
  return space_sep_str.split(" ")

# test = "FJ817486 JX069768 JX469983"
# print(space_sep_to_list(test))
