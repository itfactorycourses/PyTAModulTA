from requests_folder.get_books import get_all_books


class Test_GET_All_Books:

    def test_get_all_books_no_filter(self):
        response_data = get_all_books()
        assert len(response_data.json()) == 6, f"Error: expected length: 6, actual length: {len(response_data.json())}"
        assert response_data.status_code == 200, f"Error, expected status code: 200, actual status code {response_data.status_code}"

    def test_get_all_books_filter_by_type_fiction(self):
        # response_data = get_all_books("","fiction")
        books_list_by_type_fiction = get_all_books("fiction").json()
        is_filtering_correct = True
        for item in books_list_by_type_fiction:
            if item["type"] != "fiction":
                is_filtering_correct = False
                break
        assert is_filtering_correct == True, "Error, at least one book has the wrong type"

    # de completat data viitoare:
    def test_get_all_books_filter_by_valid_limit(self):
        response_data = get_all_books(limit=3)
        assert len(response_data.json()) == 3, "Error, the number of returned books is not correct"

    def test_get_all_books_filter_by_type_and_valid_limit(self):
        response_data = get_all_books('non-fiction',3)
        is_filtering_by_type_correct = True
        for item in response_data.json():
            if item["type"] != "non-fiction":
                is_filtering_by_type_correct = False
                break
        assert is_filtering_by_type_correct == True, "Error, at least one book has the wrong type"
        assert len(response_data.json())<=3, "Error, request returned more than the designated limit of books"


    # - delete order

# ["mere","pere","nuci","covrigi"]
#    0       1      2       3