import logging
import re
import xml.etree.ElementTree as ET
import pandas as pd
import os


def _parse_xml():

    working_directory = os.getcwd()
    xml_file_path = working_directory + "/{}/{}/{}".format(
        "xml_to_csv/main/data", "xml" ,"DLTINS_20210117_01of01.xml"
    )

    tree = ET.parse(xml_file_path)

    finInstrmGnlAttrbts_elems = tree.findall(".//{*}FinInstrmGnlAttrbts")
    issr_elems = tree.findall(".//{*}Issr")

    return finInstrmGnlAttrbts_elems, issr_elems


def xml_to_csv():
    """
    Convert the xml file to csv.

    Args:
        None. 
        Uses file path to the xml file to load the file and then convert it.
    
    Returns:
            True if the file was converted to csv
        else False

    """
    finInstrmGnlAttrbts_elems, issr_elems = _parse_xml()

    elem_id = []
    fullNm = []
    clssfctnTp = []
    cmmdtyDerivInd = []
    ntnlCcy = []
    issr = []

    iter = 0
    for elements in finInstrmGnlAttrbts_elems:

        elem_id.append(elements.find(".//{*}Id").text)
        fullNm.append(elements.find(".//{*}FullNm").text)
        clssfctnTp.append(elements.find(".//{*}ClssfctnTp").text)
        cmmdtyDerivInd.append(elements.find(".//{*}CmmdtyDerivInd").text)
        ntnlCcy.append(elements.find(".//{*}NtnlCcy").text)
        issr.append(issr_elems[iter].text)
        iter += 1

    finInstrmGnlAttrbts_data = pd.DataFrame(
        {
            "Id": elem_id,
            "FullNm": fullNm,
            "ClssfctnTp": clssfctnTp,
            "CmmdtyDerivInd": cmmdtyDerivInd,
            "NtnlCcy": ntnlCcy,
            "Issr": issr,
        }
    )

    _save_csv(finInstrmGnlAttrbts_data)


def _save_csv(finInstrmGnlAttrbts_data):

    working_directory = os.getcwd()
    finInstrmGnlAttrbts_data_path = working_directory + "/{}/{}/{}".format(
        "xml_to_csv/main/data", "csv", "finInstrmGnlAttrbts_data.csv"
    )

    try:
        finInstrmGnlAttrbts_data.to_csv(finInstrmGnlAttrbts_data_path, index=False)
    except Exception as e:
        logging.exception(e)
        return False
    return True

