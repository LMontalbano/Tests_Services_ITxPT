import requests
import xml.etree.ElementTree as ElementTree


def main_cli_avms(server, local):
    # Initialisation des variables
    ADDRESS = "http://" + server
    PORT = '8000'
    Client_IP_Address = local
    ReplyPort = PORT
    ReplyPath_run_monitoring = '/RunMonitoringDeliveryReply/1'
    ReplyPath_planned_pattern = '/PlannedPatternDeliveryReply/1'
    ReplyPath_vehicle_monitoring = 'VehicleMonitoringDeliveryReply/1'
    ReplyPath_journey_monitoring = 'JourneyMonitoringDeliveryReply/1'
    ReplyPath_general_message = 'GeneralMessageDeliveryReply/1'
    ReplyPath_pattern_monitoring = 'PatternMonitoringDeliveryReply/1'

    ### RunMonitoring ###
    tree0 = ElementTree.ElementTree(
        ElementTree.fromstring("<?xml version='1.0' encoding='UTF-8'?>\n    <SubscribeRequest>\n        "
                               "<Client-IP-Address>" + Client_IP_Address + "</Client-IP-Address>\n        <ReplyPort>"
                               + ReplyPort + "</ReplyPort>\n        <ReplyPath>" + ReplyPath_run_monitoring +
                               "</ReplyPath>\n "
                               "</SubscribeRequest>")
    )
    root = tree0.getroot()
    rxml0 = ElementTree.tostring(root, encoding='utf8', method='xml')


    ### PlannedPattern ###
    tree1 = ElementTree.ElementTree(
        ElementTree.fromstring("<?xml version='1.0' encoding='UTF-8'?>\n    <SubscribeRequest>\n        "
                               "<Client-IP-Address>" + Client_IP_Address + "</Client-IP-Address>\n        <ReplyPort>"
                               + ReplyPort + "</ReplyPort>\n        <ReplyPath>" + ReplyPath_planned_pattern +
                               "</ReplyPath>\n "
                               "</SubscribeRequest>")
    )
    root = tree1.getroot()
    rxml1 = ElementTree.tostring(root, encoding='utf8', method='xml')


    ### VehicleMonitoring ###
    tree2 = ElementTree.ElementTree(
        ElementTree.fromstring("<?xml version='1.0' encoding='UTF-8'?>\n    <SubscribeRequest>\n        "
                               "<Client-IP-Address>" + Client_IP_Address + "</Client-IP-Address>\n        <ReplyPort>"
                               + ReplyPort + "</ReplyPort>\n        <ReplyPath>" + ReplyPath_vehicle_monitoring +
                               "</ReplyPath>\n    "
                               "</SubscribeRequest>")
    )
    root = tree2.getroot()
    rxml2 = ElementTree.tostring(root, encoding='utf8', method='xml')


    ### JourneyMonitoring ###
    tree3 = ElementTree.ElementTree(
        ElementTree.fromstring("<?xml version='1.0' encoding='UTF-8'?>\n    <SubscribeRequest>\n        "
                               "<Client-IP-Address>" + Client_IP_Address + "</Client-IP-Address>\n        <ReplyPort>"
                               + ReplyPort + "</ReplyPort>\n        <ReplyPath>" + ReplyPath_journey_monitoring +
                               "</ReplyPath>\n    "
                               "</SubscribeRequest>")
    )
    root = tree3.getroot()
    rxml3 = ElementTree.tostring(root, encoding='utf8', method='xml')


    ### GeneralMessage ###
    tree4 = ElementTree.ElementTree(
        ElementTree.fromstring("<?xml version='1.0' encoding='UTF-8'?>\n    <SubscribeRequest>\n        "
                               "<Client-IP-Address>" + Client_IP_Address + "</Client-IP-Address>\n        <ReplyPort>"
                               + ReplyPort + "</ReplyPort>\n        <ReplyPath>" + ReplyPath_general_message +
                               "</ReplyPath>\n    "
                               "</SubscribeRequest>")
    )
    root = tree4.getroot()
    rxml4 = ElementTree.tostring(root, encoding='utf8', method='xml')


    ### PatternMonitoring ###
    tree5 = ElementTree.ElementTree(
        ElementTree.fromstring("<?xml version='1.0' encoding='UTF-8'?>\n    <SubscribeRequest>\n        "
                               "<Client-IP-Address>" + Client_IP_Address + "</Client-IP-Address>\n        <ReplyPort>"
                               + ReplyPort + "</ReplyPort>\n        <ReplyPath>" + ReplyPath_pattern_monitoring +
                               "</ReplyPath>\n    "
                               "</SubscribeRequest>")
    )
    root = tree5.getroot()
    rxml5 = ElementTree.tostring(root, encoding='utf8', method='xml')


    # Création d'un headers personnalisé
    headers = {
        "Content-Length": "",
        "Accept-Encoding": "identity",
        "Host": ADDRESS + ':' + PORT,
        "Content-Type": "text/xml"
    }

    ### POST Requests ###

    # Request pour le module runmonitoring
    r0 = requests.post(ADDRESS + ':' + PORT + "/avms/runmonitoring", data=rxml0, headers=headers)

    # Request pour le module plannedpattern
    r1 = requests.post(ADDRESS + ':' + PORT + "/avms/plannedpattern", data=rxml1, headers=headers)

    # Request pour le module vehiclemonitoring
    r2 = requests.post(ADDRESS + ':' + PORT + "/avms/vehiclemonitoring", data=rxml2, headers=headers)

    # Request pour le module journeymonitoring
    r3 = requests.post(ADDRESS + ':' + PORT + "/avms/journeymonitoring", data=rxml3, headers=headers)

    # Request pour le module generalmessage
    r4 = requests.post(ADDRESS + ':' + PORT + "/avms/generalmessage", data=rxml4, headers=headers)

    # Request pour le module patternmonitoring
    r5 = requests.post(ADDRESS + ':' + PORT + "/avms/patternmonitoring", data=rxml5, headers=headers)
