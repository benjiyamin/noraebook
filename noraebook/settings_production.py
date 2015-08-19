from .settings import *


DEBUG = False
TEMPLATE_DEBUG = DEBUG


# Allow all host headers
ALLOWED_HOSTS = ['*']


DATABASES = {
    'default': {
        'ENGINE': 'mysql.connector.django',
        'NAME': 'benjiyamin$noraebook',
        'USER': 'benjiyamin',
        'PASSWORD': 'ch1ck3nb0wl',
        'HOST': 'benjiyamin.mysql.pythonanywhere-services.com',
    }
}
