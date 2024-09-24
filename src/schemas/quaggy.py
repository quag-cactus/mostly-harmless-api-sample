from pydantic import BaseModel, Field


class GetScheduleNowResponse(BaseModel):
    request_id: str = Field(examples=["unique-uuid-request-id"])
    status: str = Field(examples=["quaggy-current-status"])
