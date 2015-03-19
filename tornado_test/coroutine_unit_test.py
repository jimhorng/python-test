'''
Created on Jan 8, 2015

@author: jimhorng
'''

from tornado.gen import coroutine, Return
from tornado.concurrent import Future
from tornado.testing import gen_test
from tornado.testing import AsyncTestCase

import mock

# import mod_under_test_1

@coroutine
def _func_inner_1(num):
    raise Return(num + 1)

@coroutine
def _func_inner_2():
    result = yield _func_inner_3()
    raise Return(result + 1)

@coroutine
def _func_inner_3():
    raise Return(3)

@coroutine
def _func_under_test_1(num):
    temp1 = yield _func_inner_1(num)
    temp2 = yield _func_inner_2()
    raise Return(temp1 + temp2 + 1)

class Test123(AsyncTestCase):

    @mock.patch("%s._func_inner_2" % __name__, autospec=True)
    @mock.patch("%s._func_inner_1" % __name__, autospec=True)
    @gen_test
    def test_1(self, mock_func_inner_1, mock_func_inner_2):
        future_1 = Future()
        future_1.set_result(9)
        mock_func_inner_1.return_value = future_1
        future_2 = Future()
        future_2.set_result(19)
        mock_func_inner_2.return_value = future_2
        result1 = yield _func_inner_1()
        print "_func_inner_1: ", result1
        result2 = yield _func_inner_2()
        print "_func_inner_2: ", result2
        result = yield _func_under_test_1()
        self.assertEqual(29, result, result)

    @gen_test
    def test_2(self):
        func_inner_1_patcher = mock.patch("%s._func_inner_1" % __name__, autospec=True)
        mock_func_inner_1 = func_inner_1_patcher.start()
        func_inner_2_patcher = mock.patch("%s._func_inner_2" % __name__, autospec=True)
        mock_func_inner_2 = func_inner_2_patcher.start()
        
        future_1 = Future()
        future_1.set_result(9)
        mock_func_inner_1.return_value = future_1
        future_2 = Future()
        future_2.set_result(19)
        mock_func_inner_2.return_value = future_2

        result1 = yield _func_inner_1(num=3)
        print "_func_inner_1: ", result1
        result2 = yield _func_inner_2()
        print "_func_inner_2: ", result2
        result = yield _func_under_test_1(5)
        print "_func_inner_1 calls: ", mock_func_inner_1.mock_calls
        self.assertEqual(29, result, result)

    @gen_test
    def test_3(self):
        func_inner_2_patcher = mock.patch("%s._func_inner_2" % __name__, autospec=True)
        mock_func_inner_2 = func_inner_2_patcher.start()

        future_2 = Future()
        future_2.set_result(2)
        mock_func_inner_2.return_value = future_2

        result1 = yield _func_inner_1(3)
        print "_func_inner_1: ", result1
        result2 = yield _func_inner_2()
        print "_func_inner_2: ", result2
        result = yield _func_under_test_1(5)
        self.assertEqual(4, result, result)

    def tearDown(self):
        mock.patch.stopall()
        super(AsyncTestCase, self).tearDown()

#     @gen_test
#     def test_4(self):
#         global _func_inner_1
#         mock_func_inner_1 = mock.create_autospec(_func_inner_1)
#         mock_func_inner_1.side_effect = Return(100)
#         _func_inner_1_original = _func_inner_1
#         _func_inner_1 = coroutine(mock_func_inner_1)
#         result = yield _func_under_test_1()
#         self.assertEqual(101, result, result)
#         
#         # clear up, reset
#         _func_inner_1 = _func_inner_1_original
#         result = yield _func_under_test_1()
#         self.assertEqual(2, result, result)

#     @gen_test
#     def test_4(self):
#         mock_func_inner_1 = mock.create_autospec(mod_under_test_1._func_inner_1)
#         mock_func_inner_1.side_effect = Return(100)
#         mock_func_inner_1 = coroutine(mock_func_inner_1)
#         mod_under_test_1._func_inner_1 = mock_func_inner_1
#         result = yield _func_under_test_1()
#         self.assertEqual(2, result, result)

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
