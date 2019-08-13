
class TestDict:
    """TestDict проверяет работу с типом dict"""
    def test_one(self, create_dict_module_fixture):
        """проверяем сохранение порядка записей в словаре"""
        print(create_dict_module_fixture)
        team_copy = create_dict_module_fixture.copy()
        assert team_copy.get(6) == "Lebron", "Значения ключа для такого значения должно быть равно Lebron"

    def test_two(self, create_dict_module_fixture):
        """проверяем обновление value для ключа"""
        print(create_dict_module_fixture)
        team_copy = create_dict_module_fixture.copy()
        team_copy[6] += "James"
        assert team_copy[6] == "LebronJames"

    def test_three(self, create_dict_module_fixture):
        """проверяем удаление элемента из словаря"""
        print(create_dict_module_fixture)
        team_copy = create_dict_module_fixture.copy()
        team_copy.__delitem__(6)
        assert ("Lebron" not in team_copy)
        print(team_copy)
