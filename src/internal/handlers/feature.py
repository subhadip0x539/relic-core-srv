from internal.port.feature import FeatureService
from internal.dto.feature import GetFeaturesResponse


class FeatureHandler:
    svc: FeatureService

    def __init__(self, svc: FeatureService):
        self.svc = svc

    def all(self, api_key: str) -> GetFeaturesResponse:
        result = self.svc.all(api_key)

        response = GetFeaturesResponse(body=result)

        return response
