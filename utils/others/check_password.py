from hashlib import sha256


def check_sha256(trypass: str, realpass: str):
	parts = realpass.split('$')
	salt = parts[2]

	hashed = sha256((sha256(trypass.encode()).hexdigest() + salt).encode()).hexdigest()

	hashed = f'$SHA${salt}${hashed}'

	return hashed == realpass

