# Password Encryption Service

This project provides a secure way to handle user passwords by implementing password hashing and verification using the bcrypt hashing algorithm. It ensures that passwords are never stored in plain text in a database, enhancing the security of user data.

## Features

- **Hash Password**: Generates a salted, hashed password from a plain text password, ensuring that each password is uniquely salted and securely hashed.
- **Verify Password**: Checks if a provided plain text password matches a previously hashed password, allowing for secure authentication.

## Requirements

- Python 3.6+
- bcrypt library

## Installation

Before running the scripts, ensure you have Python 3.6 or later installed on your system. You will also need to install the bcrypt library. You can install the required library using pip:

```bash
pip install bcrypt

## Usage

The project includes two main functions:

1. **hash_password(password: str) -> bytes**: This function takes a plain text password as input and returns a salted, hashed password as a byte string.

2. **is_valid(hashed_password: bytes, password: str) -> bool**: This function takes a hashed password and a plain text password as inputs and returns `True` if the plain text password matches the hashed password, otherwise `False`.

### Example

```python
from encrypt_password import hash_password, is_valid

password = "MyAmazingPassw0rd"
hashed_password = hash_password(password)
print(hashed_password)  # This will print the hashed password

# Verify the password
print(is_valid(hashed_password, password))  # This should return True
```

## Security

This project uses bcrypt for hashing passwords, which is a secure choice for the following reasons:

- Automatically handles salt generation and storage.
- Designed to be computationally intensive, making brute-force attacks impractical.
- Resistant to rainbow table attacks.

## Contributing

Contributions to improve the project are welcome. Please follow the standard fork-branch-PR workflow.

## License

This project is open-sourced under the MIT License. See the LICENSE file for more details.
```
