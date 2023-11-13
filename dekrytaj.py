def decrypt(encrypted_text, key):
    decrypted_text = ""
    key_length = len(key)
    for i, char in enumerate(encrypted_text):
        if char.isalpha():
            start = ord('a') if char.islower() else ord('A')
            key_char = key[i % key_length]
            key_shift = ord(key_char.lower()) - ord('a')
            decrypted_text += chr((ord(char) - start - key_shift) % 26 + start)
        else:
            decrypted_text += char
    return decrypted_text 