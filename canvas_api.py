import requests

url='http://arm-canvas-6d-in-dell-bss-certification-int-dell6d-qa-01.apps.ocplab.6d.local/arm-master-definition-svc/api/v1/assetDetails'

params = {
    "filterSerialId" : "89855897899998739461",
    "includeAssetSpecific" : "true"
    }

headers = {
    "X-Request-ID" : "uhu9uhu8u" 
    }

response = requests.get(url, headers=headers, params=params)

op = response.json()
content = op["data"]["content"][0]


print("Product  Name : ",content["assetName"])
print("Product ICCID : ",content["serialnumber"])
print("Product ID : ",content["productId"])
print("Product Status : ",content["statusName"])
print("Product Code : ",content["productCode"])
print("Product Expiry : ",content["expiryDate"])
#Git