import logging


def test_queue_notification_runs_background_task(client, auth_headers, caplog):
    caplog.set_level(logging.INFO, logger="app.background")

    response = client.post(
        "/tasks/notifications",
        json={"message": "send report"},
        headers=auth_headers,
    )

    assert response.status_code == 202
    assert response.json() == {"message": "notification queued"}
    assert "notification queued: send report" in caplog.messages
