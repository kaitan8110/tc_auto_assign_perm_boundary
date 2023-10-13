from createPolicy import createPolicy
from putRolePermissionsBoundary import putRolePermissionsBoundary
import json
import csv


# Note, newline='' is a documented requirement for the csv module
# for reading and writing CSV files.
with open('input.csv', encoding='utf-8-sig', newline='') as file:
    csvreader = csv.reader(file)

    header = []
    header = next(csvreader)
    print(header)

    for row in csvreader:
        policyName = row[1]
        ipWhitelist = row[2]
        
        createPolicyRespnse = createPolicy(policyName, ipWhitelist)
        policyDict = json.loads(createPolicyRespnse.to_json_string())

        targetUin = int(row[0])
        policyId = policyDict["PolicyId"]

        putRolePermissionsBoundary(targetUin, policyId)



# policyName = "testPolicy3"
# ipWhitelist = "127.0.0.1"

# createPolicyRespnse = createPolicy(policyName, ipWhitelist)
# policyDict = json.loads(createPolicyRespnse.to_json_string())

# targetUin = 200033544551
# policyId = policyDict["PolicyId"]

# putRolePermissionsBoundary(targetUin, policyId)


