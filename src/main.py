import argparse
from pathlib import Path


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

    except ValueError as error:
        print(error)


if __name__ == "__main__":
    main()