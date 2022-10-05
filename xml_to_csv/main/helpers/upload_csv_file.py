import logging
import boto3
from botocore.exceptions import ClientError
import os


def upload_csv():

    """
    Upload a file to an S3 bucket
    
    Args:
        None
    Returns:
            True if the csv file is uploaded to the S3 bucket successfully
        else False
    """

    s3_client = boto3.client(
        "s3",
        aws_access_key_id=os.environ["ACCESS_KEY_ID"],
        aws_secret_access_key=os.environ["SECRET_ACCESS_KEY"],
    )

    working_directory = os.getcwd()
    finInstrmGnlAttrbts_data_path = working_directory + "/{}/{}/{}".format(
        "xml_to_csv/main/data", "csv", "finInstrmGnlAttrbts_data.csv"
    )

    bucket_name = os.environ["BUCKET_NAME"]

    object_name = os.path.basename(finInstrmGnlAttrbts_data_path)

    # Upload the file

    try:
        response = s3_client.upload_file(
            finInstrmGnlAttrbts_data_path, bucket_name, object_name
        )
    except ClientError as e:
        logging.error(e)
        return False
    return True
