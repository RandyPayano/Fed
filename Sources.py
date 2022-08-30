from Fed import Fed

class Sources(Fed):
    def __init__(self, apikey, series_id):
        super().__init__(apikey)
        self.url_base = self._create_path("sources") 
        self.series_id = series_id
        
    def sources(self):
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
    