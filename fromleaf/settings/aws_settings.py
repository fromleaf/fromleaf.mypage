"""
 - description: AWS에서 App을 운영 중이라면, 이 Setting을 시작점으로 AWS 환경설정을 한다.
 - Author: Yun (fromleaf@gmail.com)
"""

import os

# CHECK: AWS에서는 환경설정을 이런식으로 해야하는데 APP_IS_ON_AWS = True 이렇게는 안되는 걸까?
os.environ.setdefault('APP_IS_ON_AWS', '')

from .settings import *
