from bson import BSON
from base64 import b64encode


class Data:

    def __init__(self, payload: str, collection: str, owner_anid: str):
        self.payload = payload
        self.collection = collection
        self.owner_anid = owner_anid

    @classmethod
    def unmarshal(cls, bson: bytes) -> 'Data':
        document = BSON.decode(bson)
        return cls(payload=document['payload'],
                   collection=document['collection'],
                   owner_anid=document['owner_anid'])

    def marshal(self) -> bytes:
        return BSON.encode(document={
            'payload': self.payload,
            'collection': self.collection,
            'owner': self.owner_anid,
        })

    def __bytes__(self) -> bytes:
        return self.marshal()


class EncryptedData(Data):

    def __init__(self, payload: bytes, capsule: bytes, collection: str, owner_anid: str):
        self.payload = payload
        self.capsule = capsule
        self.collection = collection
        self.owner_anid = owner_anid

    @classmethod
    def unmarshal(cls, bson: bytes):
        document = BSON.decode(bson)
        return cls(payload=document['payload'],
                   capsule=document['capsule'],
                   collection=document['collection'],
                   owner_anid=document['owner_anid'])

    def marshal(self) -> bytes:
        return BSON.encode(document={
            'payload': self.payload,
            'capsule': self.capsule,
            'collection': self.collection,
            'owner': self.owner_anid,
        })

    def __repr__(self):
        return dict.__repr__({
            'payload': b64encode(self.payload.decode()).decode('utf-8'),
            'capsule': b64encode(self.capsule.decode()).decode('utf-8'),
            'collection': self.collection,
            'owner': self.owner_anid,
        })
