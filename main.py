class URL_shortener:
    urlid2 = {}
    id = 1000000

    def __init__(self, url):
        self.url = url

    def shorten_url(self, url):
        if self.url in self.urlid2:
            shortened_id = self.urlid2[self.url]
        else:
            self.urlid2[self.url] = self.id
            shortened_id = self.encode(self.id)
            self.id += 1

        return f"http://127.0.0.1:5000/{shortened_id}"

    @classmethod
    def get_original_url(cls, shortened_id):
        for url, sid in cls.urlid2.items():
            if str(sid) == shortened_id:
                return url
        return None

    def encode(self, id):
        characters = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
        base = len(characters)

        if id == 0:
            return characters[0]

        ret = []

        while id > 0:
            value = id % base
            ret.append(characters[value])
            id = id // base

        return "".join(ret[::-1])
