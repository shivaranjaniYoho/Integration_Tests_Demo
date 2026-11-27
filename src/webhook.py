
import hmac
import hashlib
import os

from fastapi import APIRouter, Request, Header, HTTPException


router = APIRouter(tags=["Webhook"])

WEBHOOK_SECRET = os.getenv(
    "WEBHOOK_SECRET",
    "my-webhook-secret"
)


@router.post("/webhook")
async def receive_webhook(
    request: Request,
    signature: str | None = Header(
        default=None,
        alias="X-Webhook-Signature"
    )
):
    if signature is None:
        raise HTTPException(
            status_code=401,
            detail="Missing signature"
        )

    body = await request.body()

    expected_signature = hmac.new(
        WEBHOOK_SECRET.encode(),
        body,
        hashlib.sha256
    ).hexdigest()

    if not hmac.compare_digest(
        expected_signature,
        signature
    ):
        raise HTTPException(
            status_code=401,
            detail="Invalid signature"
        )

    return {
        "message": "Webhook received successfully"
    }
