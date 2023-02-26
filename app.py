import json
from flask import Flask, render_template, jsonify
from database import load_jobs_from_db, load_job_from_db

# flask is module and FLask is Class

app = Flask(__name__)  
# app is an object of Class Flask. Variable __name__ 
          
                              
@app.route("/")  
def hello_world():
    jobs = load_jobs_from_db()
    return render_template('home.html', jobs=jobs, company_name='Shailesh')

@app.route("/api/jobs")
def list_jobs():
    jobs = load_jobs_from_db()
    return json.dumps([dict(j) for j in jobs])

@app.route("/job/<id>")
def show_job(id):
    job = load_job_from_db(id)
    return jsonify(job)
    
if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)