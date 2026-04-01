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


**EXAMPLE 1:**
Enter plaintext: crypto
Enter key: cat
P' = [104,119,126,117,121,116]
c   a   t
2   1   3   (order)
-------------------
104 119 126
117 121 116
CIPHER NUMBERS: [119,121,104,117,126,116] => HEX(X) => b1a7aaac9ba8
Ciphertext (HEX): b1a7aaac9ba8
[177, 167, 170, 172, 155, 168] => RECONSTRUCT Matrix => P[i]=(value−k+256)mod256
Decrypted: crypto

**EXAMPLE 2:**
Enter plaintext: dscds
Enter key: key
CIPHER NUMBERS: [100, 115, 99, 100, 115] => HEX(X) 
Ciphertext (HEX): adadbcbcac
Decrypted: dscds

####TEST SCRIPT
crypto(plaintext)->[104,119,126,117,121,116]->b1a7aaac9ba8(ciphertext)->crypto(plaintext)
round trip successful
