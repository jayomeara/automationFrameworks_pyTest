from pytest import mark

@mark.smoke

@mark.body
class BodyTests:
        @mark.door
        def test_door(self):
                assert True

        def test_bumper(self):
                assert True

        def test_windshield(self):
                assert True