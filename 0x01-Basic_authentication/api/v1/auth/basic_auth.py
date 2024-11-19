#!/usr/bin/env python3
""" BasicAuth module for hadnling Basic HTTP Authentication.

Provides a class that inherits from the 'AUth' class.
"""
from api.v1.auth.auth import Auth
from flask import Flask, request, Response
import base64


class BasicAuth(Auth):
    """ BasicAuth class that inherits from Auth.

    This class provides methods to handle Basic HTTP Authentication,
    including extracting and decoding authorization headers.
    """

    def extract_base64_authorization_header(self,
                                            authorization_header: str) -> str:
        """
        Extract the Base64 part of the Authorization header.

        Args:
            authorization_header (str)

        Returns:
            str: The Base64-encoded part of the header, or None.
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

    def decode_base64_authorization_header(self, base64_authorization_header:
                                           str) -> str:
        """
        Decode the Base64-encoded part of the Authorization header.

        Args:
            base64_authorization_header (str).

        Returns:
            str: The decoded string.

        Exceptions:
            - Returns None if the input is None or not a valid Base64 string.
        """
        if base64_authorization_header is None:
            return None
        if not isinstance(base64_authorization_header, str):
            return None
        try:
            decoded_bytes = base64.b64decode(base64_authorization_header)
            return decoded_bytes('utf-8')
        except (base64.binascii.Error, UnicodeDecodeError):
            return None
