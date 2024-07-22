import string

# Removing white space and replacing j with i and adding x at the end if the length of the word is odd
def process_text(pt:str):
  pt = pt.replace(" ","").lower().replace('j','i')
  spt = list(pt)
  if len(spt) & 1 == 1:
     spt.append('x')

  return spt

# Removing white space's from key and replacing j with i
def process_key(key:str):
  key = key.replace(" ","").lower().replace('j','i')
  return list(key)

# Generating a pool of key and alphabet where every character is unique
def generate_pool_with_key(key:str):
  pool = key + list(string.ascii_lowercase)
  new_pool = []
  for i in range(len(pool)-1):
    if pool[i] == 'j':
      pool.pop(i)
  for i in pool:
    if i not in new_pool:
      new_pool.append(i)
  return new_pool

# Generating matrix
def generate_matrix(pool:list, row, col):
  matrix = []
  for i in range(row):
    start_index = i * col
    end_index = col + start_index
    row = pool[start_index:end_index]
    matrix.append(row)
  return matrix

# Finding the index of a given character in the matrix
def locate_index(chr, matrix):
  for i in range(len(matrix)):
    for j in range(len(matrix[0])) :
      if matrix[i][j] == chr:
        return i, j

# Encrypting list of 2 characters according to playfair cipher rule
def encrypt_2_char(lst, matrix):
  r1, c1 = locate_index(lst[0], matrix)
  r2, c2 = locate_index(lst[1], matrix)
  
  if r1 == r2 :
    return matrix[r1][(c1+1)%5] + matrix[r1][(c2+1)%5]
  elif c1 == c2 :
    return matrix[(r1+1)%5][c1] + matrix[(r2+1)%5][c1]
  else:
    return matrix[r1][c2] + matrix[r2][c1]

# Decrypting list of 2 characters according to playfair cipher rule but in reverse
def decrypt_2_char(lst, matrix):
    r1, c1 = locate_index(lst[0],matrix)
    r2, c2 = locate_index(lst[1],matrix)
    
    if r1 == r2:
        return matrix[r1][(c1 - 1)] + matrix[r2][(c2 - 1)]
    elif c1 == c2:
        return matrix[(r1 - 1)][c1] + matrix[(r2 - 1)][c2]
    else:
        return matrix[r1][c2] + matrix[r2][c1]
    
# Generating sublist 2 character of the plain text using the generate_matrix function 
def generate_plain_text_sublist(plaint_text):
  lists = generate_matrix(plaint_text, int(len(plaint_text)/2), 2)
  for lst in lists:
    if lst[0] == lst[1]:
      lst[1] = 'x'
  return lists
  
# Using all the function and putting it into one final function and creating the cipher text
def playfair_encrypt(plain_text, key):
  cipher_text = ''
  plain_text = process_text(plain_text)
  key = process_key(key)
  key_pool = generate_pool_with_key(key)

  matrix = generate_matrix(key_pool, 5, 5)

  plain_text_lists = generate_plain_text_sublist(plain_text)

  for i in plain_text_lists:
    cipher_text += encrypt_2_char(i, matrix)

  return cipher_text

def playfair_decrypt(cipher_text, key):
  original_text = ''
  cipher_texts = process_text(cipher_text)
  key = process_key(key)
  key_pool = generate_pool_with_key(key)

  matrix = generate_matrix(key_pool, 5, 5)

  cipher_text_lists = generate_plain_text_sublist(cipher_texts)

  for i in cipher_text_lists:
    original_text += decrypt_2_char(i, matrix)

  print(original_text)
  cipher_list = list(original_text)
  if cipher_list[-1] == 'x':
    cipher_list.pop()
  
  for i in range(len(cipher_list)):
    if i <= len(cipher_list)-1:
      if cipher_list[i] == 'x':
        cipher_list.pop(i)
        cipher_list.insert(i, cipher_list[i-1])
  
  original_text = ''.join(cipher_list)
  return original_text

ende = input("Do you want to encrypt or decrypt your text? (e/d): ")
if ende == 'd':
  cipher = input("Enter the text you want to decrypt: ") 
  key = input("Enter the same key that you used for encryption: ") 
  original = playfair_decrypt(cipher, key).upper()
  print(f"Cipher text: {cipher} \nDecrpyted text: {original.upper()} \nKey: {key}")
else:
  plain_text = input("Enter the text you want to encrypt: ") 
  key = input("Enter key: ") 
  cipher = playfair_encrypt(plain_text,key).upper()
  print(f"Plaint text: {plain_text} \nCipher text: {cipher} \nKey: {key}")






