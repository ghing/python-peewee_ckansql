from peewee import *
from peewee_ckansql import CkanDatabase

db = CkanDatabase('http://ods-service-test.herokuapp.com/api/action/datastore_search_sql')

class BaseModel(Model):
    class Meta:
        database = db

class BudgetRecommendation(BaseModel):
    fund_type = CharField(db_column='FUND TYPE', primary_key=True)
    fund_code = CharField(db_column='FUND CODE')
    fund_description = CharField(db_column='FUND DESCRIPTION')
    department_number = CharField(db_column='DEPARTMENT NUMBER')
    department_description = CharField(db_column='DEPARTMENT DESCRIPTION')
    appropriation_authority = CharField(db_column='APPROPRIATION AUTHORITY')
    appropriation_authority_description = CharField(db_column='APPROPRIATION AUTHORITY DESCRIPTION')
    appropriation_account = CharField(db_column='APPROPRIATION ACCOUNT')
    appropriation_account_description = CharField(db_column= 'APPROPRIATION ACCOUNT DESCRIPTION')
    appropriation_2012 = CharField(db_column='2012 APPROPRATION')
    appropriation_2012_revised = CharField(db_column='2012 REVISED APPROPRIATION')
    recommendation_2013 = CharField(db_column='2013 RECOMMENDATION')

    class Meta:
        db_table = 'appropriations'

def main():
    recs = BudgetRecommendation.select().limit(2)
    for rec in recs:
        print rec.department_description, rec.fund_description, rec.appropriation_2012, rec.recommendation_2013

if __name__ == "__main__":
    main()
