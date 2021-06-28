
# phassh-validator

phassh-validator is password complexity validator with a password hashing element(SHA-512).

The current setting validates the following criterias before hashing the provided password: 

At least, 

- 1x special character
- 1x uppercase letter
- 1x lowercase letter
- 1x number

must be used.


## Usage

Docker:
```bash
docker run --rm -it 8times4:validator
```
then enter your password twice, and you'll get your hash. 

Python:
```python3
python3 validator.py
```
then enter your password twice, and you'll get your hash.

 
## ToDo:
Add some properly formatted zxcvbn output to validate complexity properly.

## Why?

Simply running ```docker run --rm --entrypoint python3 python:3 -c 'import crypt; print(crypt.crypt("YOUR_PASSWORD", crypt.mksalt(crypt.METHOD_SHA512)))'``` is simply not sufficient if you'd also want to validate password length, plus why would you want to type this command out every time you don't have your notes? 

This simplifies ssh password generations for the end user.

Main validation code, courtesy of [this StackOverflow user](https://stackoverflow.com/a/59501708).