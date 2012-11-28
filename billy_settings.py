# @see http://billy.readthedocs.org/en/latest/configuration.html
# @see https://github.com/sunlightlabs/billy/blob/master/billy/core/default_settings.py
import os

MONGO_DATABASE = 'opengovernment_local'

# @todo Set up a compatible boundary service instance.
#BOUNDARY_SERVICE_URL  = ''

SCRAPER_PATHS = [os.path.join(os.path.dirname(os.path.abspath(__file__)), 'scrapers')]

# @see http://en.wikipedia.org/wiki/Local_government_in_the_United_States
LEVEL_FIELD = 'jurisdiction'
