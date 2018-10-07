from airbloc.warehouse.uri import Uri


class DataSource:
    """ Abstract class representing a data source of the DDW. (e.g. S3, HDFS, IPFS) """

    def name(self) -> str:
        raise NotImplemented

    def create(self, payload: bytes) -> Uri:
        raise NotImplemented

    def read(self, id: str) -> bytes:
        raise NotImplemented

    def delete(self, id: str):
        raise NotImplemented
