import json
import base64

b64_challenge = getChallenge("b64")
payload = {"challenge": b64_challenge}

licHeaders["Content-Type"] = "application/json"
licHeaders["Accept"] = "application/json"

res = corsFetch(licUrl, "POST", licHeaders, json.dumps(payload), "json")

if "license" in res:
    raw_license = res["license"]
elif "licenseResponse" in res:
    raw_license = res["licenseResponse"]
else:
    raw_license = res

licence = base64.b64decode(raw_license)
