"""
Run this once to create .sqlite3 file
"""
from config.datapath import DATABASE
from sqlalchemy import *
from sqlalchemy.orm import *
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

ENGINE = create_engine(
    DATABASE,
    encoding="utf-8",
    echo=False
)

session = scoped_session(
    sessionmaker(
        autocommit=False,
        autoflush=False,
        bind=ENGINE
    )
)

Base = declarative_base()
Base.query = session.query_property()


class GPULog(Base):
    __tablename__ = "gpu_log"
    id = Column("id", Integer, primary_key=True)
    gpu_0 = Column("gpu_0", Boolean, nullable=False, comment="GPU0's state. True if used.")
    gpu_1 = Column("gpu_1", Boolean, nullable=False, comment="GPU1's state. True if used.")
    gpu_2 = Column("gpu_2", Boolean, nullable=False, comment="GPU2's state. True if used.")
    gpu_3 = Column("gpu_3", Boolean, nullable=False, comment="GPU3's state. True if used.")
    gpu_4 = Column("gpu_4", Boolean, nullable=False, comment="GPU4's state. True if used.")
    gpu_5 = Column("gpu_5", Boolean, nullable=False, comment="GPU5's state. True if used.")
    gpu_6 = Column("gpu_6", Boolean, nullable=False, comment="GPU6's state. True if used.")
    gpu_7 = Column("gpu_7", Boolean, nullable=False, comment="GPU7's state. True if used.")
    created_at = Column(DateTime, nullable=False, default=datetime.utcnow)

    state_list = [gpu_0, gpu_1, gpu_2, gpu_3, gpu_4, gpu_5, gpu_6, gpu_7]

    def __getitem__(self, item: int):
        return self.state_list[item]

    def __eq__(self, other):
        for i, j in zip(self.state_list, other.state_list):
            if i != j:
                return False
            return True

    def __ne__(self, other):
        return not self.__eq__(other)

    def save_state_list(self, state_list):
        for idx, gpu in enumerate(self.state_list):
            self.state_list[idx] = state_list[idx]

    @staticmethod
    def latest_state():
        return session.query(GPULog.gpu0,
                             GPULog.gpu1,
                             GPULog.gpu2,
                             GPULog.gpu3,
                             GPULog.gpu4,
                             GPULog.gpu5,
                             GPULog.gpu6,
                             GPULog.gpu7).order_by(desc(GPULog.created_at)).first()



if __name__ == '__main__':
    Base.metadata.create_all(bind=ENGINE)
