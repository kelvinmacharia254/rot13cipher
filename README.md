**ROT-13 Cipher**

ROT13 is a simple letter substitution cipher that replaces a letter with the letter 13 letters after it in the alphabet. ROT13 is an example of the Caesar cipher.

I have created a function that takes a string and returns the string ciphered with Rot13. If there are numbers or special characters included in the string, they should be returned as they are. 

Only letters from the latin/english alphabet should be shifted, like in the original Rot13 "implementation".

Because there are 26 letters (2×13) in the basic Latin alphabet, ROT13 is its own inverse; that is, to undo ROT13, the same algorithm is applied, so the same action can be used for encoding and decoding.

Example:

rot13("Gb trg gb gur bgure fvqr!") -> To get to the other side!
