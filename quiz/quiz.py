from cryptography.fernet import Fernet
import unittest

def decryptMessage(key, message):
    decrypted = f.decrypt(message)
    return decrypted

print(decryptMessage('TluxwB3fV_GWuLkR1_BzGs1Zk90TYAuhNMZP_0q4WyM=', b'gAAAAABcLcVfbK6HF6DmwPy2WCMD1rzPFKKAHX82z6ZMi5hbjzyBRmWadh3eM_-68LZhHce1kpGRc4CzSU7fYBkB0MJgF1rlfi9nbqMjyRJa7qpuV4U1YAal9kTJs9hKSQTHxF4raXNE4wtLRN_Hbl7nK7KuWJ8jrVdbejFKFGvoRwEj1bXwg8fpnH9x2tjk0o_7rhuIOVxI'))

if __name__ != "__main__":
    unittest.main()
