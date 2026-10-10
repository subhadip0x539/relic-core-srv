from internal.port.feature import FeatureService
from internal.port.apikey import ApiKeyRepository
from internal.port.flag import FlagRepository
from internal.dto.feature import GetFeaturesResponseBody, GetFeaturesResponseBodyItem
from internal.domain.common import Filter, FilterOperator
from internal.lib.fc import FC


class FeatureServiceImpl(FeatureService):
    def __init__(self, flag_repo: FlagRepository, api_key_repo: ApiKeyRepository):
        self.flag_repo = flag_repo
        self.api_key_repo = api_key_repo

    def all(self, api_key: str) -> GetFeaturesResponseBody:
        ak = self.api_key_repo.get(api_key)

        fc = FC(
            [
                Filter(
                    field="service_id",
                    operator=FilterOperator.EQ,
                    value=[ak.service_id],
                )
            ]
        )

        flags = self.flag_repo.all(fc)

        return [
            GetFeaturesResponseBodyItem(
                id=f.id,
                name=f.name,
                description=f.description,
                type=f.type,
                value=f.value,
                enabled=f.enabled,
            )
            for f in flags
        ]
