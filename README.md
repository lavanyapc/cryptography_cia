# Myszkowski cipher with Hash function for key and plain text

**DESCRIPTION:**
This algorithm implements a modified Myszkowski cipher using key-based hashing and ASCII transformation. The key is processed to generate column ranks, which determine the order of columnar transposition. The plaintext is converted into ASCII values and shifted using a key-derived value before being placed into a matrix. Encryption is performed using rank-based column traversal, and the output is encoded in HEX format. Decryption reverses the process using inverse transformation, matrix reconstruction, and HEX decoding to recover the original plaintext.

**Algorithm: Modified Myszkowski Cipher with Key Hashing and ASCII Transformation**
Input:
1. Plaintext string P
2. Key string K
Output:
1. Ciphertext (HEX encoded)
2. Decrypted plaintext

**Encryption Process**
1. Initialize empty list ciphertext
2. Find maximum rank value in ranks
3. For each rank r from 1 to max rank:
  3.1 Find all column indices where rank = r
  3.2 Sort column indices in ascending order
  3.3 For each column:
   3.3.1 Traverse matrix row-wise
   3.3.2 Append non-empty elements to ciphertext
4. Convert each number in ciphertext to HEX format
5. Concatenate HEX values to form final ciphertext

**Decryption Process**
1. Convert HEX ciphertext into integer list
2. Create empty matrix of size rows × cols
3. Initialize index idx = 0
4. For each rank r from 1 to max rank:
  4.1 Find all column indices with rank = r
  4.2 Sort column indices
  4.3 Fill matrix column-wise (row by row) using ciphertext values
5. Flatten matrix row-wise into list flat
6. Apply inverse transformation:
   P[i] = (flat[i] - k + 256) mod 256
7. Convert ASCII values back to characters


