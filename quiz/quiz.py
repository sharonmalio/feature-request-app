from cryptography.fernet import Fernet
import unittest


def decryptMessage(key, message):
    f = Fernet(key)
    decrypted = f.decrypt(message)
    return decrypted


print(decryptMessage('TluxwB3fV_GWuLkR1_BzGs1Zk90TYAuhNMZP_0q4WyM=',
                      b'gAAAAABcOau24GKxyn_B8vNVmwXmZpF5E6GyK6yfgL8x6A43gwujo31ppHQEh0f34E7gglF8uQudEaSCXnjnGX32jCKTklBXQe1MFGLgXCIWgd2A4Z05CnVI_YBLYj0Swn_YKPC5tyBUSfe0qowFtLZXR1GZKBGFgisVviHRAPDBu-7hmI5dQYau-2b-pg3oYPVrok3UVKQz'))


if __name__ == "__main__":
    unittest.main()
