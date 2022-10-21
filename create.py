import mysql.connector
import mysql.connector as sql
import requests

connection = sql.connect(
  host="localhost",
  port=8889,
  user="root",
  password="root",
  database="dataengineer"
)

db_Info = connection.get_server_info()
print("Connected to MySQL Server version ", db_Info)

query = "ALTER TABLE `address` ADD `longitude` VARCHAR(50) NOT NULL AFTER `postal_code`, " \
        "ADD `latitude` VARCHAR(50) NOT NULL AFTER `longitude`;"

cursor = connection.cursor()
cursor.execute("SELECT `address`, `postal_code` FROM `address`")
addresses = cursor.fetchall()
address_id = 0
for address in addresses:
    address_id = address_id + 1
    zip_code = address[1]
    while len(zip_code) < 5:
        zip_code = "0" + zip_code
    street = address[0].split(" ")
    sep = "+"
    request_address = sep.join(street)
    url = "https://nominatim.openstreetmap.org/search?"
    PARAMS = {"q": request_address, "format": "json", "postalcode": zip_code}

    response = requests.get(url, params=PARAMS)
    content = response.json()
    if not content:
        continue
    longitude = content[0]['lon']
    latitude = content[0]['lat']
    print(address_id)
    cursor.execute("UPDATE `address` SET `longitude` = %s, `latitude`  = %s  WHERE `address`.`address_id` = %d" % (longitude, latitude, address_id))
    connection.commit()






















