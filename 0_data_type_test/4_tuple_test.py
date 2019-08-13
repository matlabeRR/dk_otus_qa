def test_one(create_list_function_fixture):
    """проверяем сохранение позиций кортежа"""
    print("this is list:", create_list_function_fixture)
    team = tuple(create_list_function_fixture)
    print("this is tuple:", team)
    assert (team.index("Lebron") == 8) and (team.index("Jesus") == 6)
