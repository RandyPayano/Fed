import requests 
dev_key = "127d428fd5917c2a35047e76f0b92fd0"
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
        print(URL)
        response = requests.get(URL, params = url_params)
        return response.status_code, response.text    

    def _create_path(self, *args):
        """Create the URL path with the Fred endpoint and given arguments."""
        args = filter(None, args)
        path = self.url_base + '/'.join(args)
        return path 