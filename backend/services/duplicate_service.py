from pathlib import Path
import hashlib


def calculate_hash(file_path: Path) -> str:
    """
    Calcula o hash SHA-256 de um arquivo.
    """

    sha256 = hashlib.sha256()

    with open(file_path, "rb") as file:
        while chunk := file.read(8192):
            sha256.update(chunk)

    return sha256.hexdigest()


def find_duplicates(directory: Path) -> list:
    """
    Procura arquivos duplicados dentro de um diretório.
    """

    hashes = {}

    for file in directory.rglob("*"):

        if not file.is_file():
            continue

        try:
            file_hash = calculate_hash(file)

            hashes.setdefault(file_hash, []).append(file)

        except Exception:
            continue

    duplicates = []

    for file_hash, files in hashes.items():

        if len(files) > 1:

            duplicates.append(
                {
                    "hash": file_hash,
                    "files": [
                        {
                            "name": file.name,
                            "path": str(file),
                            "size": file.stat().st_size,
                        }
                        for file in files
                    ],
                }
            )

    return duplicates