# Explanation Test AVMS

The AVMS Test works with HTTP requests. First, we come to register for the loan of the SAE server
to different services
([run_monitoring](https://github.com/LMontalbano/Tests_Services_ITxPT/blob/main/AVMS/Exemple_XML/RunMonitoring.xml), 
[planned_pattern](https://github.com/LMontalbano/Tests_Services_ITxPT/blob/main/AVMS/Exemple_XML/PlannedPattern.xml),
[vehicle_monitoring](https://github.com/LMontalbano/Tests_Services_ITxPT/blob/main/AVMS/Exemple_XML/VehicleMonitoring.xml),
[journey_monitoring](https://github.com/LMontalbano/Tests_Services_ITxPT/blob/main/AVMS/Exemple_XML/JourneyMonitoring.xml),
[general_message](https://github.com/LMontalbano/Tests_Services_ITxPT/blob/main/AVMS/Exemple_XML/GeneralMessage.xml),
[pattern_monitoring](https://github.com/LMontalbano/Tests_Services_ITxPT/blob/main/AVMS/Exemple_XML/PatternMonitoring.xml)).
Then depending on the service, the SAE server sends us back an xml stream containing a lot of information.
Some services are updated every second say what others every minute.

The Test only returns certain information:
- The **DriverID** which corresponds to the "_DriverID_" tag of the xml stream sent by the service [planned_pattern](https://github.com/LMontalbano/Tests_Services_ITxPT/blob/main/AVMS/Exemple_XML/PlannedPattern.xml)
- The **Destination** which corresponds to the "_DestinationName_" tag of the xml stream sent by the service [planned_pattern](https://github.com/LMontalbano/Tests_Services_ITxPT/blob/main/AVMS/Exemple_XML/PlannedPattern.xml)
- The **Nom de ligne** which corresponds to the "_ExternalLineRef_" tag of the xml stream sent by the service [planned_pattern](https://github.com/LMontalbano/Tests_Services_ITxPT/blob/main/AVMS/Exemple_XML/PlannedPattern.xml)
- The **Dernier arrêt** which corresponds to the tag "_StopPointRef_" which has for path
  _"VehicleActivity/ProgressBetweenStops/PreviousCallRef/"_ within the xml stream sent by the service [vehicle_monitoring](https://github.com/LMontalbano/Tests_Services_ITxPT/blob/main/AVMS/Exemple_XML/VehicleMonitoring.xml)
  
- The **Heure d'arrivée prévue** which corresponds to the tag "_PlannedArrivalTime_" which has for path
  _"MonitoredJourney/OnwardCalls/OnwardCall/"_ within the xml stream sent by the service [journey_monitoring](https://github.com/LMontalbano/Tests_Services_ITxPT/blob/main/AVMS/Exemple_XML/JourneyMonitoring.xml)
  
- The **Heure d'arrivée estimé** which corresponds to the tag "_ExpectedArrivalTime_" which has for path
  _"MonitoredJourney/OnwardCalls/OnwardCall/"_ within the xml stream sent by the service [journey_monitoring](https://github.com/LMontalbano/Tests_Services_ITxPT/blob/main/AVMS/Exemple_XML/JourneyMonitoring.xml)