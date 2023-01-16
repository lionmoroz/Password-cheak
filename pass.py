import requests
import hashlib
import sys


def password_hash(input_password):
    hash = hashlib.sha1(input_password.encode('utf-8')).hexdigest().upper()
    return hash


def send_req(password):
    hash_password = password_hash(password)
    hash_password_for_req = hash_password[:5]
    url = "https://api.pwnedpasswords.com/range/"+ hash_password_for_req
    res = requests.get(url)
    if res.status_code != 200:
        raise RuntimeError(f"Some thinng failed, please check API {res.status_code}")
    return res

def response_database(password):
    hash_password = password_hash(password)
    req = send_req(password)
    data = (line.split(':') for line in req.text.splitlines())
    for h, count in data:
        if h == hash_password[5:]:
            return count
    return 0


def main(argv):
    for password in argv:
        count = response_database(password)
        if count:
            print(f'Your password - {password}- is broken {count}, please use more strong password')
        else:
            print(f'All right your password {password}, have a good secure')


main(
    sys.argv[1:]
)
