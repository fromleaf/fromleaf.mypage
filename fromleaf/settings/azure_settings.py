"""
 - description: Azure에서 App을 운영 중이라면, 이 Setting을 시작점으로 AWS 환경설정을 한다.
 - Author: Yun (fromleaf@gmail.com)
"""
# TODO: 계속 Azure서비스를 사용할지는 잘 모르겠다. 지워야하나?

import os

os.environ.setdefault('APP_IS_ON_AZURE', '')

from .settings import *
