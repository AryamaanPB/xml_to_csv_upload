import logging
from unittest import result
import xml.etree.ElementTree as ET
import requests
import os


def download_zip():

    """
    Downloads the zip file from the link extracted from the response xml file

    Args:
        Reads the xml file from its file path
    
    Returns:
            True if the file was downloaded
        else False
    """

    working_directory = os.getcwd()
    response_file_path = working_directory + "/{}/{}/{}".format(
        "xml_to_csv/main/data", "xml", "response.xml"
    )

    response_tree = ET.parse(response_file_path)
    results = response_tree.find("result")
    docs = results.find("doc")
    download_link = docs.find('.//str[@name="download_link"]').text

    req = requests.get(download_link)

    zip_file_path = working_directory + "/{}/{}/{}".format(
        "xml_to_csv/main/data", "zip", "esma_data.zip"
    )

    try:
        open(zip_file_path, "wb").write(req.content)
    except Exception as e:
        logging.exception(e)
        return False
    return True

