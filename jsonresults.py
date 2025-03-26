import json
import sys

FileInfo = {"md5": "null", "sha1": "null", "sha256": "null", "Imphash": "null", "File type": "null", "File size": "null", "File Name": "null", "CA Issuer": "null", "CA Owner": "null", "CA Valid From": "null", "CA Valid Until": "null",
"CA Root Issuer": "null", "CA Root Owner": "null", "CA Root Valid From": "null", "CA Root Valid Until": "null", "CA Valid": "null", "AV Detect": "null", "Threat Level": "null", "Threat Score": "null", "Verdict": "null"}
Err ={"hash": "null", "message": "null"}
class JSONRESULTS:

    def __init__(self, lst, hash):
        self.lst = lst
        self.hash = hash

    def parse(self):
        if self.lst:
            if 'message' in self.lst:
                Err["hash"] = self.hash
                Err["message"] = "Provided value is not one of expected hashes (MD5, SHA1, SHA256)."
                return Err, "error"
            for i in self.lst:
                if FileInfo["md5"] != i['md5']:
                    FileInfo["md5"] = i['md5']
                if  FileInfo["sha1"] != i['sha1']:
                    FileInfo["sha1"] = i['sha1']
                if FileInfo["sha256"] != i['sha256']:
                    FileInfo["sha256"] = i['sha256']
                if  FileInfo["Imphash"] != i['imphash']:
                    FileInfo["Imphash"] = i['imphash']
                if FileInfo["File type"] != i['type']:
                    FileInfo["File type"] = i['type']
                if  FileInfo["File size"] != i['size']:
                    FileInfo["File size"] = i['size']
                if FileInfo["File Name"] != i['submit_name']:
                    FileInfo["File Name"] = i['submit_name']
                if i['certificates']:
                    if  FileInfo["CA Issuer"] != i['certificates'][0]['issuer']:
                        FileInfo["CA Issuer"] = i['certificates'][0]['issuer']
                    if  FileInfo["CA Owner"] != i['certificates'][0]['owner']:
                        FileInfo["CA Owner"] = i['certificates'][0]['owner']
                    if  FileInfo["CA Valid From"] != i['certificates'][0]['valid_from']:
                        FileInfo["CA Valid From"] = i['certificates'][0]['valid_from']
                    if  FileInfo["CA Valid Until"] != i['certificates'][0]['valid_until']:
                        FileInfo["CA Valid Until"] = i['certificates'][0]['valid_until']
                    if  FileInfo["CA Root Issuer"] != i['certificates'][1]['issuer']:
                        FileInfo["CA Root Issuer"] = i['certificates'][1]['issuer']
                    if  FileInfo["CA Root Owner"] != i['certificates'][1]['owner']:
                        FileInfo["CA Root Owner"] = i['certificates'][1]['owner']
                    if  FileInfo["CA Root Valid From"] != i['certificates'][1]['valid_from']:
                        FileInfo["CA Root Valid From"] = i['certificates'][1]['valid_from']
                    if  FileInfo["CA Root Valid Until"] != i['certificates'][1]['valid_until']:
                        FileInfo["CA Root Valid Until"] = i['certificates'][1]['valid_until']
                if isinstance(i['is_certificates_valid'], bool):
                    FileInfo["CA Valid"] = str(i['is_certificates_valid'])
                if FileInfo["AV Detect"] != i['av_detect']:
                    FileInfo["AV Detect"] = i['av_detect']
                if FileInfo["Threat Level"] != i['threat_level']:
                    FileInfo["Threat Level"] = i['threat_level']
                if FileInfo["Threat Score"] != str(i['threat_score']):
                    FileInfo["Threat Score"] = str(i['threat_score'])
                if FileInfo["Verdict"] != i['verdict']:
                    FileInfo["Verdict"] = i['verdict']
            return FileInfo, "Found"            
        else:
            Err["hash"] = self.hash
            Err["message"] = "hash was not found"
            return Err, "Not Found"

    def run(self):
        parsed_lst, msg = self.parse()
        parsed_lst = json.dumps(parsed_lst)
        if msg == "Found":
            result = open("results.json","a+")
            result.write(str(parsed_lst)+"\n")
            result.close()
        elif msg == "Not Found":
            result = open("NotFound.json","a+")
            result.write(str(parsed_lst)+"\n")
            result.close()
        else:
            result = open("error.json","a+")
            result.write(str(parsed_lst)+"\n")
            result.close()