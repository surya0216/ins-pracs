import string

def process_text(text):
  return list(text.upper().replace(" ",""))

def generate_pool():
  return list(string.ascii_uppercase)

def genearte_shifted_pool(shift_value=3):
  pool = generate_pool()
  lst = []
  for i in range(len(pool)):
    lst.append(pool[(i+shift_value)%(26)])
  return lst

def ceaser_encrypt(plai_text, shift_value=3):
  plai_text = process_text(plai_text)
  cipher = ''
  pool = generate_pool()
  lst = genearte_shifted_pool(shift_value)
  for i in range(len(plai_text)):
    for j in range(len(pool)):
      if plai_text[i] == pool[j]:
        cipher += lst[j]
  return cipher

def ceaser_decrypt(cipher_text, shift_value=3):
  cipher_text = process_text(cipher_text)
  original = ''
  pool = generate_pool()
  lst = genearte_shifted_pool(shift_value)
  for i in range(len(cipher_text)):
    for j in range(len(pool)):
      if cipher_text[i] == lst[j]:
        original += pool[j]
  return original 

ende = input("Do you want to encrypt or decrypt? (d/e): ")
if ende == 'd':
  cipher_text = input("Enter the text you want to decrpyt: ")
  shift_vaule = input("Enter the shift value that used for encryption (default = 3): ")
  if shift_vaule == '':
    shift_vaule = 3
  else:
    shift_vaule = int(shift_vaule)
  plain_text = ceaser_decrypt(cipher_text, shift_vaule)
  print(f"Cipher Text: {cipher_text} \nDecrypted Text: {plain_text} \nShift Value = {shift_vaule}")
else:
  plain_text = input("Enter the text you want to encrpyt: ")
  shift_vaule = input("Enter the shift value (default = 3): ")
  if shift_vaule == '':
    shift_vaule = 3
  else:
    shift_vaule = int(shift_vaule)
  cipher_text = ceaser_encrypt(plain_text, shift_vaule)
  print(f"Plain Text: {plain_text} \nCipher Text: {cipher_text} \nShift Value = {shift_vaule}")


# cipher_text = ceaser_encrypt("surya")
# original_text = ceaser_decrypt(cipher_text)

# print(cipher_text, original_text)