'''
Created on Jan 8, 2015

@author: jimhorng
'''

from tornado.gen import coroutine, Return
from tornado.testing import gen_test
from tornado.testing import AsyncTestCase

import mock

# import mod_under_test_1

@coroutine
def _func_inner_1():
    raise Return(1)

# @coroutine
# def _func_under_test_1():
#     temp = yield mod_under_test_1._func_inner_1()
#     raise Return(temp + 1)

@coroutine
def _func_under_test_1():
    temp = yield _func_inner_1()
    raise Return(temp + 1)

# def _func_under_test_2():
#     temp = mod_under_test_1.func_normal_1()
#     return temp

class Test123(AsyncTestCase):

    @gen_test
    @mock.patch("%s._func_inner_1" % __name__, autospec=True)
    def test_1(self, mock_func_inner_1):
        mock_func_inner_1.side_effect = Return(9)
#         mock_func_inner_1 = mock_func_inner_1
        result_1 = yield _func_inner_1()
        print 'result_1', result_1
        result = yield _func_under_test_1()
        self.assertEqual(10, result, result)

#     @gen_test
#     @patch('mod_under_test_1._func_inner_1')
#     def test_1(self, mock_func_inner_1):
#         mock_func_inner_1.side_effect = Return(9)
#         mock_func_inner_1 = coroutine(mock_func_inner_1)
#         result_1 = yield mod_under_test_1._func_inner_1()
#         print 'result_1', result_1
#         result_2 = mod_under_test_1._func_inner_1()
#         print 'result_2: ', result_2
#         result = yield _func_under_test_1()
#         self.assertEqual(10, result, result)

#     @patch('mod_under_test_1.func_normal_1')
#     def test_2(self, mock_func_normal_1):
#         mock_func_normal_1.return_value = 8
#         result = _func_under_test_2()
#         self.assertEqual(8, result, result)

#     @gen_test
#     def test_3(self):
#         @coroutine
#         def mock_func_inner_1():
#             raise Return(8)
#         mod_under_test_1._func_inner_1 = mock_func_inner_1
#         result = yield _func_under_test_1()
#         self.assertEqual(9, result, result)

    @gen_test
    def test_4(self):
        global _func_inner_1
        mock_func_inner_1 = mock.create_autospec(_func_inner_1)
        mock_func_inner_1.side_effect = Return(100)
        _func_inner_1_original = _func_inner_1
        _func_inner_1 = coroutine(mock_func_inner_1)
        result = yield _func_under_test_1()
        self.assertEqual(101, result, result)
        
        # clear up, reset
        _func_inner_1 = _func_inner_1_original
        result = yield _func_under_test_1()
        self.assertEqual(2, result, result)

#     @gen_test
#     def test_4(self):
#         mock_func_inner_1 = mock.create_autospec(mod_under_test_1._func_inner_1)
#         mock_func_inner_1.side_effect = Return(100)
#         mock_func_inner_1 = coroutine(mock_func_inner_1)
#         mod_under_test_1._func_inner_1 = mock_func_inner_1
#         result = yield _func_under_test_1()
#         self.assertEqual(2, result, result)