from flask import Flask, render_template

app = Flask(__name__)

JOBS = [
  {
    'id': 1,
    'title': 'Ezio Auditore da Firenze',
    'location': 'Florence, Italy',
    'salary': 'Rs. 10,00,000'
  },
  {
    'id': 2,
    'title': 'Altair Ibn Lahad',
    'location': 'Jerusalem, Palestine',
    'salary': 'Rs. 15,00,000'
  },
  {
    'id': 3,
    'title': 'Connor Kenway',
    'location': 'USA',
    'salary': 'Rs. 12,00,000'
  },
  {
    'id': 4,
    'title': 'Eivor',
    'location': 'Norway',
    'salary': '$120,000'
  }
]

@app.route('/')
def run():
  return render_template('home.html', jobs = JOBS, 
                        company_name = 'Abstergo')


if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True)
