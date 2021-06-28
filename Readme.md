
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
docker run --rm -it 8times4/phassh-validator:latest
```
then enter your password twice, and you'll get your hash. 

Example:
```bash
% docker run --rm -it 8times4/phassh-validator:latest
Insert Password: BoredApeYachtClub420@
Repeat Password: BoredApeYachtClub420@
Your SHA-512 password hash is: $6$sCTugqKLcd33Q5gK$daUWUfRD/qD/MyMValJ./pHhUYraDOWQxeoiAgjciLDwFKlAdBRuJJGGwQwdsntqz7IdbebTC5gAGYnUU9/bP0
```

Python:
```python3
python3 validator.py
```
then enter your password twice, and you'll get your hash.

Example:
```bash
% python3 validator.py                       
Insert Password: BoredApeYachtClub420@
Repeat Password: BoredApeYachtClub420@
Your SHA-512 password hash is: $6Ykwgs.yHIpQ
```
### FYI
Your hash can look different based on your operating system, however it's still just as secure.

See [here](https://stackoverflow.com/questions/13052047/python-crypt-in-osx) for more info.
 
## ToDo:
Add some properly formatted zxcvbn output to validate complexity properly.

## Why?

Simply running ```docker run --rm --entrypoint python3 python:3 -c 'import crypt; print(crypt.crypt("YOUR_PASSWORD", crypt.mksalt(crypt.METHOD_SHA512)))'``` is simply not sufficient if you'd also want to validate password length, plus why would you want to type this command out every time you don't have your notes? 

This simplifies ssh password generations for the end user.

Main validation code, courtesy of [this StackOverflow user](https://stackoverflow.com/a/59501708).
