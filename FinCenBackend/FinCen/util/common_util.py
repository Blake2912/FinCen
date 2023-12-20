import secrets;

class CommonUtil():
    def generate_api_key():
        return secrets.token_urlsafe(32)