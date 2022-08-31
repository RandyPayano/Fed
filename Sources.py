from Fed import Fed

class Sources(Fed):
    def __init__(self, apikey):
        super().__init__(apikey)
        self.url_base = self._create_path("sources") 
        
    def sources(self):
        """fred/sources - Get all sources of economic data.
        Returns:
            _type_: _description_
        """
        url = self.url_base 
        return self.get(url)
    
    def source(self, source_id):
        """fred/source - Get a source of economic data.
        Returns:
            _type_: _description_
        """
        url = self.url_base[:-1]
        res = self.get(url, {"source_id": source_id})
        return res
    
    def source_releases(self, source_id):
        """fred/source/releases - Get the releases for a source.
        Returns:
            _type_: _description_
        """
        url = self.url_base[:-1] + "/releases"
        return self.get(url, {"source_id": source_id})
    
