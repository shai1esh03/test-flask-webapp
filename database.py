from sqlalchemy import create_engine, text, bindparam
engine = create_engine()

def load_jobs_from_db():
    with engine.connect() as conn:
        result = conn.execute(text("select * from jobs"))
        jobs = []
        for row in result.all():
            jobs.append(row._mapping)
        return jobs

def load_job_from_db(id):
    with engine.connect() as conn:
        result = conn.execute(text("select * from jobs where id = :val").bindparams(bindparam("val",id)))
        rows = result.all()
        if len(rows) == 0:
            return None
        else:
            return rows[0]



