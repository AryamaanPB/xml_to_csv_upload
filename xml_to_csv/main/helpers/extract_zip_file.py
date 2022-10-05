import logging
import zipfile
import os


def extract_zip():
    """
    Extracts the .zip file that was downloaded

    Args:
        Reads the zip file from the /zip folder

    Returns: 
            True if the contents of the file are extracted
        else False
    """

    working_directory = os.getcwd()
    zip_file_path = working_directory + "/{}/{}/{}".format(
        "xml_to_csv/main/data", "zip", "esma_data.zip"
    )
    xml_file_path = working_directory + "/{}/{}".format("xml_to_csv/main/data", "xml")

    with zipfile.ZipFile(zip_file_path, "r") as zip_ref:
        try:
            result = zip_ref.extractall(xml_file_path)
        except Exception as e:
            logging.exception(e)
            return False
        return True