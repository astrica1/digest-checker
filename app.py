import hashlib
import os
from enum import Enum

def clear_console():
    command = 'clear'
    if os.name in ('nt', 'dos'):
        command = 'cls'
    os.system(command)

class Algorithm(Enum):
    MD5 = 1
    SHA256 = 2
    SHA512 = 3

def calculate_hash(file_path, hash_algorithm):
    hasher = hashlib.new(hash_algorithm.name.lower())
        
    with open(file_path, 'rb') as f:
        while True:
            data = f.read(65536)
            if not data:
                break
            
            hasher.update(data)
    return hasher.hexdigest()

def verify_hash(file_path, hash_algorithm, digest):
    return calculate_hash(file_path, hash_algorithm) == digest

def main():
    clear_console()
    file_path = input('Please enter file path: ')
    clear_console()
    print('''Supported Algorithms:
=====================
1.  MD5
---------------------
2.  SHA-256
---------------------
3.  SHA-512
=====================
''')
    algorithm_key = int(input('Choose hashing algorithm: '))
    hash_algorithm = Algorithm(algorithm_key)

    clear_console()
    digest = input('Enter expected digest:\n')

    if verify_hash(file_path, hash_algorithm, digest):
        print('Hash verification successful!')
    else:
        print('Hash verification failed.')
    

if __name__ == '__main__':
    main()