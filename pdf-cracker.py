import PyPDF2

def try_passwords(pdf_path, pass_path):
    with open(pdf_path, 'rb') as pdf_file:
        reader = PyPDF2.PdfReader(pdf_file)
        if not reader.is_encrypted:
            print("The PDF is not encrypted.")
            return
        with open(pass_path, 'r') as pw_file:
            passwords = pw_file.read().splitlines()          
        for password in passwords:
            if reader.decrypt(password):
                print(f"Password found: {password}")
                return password
        print("No valid password found.")
        return None
pdf_path = 'protected2.pdf'
pass_path = 'password.txt'
found = try_passwords(pdf_path, pass_path)
if found:
    print(f"The PDF was unlocked with the password: {found}")
else:
    print("Failed to unlock the PDF.")
