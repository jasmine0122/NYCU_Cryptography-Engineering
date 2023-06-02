# NYCU_CryptographyEngineering
2022 NYCU 110-2 密碼工程 Cryptography Engineering

⭐⭐⭐如果對你有幫助的話，請幫我點下Star⭐⭐⭐

## Midterm
There are 8 questions, a total of 130 points!

## 110-2 Final project
Proposal: https://www.youtube.com/watch?v=VcP_-W6acJI

Final demo: https://www.youtube.com/watch?v=5gzGbDEWvbQ

All: https://github.com/ianchen0119/Cryptography-Engineering-2022-spring/issues/33


## Critique 1
Paper: Juels and R. Rivest. "Honeywords: Making password-cracking detectable." In ACM SIGSAC conference on Computer & communications security, 2013

## Critique 2
Reading for Critique 2: Whitten, Alma, and J. Doug Tygar. “Why Johnny Can’t Encrypt: A Usability Evaluation of PGP 5.0.” USENIX Security Symposium. Vol. 348. 1999.

## Quiz 1
Output contents: the numbers of letters’ appearance in the ciphertext

## Quiz 2
1. Please determine the dimension of the rectangle for this encryption cipher.
2. Please Solve this following transposition cipher which involves a completely filled rectangles from the
HINT.
3. Please count Index of Coincidence (IC) for each messages.
The IC of English is around 0.
4. Given the following ciphertext, please determine if this encrypted message was enciphered using a
monoalphabetic or polyalphabetic cipher based on the message’s index of coincidence.

## Quiz 3
1. Please write a python program to determine keyword length of the
encrypted message using I.C.
2. Then write a second python program to solve the encryption
keyword letters for the message.
3. Finally, break these ciphertext and recover to the plaintext.

## Quiz 4
In this assignment, we will learn using Markov chain methods to attack classical columnar transposition ciphers automatically.
The steps to solve it are as follows:
1. Using the number of vowels to detect ciphertext rectangles (In English approximately 40% of plaintext consists of vowels).
2. Using plaintext bigrams and trigrams to calculate conditional probabilities for Markov decision processing (MDP).
3. Using MDP to recover columnar transposition ciphers.

## Quiz 5
In this quiz, you will need to implement a program that takes a 16-byte number as input and find a different number with the same 16 MSB of the MD5 value.
(hint: hashlib is your best friend)
- Bonus: 為何 primitive polynomial 都是奇數項？

## Quiz 6
You will need to implement a python program that reads the ciphertext from a file named "ciphertext.txt" and save the plaintext into a file named "plaintext.txt"
A template will be given and you can follow the template or design your own MCMC
- For more detail, please reference the given template
- Reference text is war_and_peace.txt

## Quiz 7
1. Please write a program based on Berlekamp–Massey algorithm to find the shortest linear feedback shift register (LFSR) for the given sequence down below.
2. Find the sequence generation rule of 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610...
3. Extra credit: Use Berlekamp–Massey algorithm to find out the sequence rule of  0, 1, 1, 2, 3, 5, 8, 13, 21, 34...






