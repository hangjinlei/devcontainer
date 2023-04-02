import boto3


def create_client(service: str,
                  region_name: str,
                  endpoint_url: str,
                  aws_access_key_id: str,
                  aws_secret_access_key: str):

    return boto3.client(service,
                        region_name=region_name,
                        endpoint_url=endpoint_url,
                        aws_access_key_id=aws_access_key_id,
                        aws_secret_access_key=aws_secret_access_key)
