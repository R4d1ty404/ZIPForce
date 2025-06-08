import zipfile

def brute_force_zip(zip_file, wordlist):
    with zipfile.ZipFile(zip_file) as zf:
        with open(wordlist, 'r') as file:
            for line in file:
                password = line.strip()
                try:
                    zf.extractall(pwd=password.encode())
                    print(f"[✓] Password found: {password}")
                    return
                except:
                    print(f"[-] Wrong password: {password}")
    print("[-] Password not found in wordlist.")

if __name__ == "__main__":
    zip_file = input("Masukkan nama file ZIP: ")
    wordlist = input("Masukkan nama file wordlist: ")
    brute_force_zip(zip_file, wordlist)
