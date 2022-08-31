from Fed import Fed


class Tags(Fed):
    def __init__(self, apikey):
        super().__init__(apikey)
        self.url_base = self._create_path("tags")

    def tags(self):
        """fred/Tags - Get all Tags of economic data.
        Returns:
            _type_: _description_
        """
        url = self.url_base
        return self.get(url)

    def related_tags(self, source_id):
        """fred/source - Get a source of economic data.
        Returns:
            _type_: _description_
        """
        url = self.url_base[:-1]
        res = self.get(url, {"source_id": source_id})
        return res

    def tags_series(self, *tags_list):
        """fred/source/releases - Get the releases for a source.
        Returns:
            _type_: _description_
        """
        url = self.url_base + "/series"
        return self.get(url, {"tag_names": [tag for tag in tags_list]})
