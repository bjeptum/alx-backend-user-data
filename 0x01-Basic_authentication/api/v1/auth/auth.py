#!/usr/bin/env python3
"""
Auth Class Module.
"""
from flask import Flask, request
from typing import List, TypeVar


User = TypeVar('User')


class Auth:
    """Base class to manage the API authentication"""
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """
        Determine if path requires authentication based on the excluded paths.
        Return:
                bool
        """
        if path is None:
            return True
        if not excluded_paths:
            return True

        # Remove trailing slashed to handle slash tolerance
        normalized_path = path.rstrip('/')

        for excluded in excluded_paths:
            # Normalize each excluded path similarly.
            normal_excluded = excluded.rstrip('/')
            if normalized_path == normal_excluded:
                return False  # path is excluded from authentication
        return True

    def authorization_header(self, request=None) -> str:
        """
        Return authorization header from Flask request

        Args:
            Flask request object. Defaults to None in this base class

        Returns:
            str: authorization header string or None
        """
        if request is None:
            return None
        return request.headers.get('Authorization')

    def current_user(self, request=None) -> TypeVar('User'):
        """
        Retrieves current User from the request
        Returns:
            current user (or None if not authenticated)
        """
        return None
