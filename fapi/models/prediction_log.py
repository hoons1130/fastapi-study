from datetime import date, datetime

from sqlalchemy import DateTime, Float, Integer, func

from sqlalchemy.orm import Mapped, mapped_column

from database import Base

class PredictionLog(Base):
    __tablename__ = "prediction_logs"

    id: Mapped[int]= mapped_column(
        Integer,
        primary_key=True,
        autoincrement=True
    )

    prediction: Mapped[int] = mapped_column(
        Integer,
        nullable=False,
    )

    probability: Mapped[float] = mapped_column(
        Float,
        nullable=False
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime,
        nullable=False,
        server_default=func.now()
    )