from app import app

def test_resume_route():
    client = app.test_client()
    response = client.get('/')
    assert response.status_code == 200
    assert b"Nathan K" in response.data
