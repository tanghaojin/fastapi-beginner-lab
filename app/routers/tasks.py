from fastapi import APIRouter, BackgroundTasks, Depends, status

from .. import background, schemas
from ..auth import get_current_user

router = APIRouter(prefix="/tasks", tags=["tasks"])


@router.post(
    "/notifications",
    status_code=status.HTTP_202_ACCEPTED,
    summary="提交通知任务",
)
def queue_notification(
    notification: schemas.NotificationCreate,
    background_tasks: BackgroundTasks,
    current_user=Depends(get_current_user),
):
    background_tasks.add_task(background.log_notification, notification.message)
    return {"message": "notification queued"}
