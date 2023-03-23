from titlecase import title_case

class TitleCaseTests:
    def test_lower_text_is_uppercased_correctly(self):
        initial_text = 'this should be capitalized'
        expected_text = 'This should be capitalized'
        returned_text = title_case(initial_text)
        assert returned_text == expected_text