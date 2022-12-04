from Fed import Fed


class Series(Fed):
    def __init__(self, apikey):
        super().__init__(apikey)
        self.url_base = self._create_path("series")

    def series(self, series_id):
        """fred/series - Get an economic data series.
        Returns:
            _type_: _description_
        """
        url = self.url_base
        return self.get(url, {"series_id": series_id, "file_type": "json"})

    def observations(self, series_id):
        """fred/series/observations - Get the observations or data values for an economic data series.
        Returns:
            _type_: _description_
        """
        url = self.url_base + "/observations"
        return self.get(url, {"series_id": series_id, "file_type": "json"})

    def release(self, series_id):
        """fred/series/release - Get the release for an economic data series.
        Returns:
            _type_: _description_
        """
        url = self.url_base + "/release"
        return self.get(url, {"series_id": series_id, "file_type": "json"})

    def search(self, series_id):
        """fred/series/search - Get economic data series that match keywords.
        Returns:
            _type_: _description_
        """
        url = self.url_base + "/search"
        return self.get(url, {"series_id": series_id, "file_type": "json"})

    def search_tags(self, series_id):
        """fred/series/search/tags - Get the tags for a series search.
        Returns:
            _type_: _description_
        """

        url = self.url_base + "/search/tags"
        return self.get(url, {"series_id": self.series_id, "file_type": "json"})

    def search_related_tags(self, series_id):
        """fred/series/search/related_tags - Get the related tags for a series search.
        Returns:
            _type_: _description_
        """

        url = self.url_base + "/search/related_tags"
        return self.get(url, {"series_id": series_id, "file_type": "json"})

    def tags(self, series_id):
        """fred/series/tags - Get the tags for an economic data series.
        Returns:
            _type_: _description_
        """

        url = self.url_base + "/tags"
        return self.get(url, {"series_id": series_id, "file_type": "json"})

    def updates(self, series_id):
        """fred/series/updates - Get economic data series sorted by when observations were updated on the FRED® server.
        Returns:
            _type_: _description_
        """

        url = self.url_base + "/updates"
        return self.get(url, {"series_id": series_id, "file_type": "json"})

    def vintagedates(self, series_id):
        """fred/series/vintagedates - Get the dates in history when a series' data values were revised or new data values were released.
        Returns:
            _type_: _description_
        """
        url = self.url_base + "/vintagedates"
        return self.get(url, {"series_id": series_id, "file_type": "json"})

Series(Series.dev_key).series('GNPCA')