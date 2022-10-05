from cmath import log
from helpers.download_xml_file import download_xml
from helpers.download_zip_file import download_zip
from helpers.extract_zip_file import extract_zip
from helpers.parse_xml_to_csv_file import xml_to_csv
from helpers.upload_csv_file import upload_csv

import logging
import os


def main():
    """
    Controller module that initiates the entire process of downloading, parsing and converting the ESMA data to a CSV

    Args:
        None
    
    Returns:
            None
    """

    working_directory = os.getcwd()
    logs_file_path = working_directory + "\{}\{}\{}".format("main","logs", "logs.txt")

    logging.basicConfig(filename=logs_file_path, level=logging.DEBUG)

    logging.debug("Begin logging")

    res_download_xml = download_xml()
    if(res_download_xml):
        logging.info("Downloaded the XML with the ESMA Data download link")
    else:
        logging.error("Could not download the XML")

    res_download_zip = download_zip()
    if(res_download_zip):
        logging.info("Downloaded the ZIP from the download link")
    else:
        logging.error("Could not download the ZIP file")

    res_extract_zip = extract_zip()
    if(res_extract_zip):
        logging.info("Extracted contents from the ZIP into the /data/xml folder")
    else:
        logging.error("Could not extract the ZIP file")

    res_xml_to_csv = xml_to_csv()
    if(res_xml_to_csv):
        logging.info("Converting the XML to a CSV file")
    else:
        logging.error("Could not convert the XML file to CSV")

    res_upload_csv = upload_csv()
    if(res_upload_csv):
        logging.info("Uploading the CSV to an S3 bucket in AWS")
    else:
        logging.error("Could not upload the ESMA csv to an S3 bucket")


if __name__ == "__main__":
    main()
