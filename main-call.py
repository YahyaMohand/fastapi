from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()

origins = [
    "http://localhost",
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

def create_xml_string(
        str_var_device,
        str_var_row,
        str_var_chnl,
        var_protocol_path,
        str_var_fout):
    """
    Returns an XML string with the following structure:

    <?xml version="1.0" encoding="UTF-8" ?>
    <bts version="1.0">
        <cmd>start</cmd>
        <list count="1" DBC_CAN="1">
            <start ip="127.0.0.1" devtype="22" devid=str_var_device subdevid=str_var_row chlid=str_var_chnl barcode=" ">
                var_protocol_path
            </start>
            <backup backupdir="C:\BTSUser\Backup" remotedir="" filenametype="2" customfilename=str_var_fout addtimewhenrepeat="0" createdirbydate="0" filetype="2" backupontime="0" backupontimeinterval="30" backupfree="0" /> 
        </list>
    </bts>

    Parameters:
        str_var_device : str
            The device ID to use for the <start> tag's "devid" attribute.
        str_var_row : str
            The row ID to use for the <start> tag's "subdevid" attribute.
        str_var_chnl : str
            The channel ID to use for the <start> tag's "chlid" attribute.
        var_protocol_path : str
            The protocol path to use as the text content of the <start> tag.
        str_var_fout : str
            The custom filename to use for the backup file.

    Returns:
        xml_string : str
            The generated XML string.
    """

    # first define an empty string xml_string and start appending the necessary
    # XML tags and attributes to it
    xml_string = u"""<?xml version="1.0" encoding="UTF-8" ?>\n"""
    xml_string += '<bts version="1.0">\n'
    xml_string += '<cmd>start</cmd>\n'
    xml_string += '<list count="1" DBC_CAN="1">\n'
    xml_string += '<start ip="127.0.0.1" devtype="24" devid="' + str(str_var_device) + '" subdevid="' + str(str_var_row) + '" chlid="' + str(str_var_chnl) + '" barcode="D12345678901">' + var_protocol_path + '</start>\n'
    # Note that we also use double backslashes (\\) in the backupdir attribute
    # value since a single backslash is an escape character in Python strings.
    xml_string += '<backup backupdir="C:\\Program Files (x86)\\NEWARE\\BTSClient80\\Backup" remotedir="" filenametype="2" '
    xml_string += 'customfilename="' + str_var_fout + '" addtimewhenrepeat="0" createdirbydate="0" '
    xml_string += 'filetype="2" backupontime="0" backupontimeinterval="30" backupfree="0" />\n'
    xml_string += '</list>\n'
    xml_string += """</bts>\n\n"""


    print(xml_string)
    return xml_string

class BackupData(BaseModel):
    backupDirectory: str
    backupFilename: str
    backupInterval: int
    channel: int
    deviceId: int
    protocolFilename: str
    protocolFolder: str
    rowId: int

@app.post('/backup-data')
def process_backup_data(backup_data: BackupData):
    # Extract the backup data from the input
    backupDirectory = backup_data.backupDirectory
    backupFilename = backup_data.backupFilename
    backupInterval = backup_data.backupInterval
    channel = backup_data.channel
    deviceId = backup_data.deviceId
    protocolFilename = backup_data.protocolFilename
    protocolFolder = backup_data.protocolFolder
    rowId = backup_data.rowId

    # Do something with the backup data here
    # For example, print it to the console
    print("Received backup data:")
    print(f"Backup directory: {backupDirectory}")
    print(f"Backup filename: {backupFilename}")
    print(f"Backup interval: {backupInterval}")
    print(f"Channel: {channel}")
    print(f"Device ID: {deviceId}")
    print(f"Protocol filename: {protocolFilename}")
    print(f"Protocol folder: {protocolFolder}")
    print(f"Row ID: {rowId}")

    create_xml_string(deviceId,rowId,channel,protocolFolder,protocolFilename)
    # Return a success response
    return {'status': 'success'}

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host='0.0.0.0', port=8000)