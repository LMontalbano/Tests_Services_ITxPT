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
    tree_run_monitoring = ElementTree.ElementTree(
        ElementTree.fromstring("<?xml version='1.0' encoding='UTF-8'?>\n    <SubscribeRequest>\n        "
                               "<Client-IP-Address>" + client_ip_address + "</Client-IP-Address>\n        <ReplyPort>"
                               + reply_port + "</ReplyPort>\n        <ReplyPath>" + reply_path_run_monitoring +
                               "</ReplyPath>\n "
                               "</SubscribeRequest>")
    )
    root = tree_run_monitoring.getroot()
    rxml_run_monitoring = ElementTree.tostring(root, encoding='utf8', method='xml')


    ### PlannedPattern ###
    tree_planned_pattern = ElementTree.ElementTree(
        ElementTree.fromstring("<?xml version='1.0' encoding='UTF-8'?>\n    <SubscribeRequest>\n        "
                               "<Client-IP-Address>" + client_ip_address + "</Client-IP-Address>\n        <ReplyPort>"
                               + reply_port + "</ReplyPort>\n        <ReplyPath>" + reply_path_planned_pattern +
                               "</ReplyPath>\n "
                               "</SubscribeRequest>")
    )
    root = tree_planned_pattern.getroot()
    rxml_planned_pattern = ElementTree.tostring(root, encoding='utf8', method='xml')


    ### VehicleMonitoring ###
    tree_vehicle_monitoring = ElementTree.ElementTree(
        ElementTree.fromstring("<?xml version='1.0' encoding='UTF-8'?>\n    <SubscribeRequest>\n        "
                               "<Client-IP-Address>" + client_ip_address + "</Client-IP-Address>\n        <ReplyPort>"
                               + reply_port + "</ReplyPort>\n        <ReplyPath>" + reply_path_vehicle_monitoring +
                               "</ReplyPath>\n    "
                               "</SubscribeRequest>")
    )
    root = tree_vehicle_monitoring.getroot()
    rxml_vehicle_monitoring = ElementTree.tostring(root, encoding='utf8', method='xml')


    ### JourneyMonitoring ###
    tree_journey_monitoring = ElementTree.ElementTree(
        ElementTree.fromstring("<?xml version='1.0' encoding='UTF-8'?>\n    <SubscribeRequest>\n        "
                               "<Client-IP-Address>" + client_ip_address + "</Client-IP-Address>\n        <ReplyPort>"
                               + reply_port + "</ReplyPort>\n        <ReplyPath>" + reply_path_journey_monitoring +
                               "</ReplyPath>\n    "
                               "</SubscribeRequest>")
    )
    root = tree_journey_monitoring.getroot()
    rxml_journey_monitoring = ElementTree.tostring(root, encoding='utf8', method='xml')


    ### GeneralMessage ###
    tree_general_message = ElementTree.ElementTree(
        ElementTree.fromstring("<?xml version='1.0' encoding='UTF-8'?>\n    <SubscribeRequest>\n        "
                               "<Client-IP-Address>" + client_ip_address + "</Client-IP-Address>\n        <ReplyPort>"
                               + reply_port + "</ReplyPort>\n        <ReplyPath>" + reply_path_general_message +
                               "</ReplyPath>\n    "
                               "</SubscribeRequest>")
    )
    root = tree_general_message.getroot()
    rxml_general_message = ElementTree.tostring(root, encoding='utf8', method='xml')


    ### PatternMonitoring ###
    tree_pattern_monitoring = ElementTree.ElementTree(
        ElementTree.fromstring("<?xml version='1.0' encoding='UTF-8'?>\n    <SubscribeRequest>\n        "
                               "<Client-IP-Address>" + client_ip_address + "</Client-IP-Address>\n        <ReplyPort>"
                               + reply_port + "</ReplyPort>\n        <ReplyPath>" + reply_path_pattern_monitoring +
                               "</ReplyPath>\n    "
                               "</SubscribeRequest>")
    )
    root = tree_pattern_monitoring.getroot()
    rxml_pattern_monitoring = ElementTree.tostring(root, encoding='utf8', method='xml')


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
        requests.post(address + ':' + port + "/avms/runmonitoring", data=rxml_run_monitoring, headers=headers)
    except requests.exceptions.ConnectionError as e:
        print(e)
        ServerAVMS.cancel = True

    # Request pour le module plannedpattern
    try:
        requests.post(address + ':' + port + "/avms/plannedpattern", data=rxml_planned_pattern, headers=headers)
    except requests.exceptions.ConnectionError as e:
        print(e)
        ServerAVMS.cancel = True

    # Request pour le module vehiclemonitoring
    try:
        requests.post(address + ':' + port + "/avms/vehiclemonitoring", data=rxml_vehicle_monitoring, headers=headers)
    except requests.exceptions.ConnectionError as e:
        print(e)
        ServerAVMS.cancel = True

    # Request pour le module journeymonitoring
    try:
        requests.post(address + ':' + port + "/avms/journeymonitoring", data=rxml_journey_monitoring, headers=headers)
    except requests.exceptions.ConnectionError as e:
        print(e)
        ServerAVMS.cancel = True

    # Request pour le module generalmessage
    try:
        requests.post(address + ':' + port + "/avms/generalmessage", data=rxml_general_message, headers=headers)
    except requests.exceptions.ConnectionError as e:
        print(e)
        ServerAVMS.cancel = True

    # Request pour le module patternmonitoring
    try:
        requests.post(address + ':' + port + "/avms/patternmonitoring", data=rxml_pattern_monitoring, headers=headers)
    except requests.exceptions.ConnectionError as e:
        print(e)
        ServerAVMS.cancel = True
