#!/usr/bin/env python3
"""basic authentication module"""

from api.v1.auth.auth import Auth
import base64
from models.user import User
from typing import TypeVar


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

    def decode_base64_authorization_header(self, base64_authorization_header:
                                           str) -> str:
        """
        Decode Authorization string
        """
        if (base64_authorization_header is None
                or not isinstance(base64_authorization_header, str)):
            return None

        try:
            decoded_data = base64.b64decode(base64_authorization_header)
            # Convert bytes to UTF-8 string
            return decoded_data.decode('utf-8')
        except Exception:
            # Return None if decoding fails
            return None
    
    def extract_user_credentials(self, decoded_base64_authorization_header: str) -> (str, str):
        """
        Extract the user email and password from the Base64 decoded value.
        Returns:
        - (None, None) if `decoded_base64_authorization_header` is None or not a string.
        - (None, None) if `decoded_base64_authorization_header` doesn't contain ':'.
        - Otherwise, return (user_email, user_password) split by ':'.
        """
        # Check if the input is None or not a string
        if decoded_base64_authorization_header is None or not isinstance(decoded_base64_authorization_header, str):
            return None, None

        # Check if the input contains ':'
        if ':' not in decoded_base64_authorization_header:
            return None, None

        # Split the string into email and password
        email, password = decoded_base64_authorization_header.split(':', 1)

        return email, password

    def user_object_from_credentials(self, user_email: str,
                                     user_pwd: str) -> TypeVar('User'):
        """
        Returns the User instance based on his email and password
        """
        if user_email is None or not isinstance(user_email, str):
            return None

        if user_pwd is None or not isinstance(user_pwd, str):
            return None
        # Search for User by email
        users = User.search({'email': user_email})
        if not users or len(users) == 0:
            return None

        # Check the password
        user = users[0]  # Assume email is Unique, so take  the first result
        if not user.is_valid_password(user_pwd):
            return None

        # Return the User instance
        return user
