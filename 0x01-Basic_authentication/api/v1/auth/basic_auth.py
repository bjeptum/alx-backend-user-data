#!/usr/bin/env python3
"""BasicAuth module.
"""
from api.v1.auth.auth import Auth
from flask import Flask, request, Response
import base64


class BasicAuth(Auth):
    """BasicAuth class that inherits from Auth."""
    def extract_base64_authorization_header(self, authorization_header: str) -> str:
        """
        Extract the authorization_header.

        Returns:
                Base64 part of the header
        """
        if authorization_header is None:
            return None
        if not isinstance(authorization_header, str):
            return None
        if not authorization_header.startswith("Basic "):
            return None
        # Extract the part after "Basic"
        cred_header = authorization_header[len("Basic "):]
        return cred_header.strip()

    def decode_base64_authorization_header(self, base64_authorization_header: str) -> str:
        """Returns the decoded Base64 part of the header """
        if base64_authorization_header is None:
            return None
        if not isinstance(base64_authorization_header, str):
            return None
        try:
            decoded_bytes = base64.b64decode(base64_authorization_header)
            return decoded_bytes('utf-8')
        except (base64.binascii.Error, UnicodeDecodeError):
            return None
