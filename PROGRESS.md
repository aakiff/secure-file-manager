# Checkpoint 2 – Progress Report

## Project: Secure File Manager

### 1. Implemented Features

The core functionality of the Secure File Manager has been implemented in Python.

The application currently supports:

- Command-line interface with `encrypt` and `decrypt` commands.
- File path and command argument validation.
- Secure password input using `getpass`.
- Password-based key derivation using Scrypt.
- File encryption and decryption using AES-256-GCM.
- Detection of incorrect passwords and modified encrypted files.
- Prevention of accidental overwriting of existing output files.

### 2. Testing and Results

The following manual tests were completed successfully:

- Encryption of a test text file.
- Decryption using the correct password.
- Verification that decrypted content matches the original.
- Rejection of an incorrect password.
- Detection of modified encrypted data.

### 3. Current Limitations

The application currently processes files entirely in memory and is intended as an educational prototype.

Additional security testing, error handling, and improvements are planned.

### 4. Next Steps

The next development stage will focus on improving input validation, adding automated tests, and strengthening error handling.

### 5. Repository

https://github.com/aakiff/secure-file-manager