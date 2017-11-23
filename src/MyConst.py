from Const import Const

class MyConst(Const): pass

import sys
sys.modules[__name__]=MyConst()

