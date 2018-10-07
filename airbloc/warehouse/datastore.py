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

        # TODO: batch support
        datasource = self._sources[to]
        if datasource is None:
            raise ValueError("No datasource {} has been registered.".format(to))

        data_id = datasource.create(data.marshal())
        return Uri(protocol=to, path=data_id)

    def get(self, uri: Uri):
        raw_data = self._sources[uri.protocol].read(uri.path)
        return EncryptedData.unmarshal(raw_data)

