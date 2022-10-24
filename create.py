import mysql.connector
import mysql.connector as sql
import requests

# Paramètres de connexion à la base de donnée.

connection = sql.connect(
  host="localhost",
  port=8889,
  user="root",
  password="root",
  database="dataengineer"
)

db_Info = connection.get_server_info()
print("Connected to MySQL Server version ", db_Info)

# Requête permettant de rajouter les colones latitude et longitude dans la table addresse.

query = "ALTER TABLE `address` ADD `longitude` VARCHAR(50) NOT NULL AFTER `postal_code`, " \
        "ADD `latitude` VARCHAR(50) NOT NULL AFTER `longitude`;"

# Requête afin de récupérer toutes les adresses dans la table address.

cursor = connection.cursor(buffered=True)
cursor.execute("SELECT `address`, `postal_code` FROM `address`")
addresses = cursor.fetchall()

# On créer une boucle afin de récupérer les adresses une par une et obtenir l'id, la rue et le code postal

for address in addresses:
    cursor.execute('SELECT `address_id` FROM `address` WHERE `address`= "%s"' % (address[0]))
    address_id = cursor.fetchone()[0]
    zip_code = address[1]

# Ex: 318+CHE+DE+ROUMAGOUA

    street = address[0].split(" ")
    sep = "+"
    request_address = sep.join(street)

# Une fois toutes les infos récupérer on va pouvoir les introduire dans l'URL grâce à la variable PARAMS

    url = "https://nominatim.openstreetmap.org/search?addressdetails=1&"
    PARAMS = {"q": request_address, "format": "json", "postalcode": zip_code, "limit": 1}
    response = requests.get(url, params=PARAMS)
    content = response.json()

# Pour les adresses dont on ne parvient pas à obtenir les informations, on va remplacer la longitude et la latitude par le mot "inconnu"

    if not content:
        cursor.execute("UPDATE `address` SET `longitude` = 'inconnu', `latitude`  = 'inconnu'  WHERE `address`.`address_id` = %d" % (address_id))
        connection.commit()
    else:
        latitude = content[0]['boundingbox'][0]
        longitude = content[0]['boundingbox'][2]
        cursor.execute("UPDATE `address` SET `longitude` = %s, `latitude`  = %s  WHERE `address`.`address_id` = %d" % (longitude, latitude, address_id))
        connection.commit()

        connection.close()






















