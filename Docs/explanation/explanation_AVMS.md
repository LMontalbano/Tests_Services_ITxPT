# Explanation Test AVMS

Le Test AVMS fonctionne avec des requêtes HTTP. Dans un premier temps on vient s'inscrire au pret du serveur SAE
à différents services
(run_monitoring, planned_pattern, vehicle_monitoring, journey_monitoring, general_message, pattern_monitoring).
Ensuite suivant le service, le serveur SAE nous renvoie un flux xml contenant tout un tas d'informations. 
Certain services sont mise à jour toute les secondes tant dis ce que d'autre toutes les minutes.

Le Test ne retourne que certaines informations :
- Le **DriverID** qui correspond à la balise _DriverID_ du flux xml envoyer par le service [planned_pattern](https://github.com/LMontalbano/Tests_Services_ITxPT/blob/main/AVMS/Exemple_XML/PlannedPattern.xml)
- La **Destination** qui correspond à la balise _DestinationName_ du flux xml envoyer par le service [planned_pattern](https://github.com/LMontalbano/Tests_Services_ITxPT/blob/main/AVMS/Exemple_XML/PlannedPattern.xml)
- Le **Nom de ligne** qui correspond à la balise _ExternalLineRef_ du flux xml envoyer par le service [planned_pattern](https://github.com/LMontalbano/Tests_Services_ITxPT/blob/main/AVMS/Exemple_XML/PlannedPattern.xml)
- Le **Dernier arrêt** qui correspond à la balise _StopPointRef_ qui a pour chemin
  _"VehicleActivity/ProgressBetweenStops/PreviousCallRef/"_ au sein du flux xml envoyer par le service [vehicle_monitoring](https://github.com/LMontalbano/Tests_Services_ITxPT/blob/main/AVMS/Exemple_XML/VehicleMonitoring.xml)
  
- L'**Heure d'arrivée prévue** qui correspond à la balise _PlannedArrivalTime_ qui a pour chemin
  _"MonitoredJourney/OnwardCalls/OnwardCall/"_ au sein du flux xml envoyer par le service [journey_monitoring](https://github.com/LMontalbano/Tests_Services_ITxPT/blob/main/AVMS/Exemple_XML/JourneyMonitoring.xml)
  
- L'**Heure d'arrivée estimé** qui correspond à la balise _ExpectedArrivalTime_ qui a pour chemin
  _"MonitoredJourney/OnwardCalls/OnwardCall/"_ au sein du flux xml envoyer par le service [journey_monitoring](https://github.com/LMontalbano/Tests_Services_ITxPT/blob/main/AVMS/Exemple_XML/JourneyMonitoring.xml)