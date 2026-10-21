import argparse
import getpass
import os
from pathlib import Path

from cryptography.hazmat.primitives.ciphers.aead import AESGCM
from cryptography.hazmat.primitives.kdf.scrypt import Scrypt
from cryptography.exceptions import InvalidTag


def derive_key(password, salt):
    kdf = Scrypt(
        salt=salt,
        length=32,
        n=2**14,
        r=8,
        p=1
    )

    key = kdf.derive(password.encode("utf-8"))

    return key


def encrypt_file(file_path, password):
    salt = os.urandom(16)
    nonce = os.urandom(12)

    key = derive_key(password, salt)

    aesgcm = AESGCM(key)

    with open(file_path, "rb") as file:
        plaintext = file.read()

    ciphertext = aesgcm.encrypt(nonce, plaintext, None)

    output_path = Path(str(file_path) + ".enc")

    with open(output_path, "xb") as file:
        file.write(b"SFM1" + salt + nonce + ciphertext)

    print(f"File encrypted successfully: {output_path}")


def decrypt_file(file_path, password):
    with open(file_path, "rb") as file:
        encrypted_data = file.read()

    if len(encrypted_data) < 48:
        raise ValueError("Error: Invalid encrypted file.")

    if encrypted_data[:4] != b"SFM1":
        raise ValueError("Error: Invalid file format.")

    salt = encrypted_data[4:20]
    nonce = encrypted_data[20:32]
    ciphertext = encrypted_data[32:]

    key = derive_key(password, salt)
    aesgcm = AESGCM(key)

    try:
        plaintext = aesgcm.decrypt(nonce, ciphertext, None)
    except InvalidTag:
        raise ValueError(
            "Error: Incorrect password or corrupted encrypted file."
        ) from None

    if not str(file_path).endswith(".enc"):
        raise ValueError("Error: Expected a .enc file.")

    output_path = Path(str(file_path)[:-4])

    with open(output_path, "xb") as file:
        file.write(plaintext)

    print(f"File decrypted successfully: {output_path}")


def validate_file(file_path):
    path = Path(file_path)

    if not path.exists():
        raise ValueError("Error: File does not exist.")

    if not path.is_file():
        raise ValueError("Error: The specified path is not a file.")

    return path


def main():
    parser = argparse.ArgumentParser(
        description="Secure File Manager - encrypt and decrypt files."
    )

    parser.add_argument(
        "command",
        choices=["encrypt", "decrypt"],
        help="Choose whether to encrypt or decrypt a file."
    )

    parser.add_argument(
        "file",
        help="Path to the file."
    )

    args = parser.parse_args()

    try:
        file_path = validate_file(args.file)

        print(f"Command: {args.command}")
        print(f"File validated: {file_path}")

        password = getpass.getpass("Enter password: ")

        if not password:
            raise ValueError("Error: Password cannot be empty.")

        if args.command == "encrypt":
            encrypt_file(file_path, password)
        else:
            decrypt_file(file_path, password)

    except ValueError as error:
        print(error)


if __name__ == "__main__":
    main()