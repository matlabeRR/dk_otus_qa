import pytest


@pytest.fixture()
def create_list_function_fixture(request):
    """
    фикстура уровная function. создаёт список
    :param request:
    :return: list(all_students)
    """
    print(f"\n Hello from {request.scope} fixture!")
    all_students = ['Alex', 'Marina', 'Boris', 'Adam', 'Olga', 'Mokhamed', 'Jesus', 'Moisey', 'Lebron', 'Shiva',
                    'Gianis']
    return all_students

    def fin():
        print(f"\n Finalize from {request.scope} fixture!")

    request.addfinalizer(fin)


@pytest.fixture(scope="class")
def create_list_class_fixture(request):
    """
    фикстура уровня class. создаёт список
    :param request:
    :return: list(all_students)
    """
    print(f"\n Hello from {request.scope} fixture!")
    all_students = ['Alex', 'Marina', 'Boris', 'Adam', 'Olga', 'Mokhamed', 'Jesus', 'Moisey', 'Lebron', 'Shiva',
                    'Gianis']
    return all_students

    def fin():
        print(f"\n Finalize from {request.scope} fixture!")

    request.addfinalizer(fin)


@pytest.fixture(scope="module")
def create_dict_module_fixture(request):
    """
    фикстур уровня module. создаёт словарь
    :param request:
    :return: dict(team)
    """
    print(f"\n Hello from {request.scope} fixture!")
    team = \
        {
        1:'Alex',
        2:'Marina',
        3:'Boris',
        4:'Adam',
        'ya_ne_olga_ya_Artem':'Olga',
        -1:'Mokhamed',
        555:'Jesus',
        40:'Moisey',
        6:'Lebron',
        0:'Shiva',
        34:'Gianis'
        }
    return team

    def fin():
        print(f"\n Finalize from {request.scope} fixture!")

    request.addfinalizer(fin)


@pytest.fixture(scope="session")
def create_set_session_fixture(request):
    """
    фикстура уровня session. создаёт множество
    :param request: all_students
    :return: set(all_students)
    """
    print(f"\n Hello from {request.scope} fixture!")
    all_students = {'Alex', 'Marina', 'Boris', 'Adam', 'Olga', 'Mokhamed', 'Jesus', 'Moisey', 'Lebron', 'Shiva',
                    'Gianis'}
    return all_students

    def fin():
        print(f"\n Finalize from {request.scope} fixture!")

    request.addfinalizer(fin)

#
# @pytest.fixture(autouse=True)
# def create_list_always_used_fixture():
#     print(f"\n Hello, I'm fixture with autouse and funcction scope used always!")
#     all_students = ['Alex', 'Marina', 'Boris', 'Adam', 'Olga', 'Mokhamed', 'Jesus', 'Moisey', 'Lebron', 'Shiva',
#                     'Gianis']
#     return (all_students)