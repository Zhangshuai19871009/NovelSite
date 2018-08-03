import os
from django.apps import AppConfig

default_app_config = 'readStatistics.PrimaryReadStatisticsConfig'

VERBOSE_APP_NAME = '阅读管理'

def get_current_app_name(_file):
    return os.path.split(os.path.dirname(_file))[-1]

class PrimaryReadStatisticsConfig(AppConfig):
    name = get_current_app_name(__file__)
    verbose_name = VERBOSE_APP_NAME