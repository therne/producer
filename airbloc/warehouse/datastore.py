from typing import List

from airbloc.data import EncryptedData
from airbloc.warehouse import DataSource
from airbloc.warehouse.uri import Uri


class DataStore:
    """ Decentralized Data Warehouse implementation."""

    def __init__(self, sources: List[DataSource], default=None):
        self._sources = {source.name(): source for source in sources}
        self.default = default

    def add_data_source(self, source: DataSource):
        self._sources[source.name()] = source

    def store(self, data: EncryptedData, to=None) -> Uri:
        if to is None:
            to = self.default

        datasource = self._sources[to]
        if datasource is None:
            raise ValueError("No datasource {} has been registered.".format(to))

        return datasource.create(data.payload)

    def get(self, id: str):
        raise NotImplemented
