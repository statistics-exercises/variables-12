try:
    import AutoFeedback.varchecks as vc
except:
    import subprocess
    import sys

    subprocess.check_call([sys.executable, "-m", "pip", "install", "AutoFeedback"])
    import AutoFeedback.varchecks as vc

import unittest
from main import *

class UnitTests(unittest.TestCase) :
    def test_fib(self) :
       fib=np.zeros(100)
       fib[0], fib[1] = 1, 1 
       for i in range(2,100) : vv = fib[i-2] + fib[i-1]
       assert( vc.check_vars("fibonacci",fib) )    