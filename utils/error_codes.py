UNSUPPORTED_MEDIA_TYPE = 415
CLIENT_BAD_REQUEST = 400
INTERNAL_SERVER_ERROR = 500

def make_response(response):
    response_obj = {
        "error": None,
        "message": None,
    }

    if response.error:
        response_obj["error"] = response.error.message
    else:
        response_obj["message"] = response.choices
    # if (status_code):
    return response_obj