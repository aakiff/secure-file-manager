# Secure File Manager - Design Document

## 1. Project Overview

Secure File Manager is a command-line application designed to securely encrypt and decrypt files using a user-provided password.

The main security goals of the application are:

- Confidentiality: unauthorized users should not be able to read encrypted files.
- Integrity: unauthorized modification of encrypted files should be detected.
- Secure password and key handling: passwords and encryption keys should not be stored in plaintext.

## 2. System Architecture

The application consists of the following main components:

- CLI: receives commands, file paths, and the user's password.
- Key Derivation Module: derives an encryption key from the user's password and a random salt.
- Encryption Module: encrypts and decrypts file contents using authenticated encryption.
- File Handling Module: reads input files and writes encrypted or decrypted output files.
- File Storage: stores plaintext files and encrypted files on the user's local file system.

The password and derived encryption key are only needed during the encryption or decryption operation and are not stored in plaintext on disk.

## 3. Architecture Diagram

```text
                    UNTRUSTED INPUT
                          |
                          | command, file path, password
                          v
                +-------------------+
                |        CLI        |
                +---------+---------+
                          |
                          | password
                          v
                +-------------------+
                |  Key Derivation   |
                |      Module       |
                +---------+---------+
                          |
                          | derived key
                          v
                +-------------------+
                |    Encryption /   |
                |    Decryption     |
                |      Module       |
                +---------+---------+
                          |
                          | file data
                          v
                +-------------------+
                |   File Handling   |
                |      Module       |
                +---------+---------+
                          |
                          v
              +-----------------------+
              | Local File System     |
              |                       |
              | plaintext / .enc files|
              +-----------------------+

        ----------- TRUST BOUNDARY -----------
        User input and local files are treated
        as potentially untrusted data.
```

## 4. Threat Model

The application treats user input, file paths, passwords, and encrypted files as potentially untrusted.

| Area | Threat | Mitigation |
|---|---|---|
| File Handling | An attacker modifies an encrypted file. | Use authenticated encryption so unauthorized modification can be detected. |
| File Handling | A malicious or invalid file is provided to the application. | Validate file paths, file format, and input before processing. |
| Authentication | An attacker attempts to guess the user's password. | Use a password-based key derivation function with a random salt to make password guessing more expensive. |
| Authentication | An incorrect password is used for decryption. | Authenticated decryption should fail without exposing decrypted file contents. |
| Password Handling | The password is exposed on the command line or stored on disk. | Request the password securely at runtime and never store it in plaintext. |
| Key Handling | The derived encryption key is exposed or stored permanently. | Keep the derived key only for the duration of the operation and never store it in plaintext on disk. |

## 5. Cryptographic Design

The application will use a password-based encryption scheme.

A random salt will be generated for each encryption operation. The user's password and the salt will be processed using Scrypt to derive a 256-bit encryption key.

AES-256-GCM will be used for authenticated encryption. A unique random nonce will be generated for each encryption operation.

The salt and nonce do not need to be secret and will be stored together with the encrypted file. The user's password and derived encryption key will not be stored in the encrypted file.

### Encryption Flow

1. The user provides a password.
2. A random salt is generated.
3. Scrypt derives a 256-bit key from the password and salt.
4. A unique random nonce is generated.
5. AES-256-GCM encrypts the file.
6. The salt, nonce, and encrypted data are written to the output file.

### Decryption Flow

1. The encrypted file is read.
2. The salt and nonce are extracted.
3. The user provides the password.
4. Scrypt derives the same encryption key.
5. AES-256-GCM authenticates and decrypts the file.
6. If authentication fails, no decrypted output is produced.

## 6. Language and Libraries

### Programming Language

Python 3 will be used to implement the application.

Python was chosen because it allows the project to focus on secure application design while providing well-tested cryptographic libraries.

### Libraries

- `cryptography` - provides the cryptographic primitives required for Scrypt key derivation and AES-GCM authenticated encryption.
- `getpass` - Python standard library module used to request passwords without displaying them in the terminal.
- `os` - Python standard library module that can be used for secure random data generation and file operations.
- `argparse` - Python standard library module used to implement the command-line interface.

The application will rely on established cryptographic libraries instead of implementing cryptographic algorithms manually.