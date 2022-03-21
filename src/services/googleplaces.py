from multiprocessing.sharedctypes import Value
import googlemaps
import os
import sys
cur_path=os.path.abspath(os.path.dirname(__file__))
sys.path.insert(0, cur_path+"/..")

from fileReader import FileReader

class GooglePlaces:
    
    """
        Constructor method.
        Sets the API key from the file and initializes the constructor of googlemaps library
    """
    def __init__(self, configPath):
        try:
            self.setAPIKey(configPath)
            self.gmaps = googlemaps.Client(key=f'{self.API_KEY}')
        except Exception as message:
            print(message)
            sys.exit(1)

    """
        Setup the Google API Maps key by reading the credentials from config.json
    """
    def setAPIKey(self, configPath):

        if (len(configPath.strip()) == 0):
            raise ValueError('File path should not be empty')

        os.path.abspath(os.path.join(os.path.dirname( __file__ ), '..', '..'))
        file = FileReader(configPath)
        self.API_KEY = file.getFileContent()['API_KEY']
    
    """
        Method connects to Google Maps API Service to search by user input places in Kelowna.
        If query argument is empty, throw an Error and stop the program
        The result returned as a list.
    """
    def getPlaces(self, query):
        geocode_result = self.gmaps.places(f"{query} in kelowna")['results']
        result = []
        for place in geocode_result:
            result.append([place['formatted_address'], place['name']])
        return result