import zipfile


def main():
	file_name = 'Pictures.zip'
	passfile = open('password.txt', 'r')
	for word in passfile.readlines():
		password = word.strip()
		with zipfile.ZipFile(file_name) as file:
			file.extractall(pwd = bytes(password, 'utf-8'))
		print('Password Found: ' + password)
		return
	print('Sorry! password not found')


if __name__ == '__main__':
	main()
