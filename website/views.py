from flask import Blueprint,render_template,jsonify



views = Blueprint('views',__name__)


JOBS = [
    {
        'id': '1',
        'title': 'SOFTWARE ENGINNER',
        'location': 'China,Beijing',
        'salary': 'RMB 50,00,000'
    },
    {
        'id': '2',
        'title': 'PYTHON DEVELOPER',
        'location': 'China,Shanghai',
        'salary': 'RMB 40,00,000'
    },
    {
        'id': '3',
        'title': 'DATA SCIENCTIC',
        'location': 'China,Senzen',
        'salary': 'RMB 45,00,000'
    },
    {
        'id': '4',
        'title': 'PRODUCT MANAGEMENT',
        'location': 'China,Chongqing',

    }
]


@views.route('/')
def home():
    return render_template('base.html',jobs=JOBS)

@views.route("/api/jobs")
def list_jobs():
    return jsonify(JOBS)