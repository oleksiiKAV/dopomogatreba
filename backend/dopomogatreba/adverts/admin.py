# pylint: disable=no-name-in-module
# pylint: disable=no-self-argument
# pylint: disable=missing-class-docstring
# pylint: disable=trailing-whitespace

from django.contrib import admin
#from dopomogatreba.adverts import models
from adverts.models import Advert

admin.site.register(Advert)
