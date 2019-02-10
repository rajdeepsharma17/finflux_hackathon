#!/usr/bin/python
# # -*- coding: utf-8 -*-
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from databaseSetup import Base, Members
import json

  

engine = create_engine('sqlite:///finflux.db')
# Bind the engine to the metadata of the Base class so that the
# declaratives can be accessed through a DBSession instance
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
# A DBSession() instance establishes all conversations with the database
# and represents a "staging zone" for all the objects loaded into the
# database session object. Any change made against the objects in the
# session won't be persisted into the database until you call
# session.commit(). If you're not happy about the changes, you can
# revert all of them back to the last commit by calling
# session.rollback()
session = DBSession()



# ADD dummy Todos
def getData():
    with open('loan_part_0009b606f.json') as json_file:  
        data = json.load(json_file)
        for item in data:
            member = Members(member_id =  item['member_id'],
                            loan_amnt = item['loan_amnt'],
                            funded_amnt_inv = item['funded_amnt_inv'],
                            term = item['term'],
                            int_rate = item['int_rate'],
                            installment = item['installment'],
                            grade = item['grade'],
                            emp_title = item['emp_title'],
                            emp_length = item['emp_length'],
                            home_ownership = item['home_ownership'],
                            annual_inc = item['annual_inc'],
                            verification_status = item['verification_status'],
                            issue_d = item['issue_d'],
                            loan_status = item['loan_status'],
                            desc =  item['desc'],
                            purpose = item['purpose'],
                            title = item['title'],
                            addr_state = item['addr_state'],
                            last_pymnt_d = item['last_pymnt_d'],
                            last_pymnt_amnt = item['last_pymnt_amnt']
                )
            session.add(member)
            session.commit()


if __name__ == '__main__':
    getData()