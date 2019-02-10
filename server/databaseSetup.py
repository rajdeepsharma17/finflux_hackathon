from sqlalchemy import Column, ForeignKey, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

Base = declarative_base()



class Members(Base):
    __tablename__ = 'members_detail'

    id = Column(Integer, primary_key=True)
    member_id = Column(Integer)
    loan_amnt = Column(Integer)
    funded_amnt_inv = Column(Integer)
    term = Column(String)
    int_rate = Column(Float, nullable=False)
    installment = Column(Float)
    grade = Column(String)
    emp_title = Column(String)
    emp_length = Column(String)
    home_ownership = Column(String)
    annual_inc = Column(Integer)
    verification_status = Column(String)
    issue_d = Column(String)
    loan_status = Column(String)
    desc = Column(String)
    purpose = Column(String)
    title = Column(String)
    addr_state = Column(String)
    last_pymnt_d = Column(String)
    last_pymnt_amnt = Column(String)


    @property
    def serialize(self):
        """Return object data in easily serializeable format"""
        return {
            'member_id': self.member_id,
            'loan_amnt': self.loan_amnt,
            'funded_amnt_inv': self.funded_amnt_inv,
            'term': self.term,
            'int_rate': self.int_rate,
            'installment': self.installment,
            'grade': self.grade,
            'emp_title': self.emp_title,
            'emp_length': self.emp_length,
            'home_ownership': self.home_ownership,
            'annual_inc': self.annual_inc,
            'verification_status': self.verification_status,
            'issue_d': self.issue_d,
            'loan_status': self.loan_status,
            'desc':  self.desc,
            'purpose': self.purpose,
            'title': self.title,
            'addr_state': self.addr_state,
            'last_pymnt_d': self.last_pymnt_d,
            'last_pymnt_amnt': self.last_pymnt_amnt
            }


engine = create_engine('sqlite:///finflux.db')


Base.metadata.create_all(engine)
