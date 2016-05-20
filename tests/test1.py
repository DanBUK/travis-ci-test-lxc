import unittest

def fun(x):
  return x + 1

def badfun(x):
  return x


class MyTest(unittest.TestCase):
  def test(self):
    self.assertEqual(fun(3), 4)
#     self.assertEqual(badfun(3), 4)

if __name__ == '__main__':
  unittest.main()
