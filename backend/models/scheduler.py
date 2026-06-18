from sqlalchemy import Column, Integer, String, Text, DateTime, ForeignKey
from sqlalchemy.sql import func
from database import Base

class NotificationLog(Base):
    __tablename__ = "notification_logs"

    notification_id = Column(Integer, primary_key=True, index=True)
    message_id = Column(
        Integer,
        ForeignKey("scheduled_messages.message_id", ondelete="CASCADE"),
        nullable=False
    )
    notification_text = Column(Text)
    notification_time = Column(
        DateTime,
        server_default=func.now()
    )

class SchedulerLog(Base):
    __tablename__ = "scheduler_logs"
    log_id = Column(Integer, primary_key=True, index=True)
    action = Column(String)
    status = Column(String)
    log_time = Column(
        DateTime,
        server_default=func.now()
    )
    details = Column(Text)