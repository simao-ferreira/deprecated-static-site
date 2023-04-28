Title: Encrypting files with openssl
Date: 2021-12-05
Category: Learning
Tags: openssl, encryption
Author: Simao Ferreira
Summary: File encryption with openssl

## File encryption with openssl

[OpenSSL](https://www.openssl.org/) is an open software that provides cryptography tools and it's used for secure communication.

I wanted to play around with encryption methods and tools and today I chose SSL, commonly used for secure data transfer in the internet, it's also possible to use SSL to encrypt files with a password.

First let's check OpenSSL version:

```shell
$ openssl version
```

The outcome should be something similar to the following

```shell
OpenSSL 3.0.0 7 sep 2021 (Library: OpenSSL 3.0.0 7 sep 2021)
```

To get a better look into what openssl tool provides

```shell
$ openssl help
```

we are interested in the cipher commands, there we can find what encryption methods are available and select the one that interest us most to encrypt our file.

### Encrypt archive.txt with password

A password, and confirmation, will be requested after <ENTER> is pressed.

```shell
$ openssl enc -aes-256-cbc -in archive.txt -out archive.txt.enc -pbkdf2
```

Explanation:

1. enc: encrypt
2. -aes-256-cbc: encryption cipher
3. -in: input to encrypt
4. -out: encrypted output
5. -pbkdf2: password based key derivation function, recommended practice for hashing the password

Filename could be the same, but in that case the output must be another directory.

By default, pbkdf2 iterations are 10k, it's possible to change this by using the flag `-iter`, caution though it's also necessary to use the same flag in the decryption process.

Additionally, it's possible to pass the password as argument in plain text using the flag `-pass`, with the following format `-pass 'pass:some-password-here`.

### Decrypt archive.txt.enc

Password will be requested after <ENTER> is pressed

```shell
$ openssl enc -d -aes-256-cbc -n archive.txt.enc -out archive.txt -pbkdf2
```

Explanation:

1. -d: decryption

For previous versions it might be necessary to provide the used digest, help contains a section `dgst` containing some examples.

```shell
$ openssl dgst --list
```

### Comparing files

To validate the decryption did not change the file we can run:

```shell
$ diff original-file.txt decrypted-file.txt
```

If all went according to plan, nothing should have changed so the command output should be nothing.

### TL;DR

```shell
$ openssl enc -pbkdf2 -aes-256-cbc -in archive.txt -out archive.txt.enc -pass 'pass:somepassword'
```

```shell
$ openssl enc -d -pbkdf2 -aes-256-cbc -in archive.txt.enc -out archive-decrypted.txt -pass 'pass:somepassword'
```
