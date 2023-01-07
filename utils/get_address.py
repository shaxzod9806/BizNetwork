# import module
from geopy.geocoders import Nominatim


# initialize Nominatim API
def get_address_name(longitude, latitude):
    geolocator = Nominatim(user_agent="geoapiExercises")
    # Latitude = "25.594095"
    # Longitude = "85.137566"
    location = geolocator.reverse(str(latitude) + "," + str(longitude))
    address = location.raw['address']
    # traverse the data
    city = address.get('city', '')
    state = address.get('state', '')
    country = address.get('country', '')

    address_dict = {
        'city': city, 'state': state, 'country': country
    }
    return address_dict
