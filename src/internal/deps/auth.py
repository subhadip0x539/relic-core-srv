from typing import Annotated, Optional
from fastapi import Depends, HTTPException, status, Header
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from internal.domain.auth import TokenClaims, Role
from internal.domain.error import InvalidTokenError, ForbiddenError
import jwt
from .common import config, MongoClient, get_mongo_client

bearer = HTTPBearer(auto_error=False)


class Claims:
    def __init__(self, token: str):
        try:
            payload = jwt.decode(  # type: ignore
                token,
                config.auth.secret,
                algorithms=[config.auth.algorithm],
                options={"require": ["exp", "iat", "sub"]},
            )
        except jwt.ExpiredSignatureError:
            raise InvalidTokenError()
        except jwt.InvalidTokenError:
            raise InvalidTokenError()

        self.claims = TokenClaims(
            sub=payload["sub"],
            roles=payload.get("roles", []),
            jti=payload.get("jti", ""),
            iat=payload["iat"],
            exp=payload["exp"],
        )

    def has(self, role: Role):
        if not role in self.claims.roles:
            raise ForbiddenError


def get_claims(
    creds: Annotated[HTTPAuthorizationCredentials | None, Depends(bearer)],
) -> Claims:
    if not creds:
        raise HTTPException(status.HTTP_401_UNAUTHORIZED, "Invalid token")
    try:
        return Claims(creds.credentials)
    except InvalidTokenError as exc:
        raise HTTPException(exc.code, exc.message)


def get_api_key(
    mongo_client: MongoClient = Depends(get_mongo_client),
    x_api_key: Optional[str] = Header(default=None, alias="X-API-Key"),
) -> str:
    if not x_api_key:
        raise HTTPException(status.HTTP_401_UNAUTHORIZED, "Unauthorized")

    collection = mongo_client.db.get_collection("api_keys")

    doc = collection.find_one({"_id": x_api_key})

    if not doc:
        raise HTTPException(status.HTTP_401_UNAUTHORIZED, "Unauthorized")

    return x_api_key
