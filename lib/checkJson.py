import jsonschema


class Check():
    def checkschema(self,result):

        #校验数据格式设定
        schema = {
            "$schema": "http://json-schema.org/draft-04/schema#",
            "title": "test demo",
            "description": "validate result information",
            "type": "object",
            "properties": {
                "code": {
                    "description": "error code",
                    "type": "integer"
                },
                "name": {
                    "description": "name",
                    "type": "string"
                },
                "msg":
                {
                    "description": "msg",
                    "type": "string"
                },
                "password":
                {
                    "description": "error password",
                    "maxLength": 20,
                    "pattern": "^[a-f0-9]{20}$",  # 正则校验a-f0-9的16进制，总长度20
                    "type": "string"
                }
            },
            "required": [
                "code","name", "msg", "password"
            ]
        }

        jsonschema.validate(instance=result, schema=schema)