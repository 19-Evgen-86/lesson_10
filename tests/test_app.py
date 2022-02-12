from app import app


class TestViews:
    # выполняется перед тестом
    def setup(self):
        # создаем тестовый клиент для тестирования
        app.testing = True
        self.client = app.test_client()

    def test_page_home(self):
        response = self.client.get("/")
        assert response.status_code == 200

    def test_page_candidate(self):
        response = self.client.get("/candidates/")
        assert response.status_code == 200

    def test_candidate_search(self):
        response = self.client.get("/search_data/?Search=5")
        assert response.status_code == 200
        response = self.client.get("/search_data/?Search=flask")
        assert response.status_code == 200

    # выполняется после теста
    def teardown(self):
        pass
