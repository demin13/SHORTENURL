from uuid import uuid4
import base64

class BL:

    @staticmethod
    def generateShortURI():
        uuid_value = uuid4()
        uuid_bytes = uuid_value.bytes
        base64_encoded = base64.urlsafe_b64encode(uuid_bytes).decode('utf-8')
        return base64_encoded[:9]
