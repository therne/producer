from urllib.parse import urlparse, parse_qs


class Uri:

    @classmethod
    def parse(cls, uri: str):
        url = urlparse(uri)
        query = parse_qs(url.query)
        return cls(url.scheme, '{}/{}'.format(url.netloc, url.path), query.id)

    def __init__(self, protocol, path, id = None):
        self.protocol = protocol
        self.path = path
        self.id = id

    def __str__(self):
        return '{}://{}/{}' + ('id={}'.format(self.id) if self.id is not None else '')
