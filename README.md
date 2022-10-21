# tech_challenge_dataengineer

un test technique que j'ai du réaliser pour l'école wildcodeschool
Bienvenue dans ce tech challenge pour la formation en alternance Data Engineer.

Ce challenge a pour but de tester tes capacités en algorithmie et en base de données. Prends donc le temps de bien le travailler pour montrer le meilleur.

Entretien technique
L'entretien technique se déroulera ainsi :

Présentation des résultats du tech challenge et du code développé pour le résoudre : 5 à 10 minutes
Questions sur ce tech challenge : 5 minutes
Questions sur la compréhension du métier de Data Engineer : 10 minutes
Questions diverses : 5 min
Objectifs du tech challenge
Ton collègue Bernardo t'appelle. Il doit utiliser un nouvel outil de reporting pour présenter l'activité de l'entreprise, notamment une cartographie par répartition géographique. La base de données de l'entreprise contient les adresses postales. Mais le nouvel outil de reporting accepte uniquement les coordonnées géographiques (latitude/longitude).
Il te demande donc s'il est possible de compléter la base de données avec ces coordonnées géographiques.

1. Import de la base de données
Tu commenceras par importer le dump de la base de données MySQL sur ton ordinateur
Pour information, il s'agit d'une libre inspiration de la base "Sakila", dans laquelle nous avons notamment mis des adresses réelles. Tu dois donc impérativement partir de ce dump, et non pas de la base Sakila originale que tu pourrais trouver sur internet.

2. Collecte des coordonnées géographiques
A l'aide du langage de ton choix, tu devras récupérer les données géographiques correspondant aux adresses présentes dans la table address. L'équivalence entre adresses postales et coordonnées géographiques sera requêté depuis l'API d'OpenStreetMap : Nominatim.

3. Complétion de la base SQL
Tu modifieras ensuite la table address de la base SQL avec 2 nouvelles colonnes latitude et longitude. Puis tu ajouteras les données correspondantes pour chacune des adresses.
Tu feras un dump de cette base mise à jour que tu hébergeras sur ton compte github ou autre.

4. Requête SQL
Bernardo a une demande complémentaire avant de connecter son nouvel outil de reporting à ta base mise à jour. Pourrais-tu lui faire une requête SQL qui affiche les données suivantes : Nom du client, Prénom, Nombre de locations, Adresses postales, latitude et longitude. Il a uniquement besoin du client qui a fait le plus de locations de toute la base, afin de le féliciter.

Livrables attendus
Tu devras fournir un lien vers un repo github (ou une autre plateforme d'hébergement), contenant les éléments suivants :

Dump de la base mise à jour
Script du code utilisé pour requêter l'API et mettre à jour la base SQL
Requête SQL (partie 4) et le résultat produit par cette requête
Présentation
Lors de l'entretien technique, tu feras unes présentation incluant au moins les éléments suivants :

Outils et langages utilisés
Difficultés rencontrées (ou non)
Affichage du script
Démo avec la requête de la partie 4
Nous te demandons également de réfléchir à l'optimisation et la généralisation. C'est une question ouverte :
Si tu devais être dans un cas réel, avec une base comportant des millions de lignes et quelques adresses complémentaires chaque jour s'ajoutant à cette base, que mettrais tu en place pour optimiser les traitements ?

