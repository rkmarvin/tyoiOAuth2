class OAuth2Error(Exception):
    pass


class UnsupportedGrantTypeError(OAuth2Error):
    pass


class OAuth2Client(object):
    def __init__(self, client_id, client_secret, grant_type,
                 access_token_endpoint, auth_endpoint=None, redirect_uri=None,
                 scope=None):
        if grant_type not in ('authorization_code', 'client_credentials'):
            raise UnsupportedGrantTypeError('Unsupported grant type "%s"' %
                                            grant_type)

        if 'authorization_code' == grant_type and auth_endpoint is None:
            raise OAuth2Error('auth_endpoint is required with the\
                               authorization_code grant type')

        self._client_id = client_id
        self._client_secret = client_secret
        self._grant_type = grant_type
        self._access_token_endpoint = access_token_endpoint
        self._auth_endpoint = auth_endpoint
        self._redirect_uri = redirect_uri
        self._scope = scope
