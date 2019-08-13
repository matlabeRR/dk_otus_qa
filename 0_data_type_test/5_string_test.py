
class TestString:
    """
    класс TestString
    проверяет некоторые из операций сравнения строк как в чистом виде, так и после преобразований
    """
    def test_one(self, create_list_class_fixture, create_set_session_fixture):
        """проверяет длину, созданных строк из разных типов"""
        sl = str(create_list_class_fixture)   # приводим список к строке
        ss = str(create_set_session_fixture)  # приводим множество к строке
        print(type(sl), " ", type(ss))
        assert len(ss) == len(ss), \
            "строки, полученные из множества и списка должны быть одинаковой длины"

    def test_two(self, create_set_session_fixture):
        """проверяем сравнение строк. одна строка входит в другую"""
        ss = str(create_set_session_fixture)
        assert ss < (ss+" "), "строка с любым дополнительным символом будет больше идентичной"

    def test_three(self):
        """проверяем сравнение идентичных строк разных типов"""
        a1 = 'abc'
        a2 = "abc"
        a3 = '''abc'''
        assert a1 == a2 == a3, "идентичные строки должны быть равны"
        print('\n', a1, " ", a2, " ", a3)
