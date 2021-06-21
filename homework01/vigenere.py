def encrypt_vigenere(plaintext: str, keyword: str) -> str:
    """
    Encrypts plaintext using a Vigenere cipher.

    >>> encrypt_vigenere("PYTHON", "A")
    'PYTHON'
    >>> encrypt_vigenere("python", "a")
    'python'
    >>> encrypt_vigenere("ATTACKATDAWN", "LEMON")
    'LXFOPVEFRNHR'
    """
    ciphertext = ""
    # PUT YOUR CODE HERE
    # plaintext = "ATTACKATDAWN"
    # keyword = "LEMON"
    codearray = []
    keyarray = []
    while len(plaintext) > len(keyword):
        keyword += keyword
        # print(keyword)
    for letter in plaintext:
        code = ord(letter)
        codearray.append(code)
        # print(codearray)
    for keyletter in keyword:
        keycode = ord(keyletter)
        keyarray.append(keycode)
        # print(keyarray)
    for i in range(0, len(codearray)):
        if ord('A') <= (codearray[i]) <= ord('Z'):
            diff = codearray[i] - ord('A')
            shift = keyarray[i] - ord('A')
            code = (diff + shift) % 26 + ord('A')
        elif ord('a') <= (codearray[i]) <= ord('z'):
            diff = codearray[i] - ord('a')
            shift = keyarray[i] - ord('a')
            code = (diff + shift) % 26 + ord('a')
        elif 32 <= codearray[i] <= 64:
            code = codearray[i]
        ciphertext += chr(code)

    return ciphertext


def decrypt_vigenere(ciphertext: str, keyword: str) -> str:
    """
    Decrypts a ciphertext using a Vigenere cipher.

    >>> decrypt_vigenere("PYTHON", "A")
    'PYTHON'
    >>> decrypt_vigenere("python", "a")
    'python'
    >>> decrypt_vigenere("LXFOPVEFRNHR", "LEMON")
    'ATTACKATDAWN'
    """
    plaintext = ""
    # PUT YOUR CODE HERE
    plainarray = []
    keyarray = []
    while len(ciphertext) > len(keyword):
        keyword += keyword
        # print(keyword)
    for letter in ciphertext:
        code = ord(letter)
        plainarray.append(code)
    # print(plainarray)
    for keyletter in keyword:
        keycode = ord(keyletter)
        keyarray.append(keycode)
        # print(keyarray)
    for i in range(0, len(plainarray)):
        if ord('A') <= (plainarray[i]) <= ord('Z'):
            diff = plainarray[i] - ord('A')
            shift = keyarray[i] - ord('A')
            code = (diff - shift) % 26 + ord('A')
        elif ord('a') <= (plainarray[i]) <= ord('z'):
            diff = plainarray[i] - ord('a')
            shift = keyarray[i] - ord('a')
            code = (diff - shift) % 26 + ord('a')
        elif 32 <= plainarray[i] <= 64:
            code = plainarray[i]

        plaintext += chr(code)
    return plaintext
