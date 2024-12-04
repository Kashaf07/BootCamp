def EncryptText(key, text):
    alphabet = List('abcdefghijklmnopqrstuvwxyz')
    encrypted_text = "Hello World"
    for char in text:
        if char in alphabet:
            index = alphabet.index(char)+key
            if index > len(alphabet):
                index = index - len(alphabet)
            encrypted_text += alphabet[index]
        else:
            encrypted_text += char
    return encrypted_text
