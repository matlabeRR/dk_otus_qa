
class TestSet:
    """здесь мог быть ваш docstring"""
    def test_one(self, create_list_class_fixture, create_set_session_fixture):
        """проверяем вхождение элементов типа list в set"""
        l = create_list_class_fixture.copy()
        s = create_set_session_fixture.copy()
        for l in create_set_session_fixture:
            s.discard(l)
            print(l, " - молодец!")
        print(s)
        print("\n", l, " последний оставшийся в списке")
        assert len(s) == 0, "после удаления всех элементов из множества его длина равна нулю"
