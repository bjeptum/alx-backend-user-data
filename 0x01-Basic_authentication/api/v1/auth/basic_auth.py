#!/usr/bin/env python3
"""
BasicAuth module.
"""
from api.v1.auth.auth import Auth
from flask import Flask, request, Response
import base64


class BasicAuth(Auth):
    """BasicAuth class that inherits from Auth."""
    def extract_base64_authorization_header(self,
                                            authorization_header: str) -> str:
        """Returns base64 encoded"""
        if authorization_header is None:
            return None
        if not isinstance(authorization_header, str):
            return None
        if not authorization_header.startswith("Basic "):
            return None
        # Extract the part after "Basic"
        cred_header = authorization_header[len("Basic "):]
        return cred_header.strip()

        """
        Encode the extracted part to Base64
        base64_encoded = base64.b64encode(cred_header.encode('utf-8'))
        return base64_encoded.decode('utf-8')
        """
