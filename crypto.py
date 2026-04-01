import math
def generate_key_ranks(key):
    h = [(ord(key[i]) * (i + 1)) % 26 for i in range(len(key))]
    sorted_unique = sorted(list(set(h)))
    rank_map = {val: idx + 1 for idx, val in enumerate(sorted_unique)}
    ranks = [rank_map[val] for val in h]
    return ranks

def transform_text(text, key):
    k = sum(ord(c) for c in key) % 256
    return [(ord(c) + k) % 256 for c in text], k

def inverse_transform(arr, k):
    return ''.join(chr((c - k + 256) % 256) for c in arr)

def build_matrix(data, cols):
    rows = math.ceil(len(data) / cols)
    matrix = [['' for _ in range(cols)] for _ in range(rows)]
    idx = 0
    for i in range(rows):
        for j in range(cols):
            if idx < len(data):
                matrix[i][j] = data[idx]
                idx += 1
    return matrix

#ENCRYPTION
def encrypt(plaintext, key):
    ranks = generate_key_ranks(key)
    transformed, k = transform_text(plaintext, key)
    cols = len(key)
    matrix = build_matrix(transformed, cols)
    max_rank = max(ranks)
    ciphertext = []

    for r in range(1, max_rank + 1):
        cols_with_rank = sorted([i for i, val in enumerate(ranks) if val == r])
        for col in cols_with_rank:
            for row in range(len(matrix)):
                if matrix[row][col] != '':
                    ciphertext.append(matrix[row][col])

    cipher_hex = ''.join(format(c, '02x') for c in ciphertext)
    return cipher_hex, k, ranks, len(matrix), len(key)

#DECRYPTION
def decrypt(ciphertext_hex, key, k, ranks, rows, cols):
    ciphertext = [
        int(ciphertext_hex[i:i+2], 16)
        for i in range(0, len(ciphertext_hex), 2)
    ]

    matrix = [['' for _ in range(cols)] for _ in range(rows)]
    idx = 0
    max_rank = max(ranks)

    for r in range(1, max_rank + 1):
        cols_with_rank = sorted([i for i, val in enumerate(ranks) if val == r])
        for col in cols_with_rank:
            for row in range(rows):
                if idx < len(ciphertext):
                    matrix[row][col] = ciphertext[idx]
                    idx += 1

    flat = []
    for row in range(rows):
        for col in range(cols):
            if matrix[row][col] != '':
                flat.append(matrix[row][col])

    return inverse_transform(flat, k)

if __name__ == "__main__":
    plaintext = input("Enter plaintext: ")
    key = input("Enter key: ")

    cipher, k, ranks, rows, cols = encrypt(plaintext, key)

    print("\nCiphertext (HEX):", cipher)

    decrypted = decrypt(cipher, key, k, ranks, rows, cols)
    print("Decrypted:", decrypted)