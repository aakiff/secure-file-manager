# Secure File Manager

## Project Scope

Secure File Manager is a command-line application for securely encrypting and decrypting files using a user-provided password.

The application will use password-based key derivation and authenticated encryption to protect the confidentiality and integrity of files.

The project focuses on secure file handling, password and key management, and protection against unauthorized access or modification of encrypted files.

## Planned Features

- Encrypt files using a password.
- Decrypt previously encrypted files using the correct password.
- Derive an encryption key from the user's password.
- Detect unauthorized modification of encrypted files.
- Handle files and cryptographic keys securely.

## Planned Commands

```bash
python src/main.py encrypt <file>
python src/main.py decrypt <file>
```

## Installation

1. Install Python 3.
2. Install the required dependencies:

```bash
pip install -r requirements.txt
```

## Running the Application

The application will be run from the command line.

To encrypt a file:

```bash
python src/main.py encrypt <file>
```

To decrypt a file:

```bash
python src/main.py decrypt <file>
```