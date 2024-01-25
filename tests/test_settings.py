from studiofard.settings import *  # noqa
from studiofard.settings import SECRET_KEY

del SECRET_KEY

SECRET_KEY = 'super_secret_key'  # pragma: allowlist secret
