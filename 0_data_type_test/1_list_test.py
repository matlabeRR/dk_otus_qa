import pytest


@pytest.fixture
def create_list_fixture():
    """фикстура уровня function, создаёт список"""
    all_students = ['Alex', 'Marina', 'Boris', 'Adam', 'Olga',
                    'Mokhamed', 'Jesus', 'Moisey', 'Lebron', 'Shiva', 'Gianis']  # создаю список
    print("\nFile_fixture_setup")
    yield all_students  # используем yield вместо return
    print("\nFile_fixture_teardown")

    # def fin():
    #     print(f"\n Finalize from {request.scope} fixture!")
    # request.addfinalizer(fin)
    # return all_students #возвращаем список в фикстуру обычным return


def test_one(create_list_fixture):
    """
    используем для проверки фикстуру из этого же файла.
    проверяем длину списка после среза
    """
    print(create_list_fixture)
    new_group = create_list_fixture[:2].copy()  # делаем срез и копируем список в отдельную переменную
    assert len(new_group) == 2, "Должно быть 2"  # проверяем длину нового списка
    print(new_group)
    print("\ntest_one completed")


def test_two(create_list_function_fixture):
    """
    используем фикстуру уровня function из conftest.py
    проверяем добавление элементов в список
    """
    print(create_list_function_fixture)
    new_group = create_list_function_fixture.copy()
    new_group.append('ObiVan')  # добавляем элемент в конец списка
    assert (len(new_group) > len(create_list_function_fixture)) and (new_group.index(
        'ObiVan') == 11), "Длина нового списка должна быть больше, индекс элемента должен быть равен 11"
    print(new_group, '\nTest_two completed')


# используем фикстуру в conftest.py уровня "class"
class TestList:
    """TestList - класс проверок списка"""
    def test_three(self, create_list_class_fixture):
        """
        проверяем порядок списка после изменения
        :param create_list_class_fixture: фикстура уровня "class", создаёт список
        :return:
        """
        print(create_list_class_fixture)
        new_group = 2 * create_list_class_fixture.copy()
        print(new_group)
        assert new_group.index('Alex') == 0, "Индекс первого вхождения Alex должен быть остаться равен нулю "
        print("index == ", new_group.index('Alex'), '\nTest_three completed')

    def test_four(self, create_list_class_fixture):
        """
        Проверяем иденитчность трёх копий списка, созданных разными методами
        :param create_list_class_fixture: фикстура уровня "class", создаёт список
        :return:
        """
        print(create_list_class_fixture)
        list_1 = create_list_class_fixture.copy()
        list_2 = list(create_list_class_fixture)
        list_3 = create_list_class_fixture[:]
        print("\n", list_1, "\n", list_2, "\n", list_3)
        assert list_1 == list_2 == list_3, "Проверяем иденитчность трёх копий списка"
