from Fed import Fed
class Series(Fed):
    def __init__(self, apikey, series_id):
        super().__init__(apikey)
        self.url_base = self._create_path("series") 
        self.series_id = series_id
        
    def series(self):
        """fred/series - Get an economic data series.
        Returns:
            _type_: _description_
        """
        url = self.url_base 
        return self.get(url, {"series_id": self.series_id})
    
    def observations(self):
        """fred/series/observations - Get the observations or data values for an economic data series.
        Returns:
            _type_: _description_
        """
        url = self.url_base + "/observations"
        return self.get(url, {"series_id": self.series_id})
    
    def release(self):
        """fred/series/release - Get the release for an economic data series.
        Returns:
            _type_: _description_
        """
        url = self.url_base + "/release"
        return self.get(url, {"series_id": self.series_id})
    
    def search(self):
        """fred/series/search - Get economic data series that match keywords.
        Returns:
            _type_: _description_
        """
        url = self.url_base + "/search"
        return self.get(url, {"series_id": self.series_id})


    def search_tags(self):
        """fred/series/search/tags - Get the tags for a series search.
        Returns:
            _type_: _description_
        """

        url = self.url_base + "/search/tags"
        return self.get(url, {"series_id": self.series_id})

    def search_related_tags(self):
        """fred/series/search/related_tags - Get the related tags for a series search.
        Returns:
            _type_: _description_
        """
        
        url = self.url_base + "/search/related_tags"
        return self.get(url, {"series_id": self.series_id})
    
    def tags(self):
        """fred/series/tags - Get the tags for an economic data series.
        Returns:
            _type_: _description_
        """

        url = self.url_base + "/tags"
        return self.get(url, {"series_id": self.series_id})

    def updates(self):
        """fred/series/updates - Get economic data series sorted by when observations were updated on the FRED® server.
        Returns:
            _type_: _description_
        """

        url = self.url_base + "/updates"
        return self.get(url, {"series_id": self.series_id})

    def vintagedates(self):
        """fred/series/vintagedates - Get the dates in history when a series' data values were revised or new data values were released.
        Returns:
            _type_: _description_
        """
        url = self.url_base + "/vintagedates"
        return self.get(url, {"series_id": self.series_id})