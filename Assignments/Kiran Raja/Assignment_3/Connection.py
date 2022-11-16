import ibm_boto3
from ibm_botocore.client import ClientError, Config


def Connect():
    # Constants for IBM COS values
    COS_ENDPOINT = "https://control.cloud-object-storage.cloud.ibm.com/v2/endpoints"
    COS_API_KEY_ID = "ooh3NCtBViC4OcbAst8bWu0tpOtWSjAK6bePVRegjwWm"
    COS_INSTANCE_CRN = "crn:v1:bluemix:public:cloud-object-storage:global:a/3f4dc006be5e4bd9b1479bccbdf51aaa:bbdccc20-0e39-4a21-bb54-da4a74b7d046::"

    # Create resource
    try:
        cos = ibm_boto3.resource("s3",
        ibm_api_key_id=COS_API_KEY_ID,
        ibm_service_instance_id=COS_INSTANCE_CRN,
        config=Config(signature_version="oauth"),
        endpoint_url=COS_ENDPOINT
        )
        print("Connected Successfully :-)")
        return cos

    except:
        print("Error while connecting !")
        return 0

def get_bucket_contents(bucket_name,cos):
    res = [
        "https://peta.s3.us-east.cloud-object-storage.appdomain.cloud/image1.jpg",
        "https://peta.s3.us-east.cloud-object-storage.appdomain.cloud/image2.jpg",
        "https://peta.s3.us-east.cloud-object-storage.appdomain.cloud/image3.jpg",
        "https://peta.s3.us-east.cloud-object-storage.appdomain.cloud/image4.jpg",
        "https://peta.s3.us-east.cloud-object-storage.appdomain.cloud/image5.jpg"
    ]
    return res