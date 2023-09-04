from flask import Flask, render_template, jsonify

app = Flask(__name__)

JOBS = [
{
  'id' : 1,
  'title': 'Data Analysis',
  'location': 'New Jersey',
  'Salary': '100,000'
},
{
  'id':2,
  'title': 'Computer Science',
  'location': 'New York',
  'Salary': '120,000'
},

{
  'id':3,
  'title': 'Technical support',
  'location': 'Georgia',
  'Salary': '90,000'
},

{
  'id':4,
  'title': 'back-end Engineering',
  'location': 'Remote',
  'Salary': '130,000'
}
]
@app.route("/")
def hello_world():
  return render_template('home.html', jobs=JOBS,company_name='welvens')

@app.route("/api/jobs")
def list_jobs():
  return jsonify(JOBS)

if __name__ =='__main__':
  app.run(host='0.0.0.0', debug=True)