import requests
import xml.etree.ElementTree as ElementTree
import ServerAVMS


def main_cli_avms(server, local):
    # Initialisation des variables
    address = "http://" + server
    port = '8000'
    client_ip_address = local
    reply_port = port
    reply_path_run_monitoring = '/RunMonitoringDeliveryReply/1'
    reply_path_planned_pattern = '/PlannedPatternDeliveryReply/1'
    reply_path_vehicle_monitoring = '/VehicleMonitoringDeliveryReply/1'
    reply_path_journey_monitoring = '/JourneyMonitoringDeliveryReply/1'
    reply_path_general_message = '/GeneralMessageDeliveryReply/1'
    reply_path_pattern_monitoring = '/PatternMonitoringDeliveryReply/1'

    ### RunMonitoring ###
    tree0 = ElementTree.ElementTree(
        ElementTree.fromstring("<?xml version='1.0' encoding='UTF-8'?>\n    <SubscribeRequest>\n        "
                               "<Client-IP-Address>" + client_ip_address + "</Client-IP-Address>\n        <ReplyPort>"
                               + reply_port + "</ReplyPort>\n        <ReplyPath>" + reply_path_run_monitoring +
                               "</ReplyPath>\n "
                               "</SubscribeRequest>")
    )
    root = tree0.getroot()
    rxml0 = ElementTree.tostring(root, encoding='utf8', method='xml')


    ### PlannedPattern ###
    tree1 = ElementTree.ElementTree(
        ElementTree.fromstring("<?xml version='1.0' encoding='UTF-8'?>\n    <SubscribeRequest>\n        "
                               "<Client-IP-Address>" + client_ip_address + "</Client-IP-Address>\n        <ReplyPort>"
                               + reply_port + "</ReplyPort>\n        <ReplyPath>" + reply_path_planned_pattern +
                               "</ReplyPath>\n "
                               "</SubscribeRequest>")
    )
    root = tree1.getroot()
    rxml1 = ElementTree.tostring(root, encoding='utf8', method='xml')


    ### VehicleMonitoring ###
    tree2 = ElementTree.ElementTree(
        ElementTree.fromstring("<?xml version='1.0' encoding='UTF-8'?>\n    <SubscribeRequest>\n        "
                               "<Client-IP-Address>" + client_ip_address + "</Client-IP-Address>\n        <ReplyPort>"
                               + reply_port + "</ReplyPort>\n        <ReplyPath>" + reply_path_vehicle_monitoring +
                               "</ReplyPath>\n    "
                               "</SubscribeRequest>")
    )
    root = tree2.getroot()
    rxml2 = ElementTree.tostring(root, encoding='utf8', method='xml')


    ### JourneyMonitoring ###
    tree3 = ElementTree.ElementTree(
        ElementTree.fromstring("<?xml version='1.0' encoding='UTF-8'?>\n    <SubscribeRequest>\n        "
                               "<Client-IP-Address>" + client_ip_address + "</Client-IP-Address>\n        <ReplyPort>"
                               + reply_port + "</ReplyPort>\n        <ReplyPath>" + reply_path_journey_monitoring +
                               "</ReplyPath>\n    "
                               "</SubscribeRequest>")
    )
    root = tree3.getroot()
    rxml3 = ElementTree.tostring(root, encoding='utf8', method='xml')


    ### GeneralMessage ###
    tree4 = ElementTree.ElementTree(
        ElementTree.fromstring("<?xml version='1.0' encoding='UTF-8'?>\n    <SubscribeRequest>\n        "
                               "<Client-IP-Address>" + client_ip_address + "</Client-IP-Address>\n        <ReplyPort>"
                               + reply_port + "</ReplyPort>\n        <ReplyPath>" + reply_path_general_message +
                               "</ReplyPath>\n    "
                               "</SubscribeRequest>")
    )
    root = tree4.getroot()
    rxml4 = ElementTree.tostring(root, encoding='utf8', method='xml')


    ### PatternMonitoring ###
    tree5 = ElementTree.ElementTree(
        ElementTree.fromstring("<?xml version='1.0' encoding='UTF-8'?>\n    <SubscribeRequest>\n        "
                               "<Client-IP-Address>" + client_ip_address + "</Client-IP-Address>\n        <ReplyPort>"
                               + reply_port + "</ReplyPort>\n        <ReplyPath>" + reply_path_pattern_monitoring +
                               "</ReplyPath>\n    "
                               "</SubscribeRequest>")
    )
    root = tree5.getroot()
    rxml5 = ElementTree.tostring(root, encoding='utf8', method='xml')


    # Création d'un headers personnalisé
    headers = {
        "Content-Length": "",
        "Accept-Encoding": "identity",
        "Host": address + ':' + port,
        "Content-Type": "text/xml"
    }

    ### POST Requests ###

    # Request pour le module runmonitoring
    try:
        requests.post(address + ':' + port + "/avms/runmonitoring", data=rxml0, headers=headers)
    except requests.exceptions.ConnectionError as e:
        print(e)
        ServerAVMS.cancel = True

    # Request pour le module plannedpattern
    try:
        requests.post(address + ':' + port + "/avms/plannedpattern", data=rxml1, headers=headers)
    except requests.exceptions.ConnectionError as e:
        print(e)
        ServerAVMS.cancel = True

    # Request pour le module vehiclemonitoring
    try:
        requests.post(address + ':' + port + "/avms/vehiclemonitoring", data=rxml2, headers=headers)
    except requests.exceptions.ConnectionError as e:
        print(e)
        ServerAVMS.cancel = True

    # Request pour le module journeymonitoring
    try:
        requests.post(address + ':' + port + "/avms/journeymonitoring", data=rxml3, headers=headers)
    except requests.exceptions.ConnectionError as e:
        print(e)
        ServerAVMS.cancel = True

    # Request pour le module generalmessage
    try:
        requests.post(address + ':' + port + "/avms/generalmessage", data=rxml4, headers=headers)
    except requests.exceptions.ConnectionError as e:
        print(e)
        ServerAVMS.cancel = True

    # Request pour le module patternmonitoring
    try:
        requests.post(address + ':' + port + "/avms/patternmonitoring", data=rxml5, headers=headers)
    except requests.exceptions.ConnectionError as e:
        print(e)
        ServerAVMS.cancel = True
