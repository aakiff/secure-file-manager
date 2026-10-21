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

### Requirements

- Python 3.10 or newer
- pip

### Setup

1. Clone the repository:

```bash
git clone https://github.com/aakiff/secure-file-manager.git
cd secure-file-manager
```

2. Create a virtual environment:

```bash
python -m venv .venv
```

3. Activate the virtual environment.

Windows PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

Linux/macOS:

```bash
source .venv/bin/activate
```

4. Install dependencies:

```bash
python -m pip install -r requirements.txt
```

## Running the Application

Encrypt a file:

```bash
python src/main.py encrypt example.txt
```

Decrypt an encrypted file:

```bash
python src/main.py decrypt example.txt.enc
```

The application requests a password without displaying it in the terminal.

Encrypted files are saved with the `.enc` extension. The original file is not deleted.

Decryption requires the correct password. Modified or corrupted encrypted data will fail authentication.

For safety, the application does not overwrite existing output files.

## Security Features

- AES-256-GCM authenticated encryption
- Scrypt password-based key derivation
- Random salt and nonce generation
- Hidden password input
- Basic file path validation
- Detection of incorrect passwords and modified encrypted data

## Current Limitations

- Files are processed entirely in memory.
- The application is intended as an educational prototype.
- Original plaintext files are not automatically deleted.
- Additional security testing and hardening are planned.