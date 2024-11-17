#!/usr/bin/env python3
""" Main 2 """
from api.v1.auth.basic_auth import BasicAuth

a = BasicAuth()

print(a.extract_base64_authorization_header(None))                          # Expected: None
print(a.extract_base64_authorization_header(89))                            # Expected: None
print(a.extract_base64_authorization_header("Holberton School"))            # Expected: None
print(a.extract_base64_authorization_header("Basic Holberton"))             # Expected: Holberton
print(a.extract_base64_authorization_header("Basic SG9sYmVydG9u"))          # Expected: SG9sYmVydG9u
print(a.extract_base64_authorization_header("Basic SG9sYmVydG9uIFNjaG9vbA=="))  # Expected: SG9sYmVydG9uIFNjaG9vbA==
print(a.extract_base64_authorization_header("Basic1234"))                   # Expected: None
