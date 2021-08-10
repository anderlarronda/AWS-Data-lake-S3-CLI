import boto3
import pandas as pd

# criar um cliente para interagir com AWS S3

s3_client = boto3.client('s3')

s3_client.download_file("datalake-larronda-igti",
                        "data/estado.csv",
                        "data/estado.csv")

df = pd.read_csv("data/estado.csv", sep=";")
print(df)

#s3_client.upload_file("data/estado.csv",
#                      "datalake-larronda-igti",
#                      "data/estado.csv")
