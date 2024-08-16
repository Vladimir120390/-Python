from pprint import pprint


class MyClass:
    def __init__(self):
        self.attribute1 = 'value1'
        self.attribute2 = 'value2'

    def method1(self):
        return 'Method 1 called'

    def method2(self):
        return 'Method 2 called'


def introspection_info(obj):
    info = {}
    info['type'] = type(obj).__name__
    info['attributes'] = [attr for attr in dir(obj) if not callable(getattr(obj, attr))]
    info['methods'] = [method for method in dir(obj) if callable(getattr(obj, method))]
    info['module'] = obj.__class__.__module__
    # Дополнительные свойства объекта (по желанию)
    if isinstance(obj, int):
        info['bit_length'] = obj.bit_length()

    return info


# Создаем объект и вызываем функцию introspection_info
my_object = MyClass()
object_info = introspection_info(my_object)
pprint(object_info)
