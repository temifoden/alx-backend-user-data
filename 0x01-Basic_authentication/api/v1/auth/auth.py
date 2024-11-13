#!/usr/bin/env python3
"""
Auth module for API Authentication
"""
from typing import List, TypeVar
from flask import request


class Auth():
    """
    Auth class for authentication
    """
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """
        It determines if authentication is required for a gicen path
        """
        return False

    def authorization_header(self, request=None) -> str:
        """
        Retrieves the Authorization header from the request
        """
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """
        Retrieves the current user from the request
        """
        return None
