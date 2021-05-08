import unittest
import tests
import my_json.myjson_encode as encode
import my_json.myjson_decode as decode


def converter(obj):
    return decode.loads(encode.dumps(obj))


class TestSerializer(unittest.TestCase):

    def __init__(self, methodName):
        super().__init__(methodName)

    def test_empty_object(self):
        objects = tests.objects
        self.assertEqual(objects, converter(objects))

    def test_simple_string(self):
        objects = tests.string
        self.assertEqual(objects, converter(objects))

    def test_simple_obj_1(self):
        objects = tests.t1
        self.assertEqual(objects, converter(objects))

    def test_simple_obj_2(self):
        objects = tests.t2
        self.assertEqual(objects, converter(objects))

    def test_simple_obj_3(self):
        objects = tests.t3
        self.assertEqual(objects, converter(objects))

    def test_simple_func(self):
        objects = tests.simple_func
        result = converter(objects)
        self.assertEqual(objects.__code__, result.__code__)
        self.assertEqual(objects(), result())

    def test_func_with_globals_and_builtins(self):
        objects = tests.func_with_globals_and_builtins
        result = converter(objects)
        self.assertEqual(objects.__code__, result.__code__)
        self.assertEqual(objects(), result())

    def test_simple_lambda(self):
        objects = tests.simplelambda
        result = converter(objects)
        self.assertEqual(objects.__code__, result.__code__)
        self.assertEqual(objects(3), result(3))

    def test_func_with_defaults(self):
        objects = tests.func_with_defaults
        result = converter(objects)
        self.assertEqual(objects.__code__, result.__code__)
        self.assertEqual(objects(), result())

    def test_func_with_args_sum(self):
        objects = tests.func_with_args_sum
        result = converter(objects)
        self.assertEqual(objects.__code__, result.__code__)
        self.assertEqual(objects(2, 3, 4, 5), result(2, 3, 4, 5))

    def test_func_with_args_d(self):
        objects = tests.func_with_args_d
        result = converter(objects)
        self.assertEqual(objects.__code__, result.__code__)
        self.assertEqual(objects(a=4,b=3), result(a=4,b=3))

    def test_Empty_cls(self):
        objects = tests.Empty_cls
        result = converter(objects)()
        for i in objects().__dict__:
            self.assertEqual(getattr(objects(), i), getattr(result, i))

    def test_Simple_cls(self):
        objects = tests.Simple_cls
        result = converter(objects)()
        for i in objects().__dict__:
            self.assertEqual(getattr(objects(), i), getattr(result, i))

    def test_Cls_with_inheritance(self):
        objects = tests.Cls_with_inheritance
        result = converter(objects)()
        for i in objects().__dict__:
            self.assertEqual(getattr(objects(), i), getattr(result, i))

    def test_Cls_with_staticmethod(self):
        objects = tests.Cls_with_staticmethod
        result = converter(objects)()
        for i in objects().__dict__:
            self.assertEqual(getattr(objects(), i), getattr(result, i))

    def test_Inherited_cls(self):
        objects = tests.Inherited_cls
        result = converter(objects)()
        for i in objects().__dict__:
            self.assertEqual(getattr(objects(), i), getattr(result, i))

    def test_func_in_func(self):
        objects = tests.func_in_func
        result = converter(objects)
        self.assertEqual(objects.__code__, result.__code__)
        self.assertEqual(objects(2, 3, 4), result(2, 3, 4))
        
    def test_lambda_in_lambda(self):
        objects = tests.lambda_in_lambda
        result = converter(objects)
        self.assertEqual(objects.__code__, result.__code__)
        self.assertEqual(objects(3), converter(objects)(3))
    
    def test_lambda_in_function(self):
        objects = tests.lambda_in_function
        self.assertEqual(objects.__code__, converter(objects.__code__))
        self.assertEqual(objects(3), converter(objects)(3))
    
    def test_simplified_defaults(self):
        objects = tests.p
        result = converter(objects)
        self.assertEqual(objects.__code__, result.__code__)
        self.assertEqual(objects()(), result()())
