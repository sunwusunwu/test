#econding=utf-8
import unittest
import pytest
import time
import HTMLTestRunner

suite = unittest.defaultTestLoader.discover(start_dir="case",pattern="test*.py")
file = "./report/{}.html".format(time.strftime("%Y_%m_%d %H_%M_%S"))
with open(file,'wb') as f:
    HTMLTestRunner.HTMLTestRunner(stream=f).run(suite)
    f.close()

# if __name__ == '__main__':
#     pytest.main()