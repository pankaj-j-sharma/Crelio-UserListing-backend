''' Parse data recieved from external API https://randomuser.me/api/ '''

from .models import UserContact, UserInfo, UserLocation, UserLogin
from dateutil import parser

def parse_api_data(data):
    results = data['results']
    info = data['info']

    user_login=[]
    user_info = []
    user_contact = []
    user_location = []
    response_result = {'UserLogin':user_login,'UserInfo':user_info,'UserContact':user_contact,'UserLocation':user_location, 'info':info}

    for user in results:
        tmp_user_login =UserLogin(
                id = user['login']['uuid'],
                username = user['login']['username'],
                salt = user['login']['salt'],
                pwd_text = user['login']['password'],
                pwd_md5 = user['login']['md5'],
                pwd_sha = user['login']['sha1'],
                pwd_sha256 = user['login']['sha256'], 
            )
        user_login.append(tmp_user_login)

        user_info.append(
            UserInfo(
                userid = tmp_user_login,
                title = user['name']['title'],
                first = user['name']['first'],
                last = user['name']['last'],
                gender = user['gender'],
                nationality = user['nat'],
                dob = "{:%Y-%m-%d}".format(parser.parse(user['dob']['date'])),
                age = user['dob']['age'],
                reg_date = "{:%Y-%m-%d}".format(parser.parse(user['registered']['date'])),
                profile_l = user['picture']['large'],
                profile_m = user['picture']['medium'],
                profile_t = user['picture']['thumbnail']
            )
        )

        user_contact.append(
            UserContact(
                userid = tmp_user_login,
                email = user['email'],
                phone = user['phone'],
                cell = user['cell']
            )
        )

        user_location.append(
            UserLocation(
                userid = tmp_user_login,
                street_name = user['location']['street']['name'],
                street_no = user['location']['street']['number'],
                city = user['location']['city'],
                state = user['location']['state'],
                country = user['location']['country'],
                postcode = user['location']['postcode'],
                coordinates_lat = user['location']['coordinates']['latitude'],
                coordinates_long = user['location']['coordinates']['longitude'],
                timezone_offset = user['location']['timezone']['offset'],
                timezone_desc = user['location']['timezone']['description']
            )
        )

    return response_result


##########################################################################################

''' sample data '''    
'''
{
    "gender": "male",
    "name": {
        "title": "Mr",
        "first": "Hugo",
        "last": "Burgos"
    },
    "location": {
        "street": {
            "number": 8271,
            "name": "Andador Coahuila de Zaragoza"
        },
        "city": "Emiliano Zapata (Morones)",
        "state": "Chihuahua",
        "country": "Mexico",
        "postcode": 99702,
        "coordinates": {
            "latitude": "28.3897",
            "longitude": "-33.4453"
        },
        "timezone": {
            "offset": "+9:30",
            "description": "Adelaide, Darwin"
        }
    },
    "email": "hugo.burgos@example.com",
    "login": {
        "uuid": "61ed042f-65f6-40f3-810c-458a9eb24baa",
        "username": "angryrabbit341",
        "password": "antares",
        "salt": "xw9Ac9pd",
        "md5": "78692f076a1ffc47f695e44ae1088fe9",
        "sha1": "fd5f1ef049c30be263c46b5064abb20cbe2bb122",
        "sha256": "9055b561c9bdc8b7f53261335676f34dbd8fc169c0970c0beef41d310619b756"
    },
    "dob": {
        "date": "1962-06-02T08:45:17.910Z",
        "age": 60
    },
    "registered": {
        "date": "2013-02-14T21:53:24.571Z",
        "age": 9
    },
    "phone": "(658) 712 6666",
    "cell": "(652) 809 1911",
    "id": {
        "name": "NSS",
        "value": "64 78 40 5602 5"
    },
    "picture": {
        "large": "https://randomuser.me/api/portraits/men/65.jpg",
        "medium": "https://randomuser.me/api/portraits/med/men/65.jpg",
        "thumbnail": "https://randomuser.me/api/portraits/thumb/men/65.jpg"
    },
    "nat": "MX"
}


'''