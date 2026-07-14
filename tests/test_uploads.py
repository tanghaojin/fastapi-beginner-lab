def test_upload_file_returns_metadata(client, auth_headers):
    response = client.post(
        "/uploads",
        files={"file": ("note.txt", b"hello fastapi", "text/plain")},
        headers=auth_headers,
    )

    assert response.status_code == 200
    assert response.json() == {
        "filename": "note.txt",
        "content_type": "text/plain",
    }
