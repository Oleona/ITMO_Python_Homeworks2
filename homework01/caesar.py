import typing as tp


def encrypt_caesar(plaintext: str, shift: int = 3) -> str:
    """
    Encrypts plaintext using a Caesar cipher.

    >>> encrypt_caesar("PYTHON")
    'SBWKRQ'
    >>> encrypt_caesar("python")
    'sbwkrq'
    >>> encrypt_caesar("Python3.6")
    'Sbwkrq3.6'
    >>> encrypt_caesar("")
    ''
    """
    ciphertext = ""
    # PUT YOUR CODE HERE
    for letter in plaintext:
        code = ord(letter)
        if ord('A') <= (code) <= ord('Z'):
            diff = code - ord('A')
            code = (diff + shift) % 26 + ord('A')
        elif ord('a') <= (code) <= ord('z'):
            diff = code - ord('a')
            code = (diff + shift) % 26 + ord('a')
        ciphertext += chr(code)
    return ciphertext


def decrypt_caesar(ciphertext: str, shift: int = 3) -> str:
    """
    Decrypts a ciphertext using a Caesar cipher.

    >>> decrypt_caesar("SBWKRQ")
    'PYTHON'
    >>> decrypt_caesar("sbwkrq")
    'python'
    >>> decrypt_caesar("Sbwkrq3.6")
    'Python3.6'
    >>> decrypt_caesar("")
    ''
    """
    plaintext = ""
    # PUT YOUR CODE HERE
    for letter in ciphertext:
        code = ord(letter)
        if ord('A') <= (code) <= ord('Z'):
            diff = code - ord('A')
            code = (diff - shift) % 26 + ord('A')
        elif ord('a') <= (code) <= ord('z'):
            diff = code - ord('a')
            code = (diff - shift) % 26 + ord('a')
        plaintext += chr(code)
    return plaintext


def caesar_breaker_brute_force(ciphertext: str, dictionary: tp.Set[str]) -> int:
    """
    Brute force breaking a Caesar cipher.
    """
    best_shift = 0
    # PUT YOUR CODE HERE
    return best_shift
