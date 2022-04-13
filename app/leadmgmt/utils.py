from fastapi.responses import JSONResponse
from fastapi import status


def jsonresponse(reasonCode,status,reasonText,responseObject,totalRecords,responseListObject):
    json={
        "reasonCode":reasonCode,
        "status":status,
        "reasonText":reasonText,
        "responseObject":responseObject,
        "totalRecords":totalRecords,
        "responseListObject":responseListObject
    }
    return json


def leadpayloadcheckschool(addSchool):
    tool_type = addSchool.tool_type

    if tool_type == "" or tool_type == None:
        return JSONResponse(status_code=status.HTTP_400_BAD_REQUEST,
                            content=jsonresponse('400', 'fail', 'data cannot be empty', '', '', ''))
    return JSONResponse(status_code=status.HTTP_200_OK,
                        content=jsonresponse("400", "fail", "Payload Valid", "", "", ""))
