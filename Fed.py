import requests 

class Fed:
    def __init__(self, apikey):
        self.apikey = apikey
        self.url_base = "https://api.stlouisfed.org/fred/"

    def get(self, URL, parameter = {}):
        parameter['api_key'] = self.apikey
        url_params = {}
        for key, value in parameter.items():
            if value is not None:
                url_params[key] = value
        response = requests.get(URL, params = url_params)
        return response.status_code, response.text    

    def _create_path(self, *args):
        """Create the URL path with the Fred endpoint and given arguments."""
        args = filter(None, args)
        path = self.url_base + '/'.join(args)
        return path 
    def series(self):
        return Series(self.apikey)

######################################################################################3
class Series(Fed):
    def __init__(self, apikey, series_id):
        super().__init__(apikey)
        self.url_base = self._create_path("series") 
        self.series_id = series_id
        
        def categories(self):
            """Get the categories for an economic data series.
            Returns:
                _type_: _description_
            """

            url = self.url_base + "/release"
            return self.get(url, {"series_id": self.series_id})

        def observations(self):
            """Get the observations or data values for an economic data series.

            Returns:
                _type_: _description_
            """
            url = self.url_base + "/release"
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
            url = self.url_base + "/release"
            return self.get(url, {"series_id": self.series_id})

        def search_tags(self):
            """Get the tags for a series search.

            Returns:
                _type_: _description_
            """
            url = self.url_base + "/release"
            return self.get(url, {"series_id": self.series_id})
        def search_related_tags_tags(self):
            """ Get the related tags for a series search.

            Returns:
                _type_: _description_
            """
            url = self.url_base + "/release"
            return self.get(url, {"series_id": self.series_id})
            
        def tags(self):
            """ Get the tags for an economic data series.
            Returns:
                _type_: _description_
            """
            url = self.url_base + "/tags"
            return self.get(url, {"series_id": self.series_id})
            
        def release(self):
            """_summary_
            Returns:
                _type_: _description_
            """
            url = self.url_base + "/release"
            return self.get(url, {"series_id": self.series_id})

        def updates(self):
            """Get economic data series sorted by when observations were updated on the FRED® server.
            Returns:
                _type_: _description_
            """
            url = self.url_base + "/release"
            return self.get(url, {"series_id": self.series_id})

        def vintagedates(self):
            """Get the dates in history when a series' data values were revised or new data values were released.
            Returns:
                _type_: _description_
            """
            url = self.url_base + "/tags"
            return self.get(url, {"series_id": self.series_id})



test = Series(
        apikey = "127d428fd5917c2a35047e76f0b92fd0", 
        series_id = 'GNPCA'
    )

test.release()
















"""
    Series
    fred/series - Get an economic data series.
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
