

class Data:

    def __init__(self, payload: str, collection: str, owner_anid: str):
        self.payload = payload
        self.collection = collection
        self.owner_anid = owner_anid

    def __bytes__(self) -> bytes:
        return bytes(self.payload, 'utf-8')


class EncryptedData(Data):
    pass
