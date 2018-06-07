# -*- coding: utf-8 -*-
"""
Helpful snippets to make life easier
"""

import sys
python_maj_version = float(str(sys.version_info.major)+'.'+str(sys.version_info.minor))

if python_maj_version >= 3.6:
    from .encoding import Base64Util
    from .entropy import SleepUtil
    from .input_output import FileUtil
    from .unit_conversion import UnitConversion
    from .http_client import HTTPSession
    from .text_to_speach import EspeakToMe, GoogleTextToSpeach
else:
    from .http_client27 import HTTPSession

__author__ = "Sean Douglas"
__version__ = "0.1.0"
__license__ = "MIT"

