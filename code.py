import math

def get_index(x, column, i, word):
  pos = (x*column)+i
  if(pos < len(word)):
    return word[pos]
  else:
    return ''

def construct_square(word, margin):
  column = int(math.ceil(margin))
  row = int(math.floor(margin))
  result = ''
  for i in range(column):
    mat = map(lambda x: get_index(x, column, i, word), range(row+1))
    result += ''.join(mat)+ " "
  return result.strip()
    

if __name__ == "__main__":
  word = raw_input()
  margin = math.sqrt(len(word))
  print construct_square(word, margin)
