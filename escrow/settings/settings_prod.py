import os

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.environ.get('ESCROW_NAME', 'ESCROW'),
        'USER': os.environ.get('ESCROW_USER', 'ESCROW'),
        'PASSWORD': os.environ.get('ESCROW_PASSWORD', 'ESCROW'),
        'HOST': os.environ.get('ESCROW_HOST', 'db'),
        'PORT': os.environ.get('ESCROW_PORT', '5432'),
    }
}
