from functools import partial
from hashlib import sha256

def sha256_digest(path, chunksize=1024):
	md = sha256()
	with open(path, 'rb') as f:
		for buf in iter(partial(f.read, chunksize), b''):
			md.update(buf)
	return md.hexdigest()

if __name__ == '__main__':
	d1 = sha256_digest('lines.txt')
	d2 = sha256_digest('lines2.txt')
	print(d1)
	print(d2)
	print(d1 == d2)