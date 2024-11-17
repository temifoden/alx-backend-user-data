#!/usr/bin/env python3
"""basic authentication module"""

from api.v1.auth.auth import Auth


class BasicAuth(Auth):
    """Basic Auth class that inherits from Auth()"""

    def extract_base64_authorization_header(self,
                                            authorization_header: str) -> str:
        """
        Extracts the Base64 part of the authorixation
        header for basic authentication.
        """
        # Check if authorization_header is None or not a string
        if authorization_header is None or not isinstance(authorization_header,
                                                          str):
            return None

        # Check if the header starts with 'Basic ' (including space)
        if not authorization_header.startswith("Basic "):
            return None

        # Return the Base64 part after 'Basic '
        return authorization_header[len("Basic "):]
