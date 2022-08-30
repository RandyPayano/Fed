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
    
    
    def categories(self):
        """Get the categories for an economic data series.
        Returns:
            _type_: _description_
        """

        url = self.url_base + "/categories"
        return self.get(url, {"series_id": self.series_id})

    def observations(self):
        """Get the observations or data values for an economic data series.

        Returns:
            _type_: _description_
        """
        url = self.url_base + "/observations"
        return self.get(url, {"series_id": self.series_id})

    def release(self):
        """Get the release for an economic data series.

        Returns:
            _type_: _description_
        """
        url = self.url_base + "/release"
        return self.get(url, {"series_id": self.series_id})

    def search(self):
        """Get economic data series that match keywords.

        Returns:
            _type_: _description_
        """
        url = self.url_base + "/search"
        return self.get(url, {"series_id": self.series_id})


test = Series(
        apikey = "127d428fd5917c2a35047e76f0b92fd0", 
        series_id = 'GNPCA'
    )


test

"""
    Series
    
    fred/series/categories - Get the categories for an economic data series.
    fred/series/observations - Get the observations or data values for an economic data series.
    fred/series/release - Get the release for an economic data series.
    fred/series/search - Get economic data series that match keywords.
    fred/series/search/tags - Get the tags for a series search.
    fred/series/search/related_tags - Get the related tags for a series search.
    fred/series/tags - Get the tags for an economic data series.
    fred/series/updates - Get economic data series sorted by when observations were updated on the FRED® server.
    fred/series/vintagedates - Get the dates in history when a series' data values were revised or new data values were released.
"""
