# Myszkowski cipher with Hash function for key and plain text  
## THEORY
### Myszkowski Cipher
Ciphertext generation: C=ColumnWiseRead(Pmatrix​,Rkey​)
Plaintext generation: P=RowWiseRead(Reconstructed Matrix)

### Hash Function
H(i)=(ASCII(K[i])×(i+1))mod26
* Each key character is converted using its ASCII value
* Position-based weighting is applied using index (i+1)
* Modulo 26 ensures values stay within alphabet range
* Final ranks are assigned based on sorted hash values
rank order=sorted(H(i))

#### Instructions to run the code
python3 crypto.py

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
3. For each rank r from 1 to max rank
   * Find all column indices where rank = r
   * Sort column indices in ascending order
   * For each column:
     * Traverse matrix row-wise
     * Append non-empty elements to ciphertext
4. Convert each number in ciphertext to HEX format
5. Concatenate HEX values to form final ciphertext

**Decryption Process**
1. Convert HEX ciphertext into integer list
2. Create empty matrix of size rows × cols
3. Initialize index idx = 0
4. For each rank r from 1 to max rank
   * Find all column indices with rank = r
   * Sort column indices
   * Fill matrix column-wise (row by row) using ciphertext values
5. Flatten matrix row-wise into list flat
6. Apply inverse transformation:
   P[i] = (flat[i] - k + 256) mod 256
7. Convert ASCII values back to characters

## EXAMPLE 1
1. Plaintext: crypto
2. CIPHER NUMBERS: 119, 121, 104, 117, 126, 116
3. HEX(X) → b1a7aaac9ba8
Ciphertext (HEX): b1a7aaac9ba8
4. Hex to Decimal:
177, 167, 170, 172, 155, 168
5. Matrix Reconstruction →
6. Inverse Operation: P[i] = (value − k + 256) mod 256
7. Decrypted Output: crypto

**EXAMPLE 2:**
1. Enter plaintext: dscds
2. Enter key: key
3. CIPHER NUMBERS: 100, 115, 99, 100, 115 => HEX(X) 
4. Ciphertext (HEX): adadbcbcac
5. Decrypted: dscds

###TEST SCRIPT
*crypto(plaintext)->104,119,126,117,121,116->b1a7aaac9ba8(ciphertext)->crypto(plaintext)
*round trip successful
