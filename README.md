# Download and upload ESMA data as csv to an S3 bucket
### _Aryamaan Singh_


A simple application to download an [xml](https://registers.esma.europa.eu/solr/esma_registers_firds_files/select?q=*&fq=publication_date:%5B2021-01-17T00:00:00Z+TO+2021-01-19T23:59:59Z%5D&wt=xml&indent=true&start=0&rows=100) file containing a link to a zip file, the contents of which are the ESMA data in an xml format which is then converted to csv and then uploaded to an S3 bucket on AWS.

## Steps to run this project

- Specify the new link for the xml file containing the download link.
- Set up your AWS IAM credentials as environment variables in a .env file in the working directory
- Build a docker image as "internship-assignment"
- Run the docker compose file.
- Verify after a few seconds if the bucket has been updated with your csv.

## Tech
- Language : Python
- External libraries :
    * [Pandas] : A great way to automate handling of CSVs.
    * [Boto3] : Provied Python API for AWS Infrastructure tools.
    * [Requests](https://pypi.org/project/requests/) : To handle all URL related work.
    * [Elementpath](https://pypi.org/project/elementpath/) : To parse XML files.

[//]: # (These are reference links used in the body of this note and get stripped out when the markdown processor does its job. There is no need to format nicely because it shouldn't be seen. Thanks SO - http://stackoverflow.com/questions/4823468/store-comments-in-markdown-syntax)
    
   [Pandas]: <https://pandas.pydata.org/docs/getting_started/index.html>
   [Boto3]:<https://boto3.amazonaws.com/v1/documentation/api/latest/guide/quickstart.html>
   [Requests]: <https://pypi.org/project/requests/>
   [Elementpath]: <https://pypi.org/project/elementpath/>
