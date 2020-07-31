import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

# Fetch the service account key JSON file contents
cred = credentials.Certificate('smartcreators-fbc59-firebase-adminsdk-kw8g5-dd0f15aa88.json')
# Initialize the app with a service account, granting admin privileges
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://smartcreators-fbc59.firebaseio.com/'
})
ref = db.reference('Criminal')

def insertData(data):
    result = ref.push({
        'Name':data["Name"],
        'Father Name':data["Father's Name"],
        'Mother Name':data["Mother's Name"],
        'Gender': data["Gender"],
        'DOB':data["DOB(yyyy-mm-dd)"],
        'Blood Group':data["Blood Group"],
        'Identification Mark':data["Identification Mark"],
        'Nationality':data["Nationality"],
        'Religion':data["Religion"],
        'Crime done':data["Crimes Done"]
    })
    return(result)

# def retrieveData(name):
#     id = None
#     crim_data = None

#     db = pymysql.connect("localhost", "criminaluser", "", "criminaldb")
#     cursor = db.cursor()
#     print("database connected")

#     query = "SELECT * FROM criminaldata WHERE name='%s'"%name

#     try:
#         cursor.execute(query)
#         result = cursor.fetchone()

#         id=result[0]
#         crim_data = {
#             "Name" : result[1],
#             "Father's Name" : result[2],
#             "Mother's Name" : result[3],
#             "Gender" : result[4],
#             "DOB(yyyy-mm-dd)" : result[5],
#             "Blood Group" : result[6],
#             "Identification Mark" : result[7],
#             "Nationality" : result[8],
#             "Religion" : result[9],
#             "Crimes Done" : result[10]
#         }

#         print("data retrieved")
#     except:
#         print("Error: Unable to fetch data")

#     db.close()
#     print("connection closed")

#     return (id, crim_data)

def retrieveData(name):
    ide = None
    crim_data = None
    #print(name)
    snapshot = ref.order_by_child('Name').equal_to(name).get()
    temp= list(snapshot.items())
    crim_data = temp[0][1]
    ide = temp[0][0]
    return(ide,crim_data)
