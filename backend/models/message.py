from sqlalchemy import Column, Integer, Text, DateTime, String, ForeignKey
from sqlalchemy.sql import func
from database import Base

class ScheduledMessage(Base):
    __tablename__ = "scheduled_messages"

    message_id = Column(Integer, primary_key=True, index=True)

    contact_id = Column(
        Integer,
        ForeignKey("contacts.contact_id", ondelete="CASCADE"),
        nullable=False
    )

    message_content = Column(Text, nullable=False)

    scheduled_time = Column(DateTime, nullable=False)

    status = Column(String(20), default="unsent")

    created_at = Column(DateTime, server_default=func.now())

    sent_at = Column(DateTime)