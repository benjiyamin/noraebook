from .settings import *


DATABASES = {
    'default': {
        'ENGINE': 'mysql.connector.django',
        'NAME': 'benjiyamin$noraebook',
        'USER': 'benjiyamin',
        'PASSWORD': 'ch1ck3nb0wl',
        'HOST': 'mysql.server',
    }
}


DEBUG = False
TEMPLATE_DEBUG = DEBUG


# Allow all host headers
ALLOWED_HOSTS = ['*']

