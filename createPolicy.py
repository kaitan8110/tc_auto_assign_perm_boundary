import json
from tencentcloud.common import credential
from tencentcloud.common.profile.client_profile import ClientProfile
from tencentcloud.common.profile.http_profile import HttpProfile
from tencentcloud.common.exception.tencent_cloud_sdk_exception import TencentCloudSDKException
from tencentcloud.cam.v20190116 import cam_client, models
import environment_variables

def createPolicy(policyName, ipWhitelist="127.0.0.1"):
    print("Creating Policy")

    try:
        # Required steps:
        # Instantiate an authentication object. The Tencent Cloud account key pair `secretId` and `secretKey` need to be passed in as the input parameters
        # This example uses the way to read from the environment variable, so you need to set these two values in the environment variable in advance
        # You can also write the key pair directly into the code, but be careful not to copy, upload, or share the code to others
        # Query the CAM key: https://console.tencentcloud.com/capi
        cred = credential.Credential(environment_variables.SECRETID, environment_variables.SECRETKEY)
        # Instantiate an HTTP option (optional; skip if there are no special requirements)
        httpProfile = HttpProfile()
        httpProfile.endpoint = "cam.tencentcloudapi.com"

        # Optional steps:
        # Instantiate a client configuration object. You can specify the timeout period and other configuration items
        clientProfile = ClientProfile()
        clientProfile.httpProfile = httpProfile
        # Instantiate an client object
        # The second parameter is the region information. You can directly enter the string "ap-guangzhou" or import the preset constant
        client = cam_client.CamClient(cred, "ap-singapore", clientProfile)

        # Instantiate a request object. You can further set the request parameters according to the API called and actual conditions
        req = models.CreatePolicyRequest()
        params = {
            "PolicyName": policyName,
            "PolicyDocument": f'{{"version":"2.0","statement":[{{"effect":"allow","action":"*","resource":"*","condition":{{"ip_equal":{{"qcs:ip":["{ipWhitelist}"]}}}}}}]}}'
        }
        
        req.from_json_string(json.dumps(params))

        # The returned "resp" is an instance of the CreatePolicyResponse class which corresponds to the request object
        resp = client.CreatePolicy(req)
        # A string return packet in JSON format is output
        return resp


    except TencentCloudSDKException as err:
        print(err)


        # Sample Policy Document
        # {
        #     "version": "2.0",
        #     "statement": [
        #         {
        #             "effect": "allow",
        #             "action": "*",
        #             "resource": "*",
        #             "condition": {
        #                 "ip_equal": {
        #                     "qcs:ip": ["127.0.0.1"]
        #                 }
        #             }
        #         }
        #     ]
        # }
