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


    @property
    def state_list(self):
        return [
            self.gpu_1,
            self.gpu_2,
            self.gpu_3,
            self.gpu_4,
            self.gpu_5,
            self.gpu_6,
            self.gpu_7,
        ]

    def __getitem__(self, item: int):
        return self.state_list[item]

    def __str__(self):
        if self.gpu_0 is None:
            return ""
        else:
            return "(%d, %d, %d, %d, %d, %d, %d, %d)" % (self.gpu_0, self.gpu_1, self.gpu_2, self.gpu_3, self.gpu_4, self.gpu_5, self.gpu_6, self.gpu_7)

    def __eq__(self, other):
        for i, j in zip(self.state_list, other.state_list):
            if i != j:
                return False
            return True

    def __ne__(self, other):
        return not self.__eq__(other)

    def save_state_list(self, state_list):
        self.gpu_0 = state_list[0]
        self.gpu_1 = state_list[1]
        self.gpu_2 = state_list[2]
        self.gpu_3 = state_list[3]
        self.gpu_4 = state_list[4]
        self.gpu_5 = state_list[5]
        self.gpu_6 = state_list[6]
        self.gpu_7 = state_list[7]

    @staticmethod
    def latest_state():
        return session.query(GPULog).order_by(desc(GPULog.created_at)).first()



if __name__ == '__main__':
    Base.metadata.create_all(bind=ENGINE)
    log = GPULog()
    log.gpu_0 = False
    log.gpu_1 = False
    log.gpu_2 = False
    log.gpu_3 = False
    log.gpu_4 = False
    log.gpu_5 = False
    log.gpu_6 = False
    log.gpu_7 = False
    session.add(log)
    session.commit()