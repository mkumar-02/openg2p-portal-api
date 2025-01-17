from typing import List, Optional

from openg2p_fastapi_common.models import BaseORMModel
from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

# from .cycle_membership_orm import CycleMembershipORM
# from .program_orm import ProgramORM


class CycleORM(BaseORMModel):
    __tablename__ = "g2p_cycle"

    id: Mapped[int] = mapped_column(primary_key=True)
    program_id: Mapped[int] = mapped_column(ForeignKey("g2p_program.id"))
    program: Mapped[Optional[List["ProgramORM"]]] = relationship(
        back_populates="cycles"
    )
    cycle_memberships: Mapped[Optional[List["CycleMembershipORM"]]] = relationship(
        back_populates="cycles"
    )
    name: Mapped[str] = mapped_column()
