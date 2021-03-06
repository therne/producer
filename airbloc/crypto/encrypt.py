from typing import List

from umbral import pre, config, keys, signing
from umbral.curve import SECP256K1
from .keys import Key

config.set_default_curve(SECP256K1)


class Encryptor:
    def __init__(self, key: Key):
        self.private_key = keys.UmbralPrivateKey.from_bytes(key.to_bytes())
        self.public_key = self.private_key.get_pubkey()
        self.signer = signing.Signer(private_key=self.private_key)

    def encrypt(self, data: bytes):
        cipher, capsule = pre.encrypt(self.public_key, data)
        return cipher, capsule

    def decrypt(self, cipher: bytes, capsule: bytes) -> str:
        key_capsule = pre.Capsule.from_bytes(capsule, self.private_key.params)
        decrypted_bytes = pre.decrypt(cipher, key_capsule, self.private_key)
        return str(decrypted_bytes, 'utf-8')

    def reencrypt(self, receiver_public_key: bytes) -> List[pre.KFrag]:
        receiver_pubkey = keys.UmbralPublicKey.from_bytes(receiver_public_key)

        kfrags = pre.split_rekey(delegating_privkey=self.private_key,
                                 signer=self.signer,
                                 receiving_pubkey=receiver_pubkey,
                                 threshold=10,
                                 N=20)
        return kfrags
