import logging
import requests
import os


def download_xml():
    """
    Download the xml file from the link provided on the Github Wiki page for this assignment

    Args:
        None.
    
    Returns:
            True if the xml file was downloaded
        else False
    """

    url = "https://registers.esma.europa.eu/solr/esma_registers_firds_files/select?q=*&fq=publication_date:%5B2021-01-17T00:00:00Z+TO+2021-01-19T23:59:59Z%5D&wt=xml&indent=true&start=0&rows=100"

    response = requests.get(url)

    response_file_path = os.getcwd() + "/{}/{}/{}".format("xml_to_csv/main/data", "xml", "response.xml")

    try:
        with open(response_file_path, "wb") as file:
            file.write(response.content)
    except Exception as e:
        logging.exception(e)
        return False
    return True