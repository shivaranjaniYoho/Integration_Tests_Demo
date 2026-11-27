
import hmac
import hashlib
import json

from fastapi.testclient import TestClient

from src.main import app


WEBHOOK_SECRET = "my-webhook-secret"


def create_signature(payload):
    body = json.dumps(payload).encode()

    signature = hmac.new(
        WEBHOOK_SECRET.encode(),
        body,
        hashlib.sha256
    ).hexdigest()

    return body, signature


def test_valid_webhook():
    payload = {"event": "payment_completed"}

    body, signature = create_signature(payload)

    client = TestClient(app)

    response = client.post(
        "/webhook",
        content=body,
        headers={
            "Content-Type": "application/json",
            "X-Webhook-Signature": signature
        }
    )

    assert response.status_code == 200
    assert response.json() == {
        "message": "Webhook received successfully"
    }


def test_tampered_webhook():
    payload = {"event": "payment_completed"}

    body, signature = create_signature(payload)

    tampered_body = json.dumps(
        {"event": "payment_failed"}
    ).encode()

    client = TestClient(app)

    response = client.post(
        "/webhook",
        content=tampered_body,
        headers={
            "Content-Type": "application/json",
            "X-Webhook-Signature": signature
        }
    )

    assert response.status_code == 401


def test_missing_webhook_signature():
    payload = {"event": "payment_completed"}

    body = json.dumps(payload).encode()

    client = TestClient(app)

    response = client.post(
        "/webhook",
        content=body,
        headers={
            "Content-Type": "application/json"
        }
    )

    assert response.status_code == 401
