import requests
import xml.etree.ElementTree as ElementTree
import logging
import sys


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


    # Configuration du logging
    logging.basicConfig(filename="std.log",
                        format='%(asctime)s %(message)s',
                        filemode='w')
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)

    # Création et configuration d'un handler
    handler = logging.StreamHandler(sys.stdout)
    handler.setLevel(logging.INFO)
    formatter = logging.Formatter('%(asctime)s - %(message)s')
    handler.setFormatter(formatter)
    logger.addHandler(handler)

    ### POST Requests ###

    try:
        # Request pour le module runmonitoring
        requests.post(address + ':' + port + "/avms/runmonitoring", data=rxml_run_monitoring, headers=headers)

        try:
            # Request pour le module plannedpattern
            requests.post(address + ':' + port + "/avms/plannedpattern", data=rxml_planned_pattern, headers=headers)

            try:
                # Request pour le module vehiclemonitoring
                requests.post(address + ':' + port + "/avms/vehiclemonitoring", data=rxml_vehicle_monitoring,
                              headers=headers)

                try:
                    # Request pour le module journeymonitoring
                    requests.post(address + ':' + port + "/avms/journeymonitoring", data=rxml_journey_monitoring,
                                  headers=headers)

                    try:
                        # Request pour le module generalmessage
                        requests.post(address + ':' + port + "/avms/generalmessage", data=rxml_general_message,
                                      headers=headers)

                        try:
                            # Request pour le module patternmonitoring
                            requests.post(address + ':' + port + "/avms/patternmonitoring",
                                          data=rxml_pattern_monitoring, headers=headers)

                        except requests.exceptions.ConnectionError as e:
                            logger.info(e)
                            logger.removeHandler(handler)
                            print("\n")
                            print("Test AVMS Fail !!!")
                            print("Please enter a valid Local and SAE address.")

                    except requests.exceptions.ConnectionError as e:
                        logger.info(e)
                        logger.removeHandler(handler)
                        print("\n")
                        print("Test AVMS Fail !!!")
                        print("Please enter a valid Local and SAE address.")

                except requests.exceptions.ConnectionError as e:
                    logger.info(e)
                    logger.removeHandler(handler)
                    print("\n")
                    print("Test AVMS Fail !!!")
                    print("Please enter a valid Local and SAE address.")

            except requests.exceptions.ConnectionError as e:
                logger.info(e)
                logger.removeHandler(handler)
                print("\n")
                print("Test AVMS Fail !!!")
                print("Please enter a valid Local and SAE address.")

        except requests.exceptions.ConnectionError as e:
            logger.info(e)
            logger.removeHandler(handler)
            print("\n")
            print("Test AVMS Fail !!!")
            print("Please enter a valid Local and SAE address.")

    except requests.exceptions.ConnectionError as e:
        logger.info(e)
        logger.removeHandler(handler)
        print("\n")
        print("Test AVMS Fail !!!")
        print("Please enter a valid Local and SAE address.")
