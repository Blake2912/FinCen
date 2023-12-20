class ResponseUtil():

    def create_generic_response(status_code:int, message:str, data:any):
        return {
            'status_code' : status_code,
            'message': message,
            'data': data
        }