from flask import Flask, request, render_template, url_for, redirect, flash
from forms import RegistrationForm
from Game import Game, DifficultyEnum
from werkzeug.utils import secure_filename
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = 'cd291fd59e221b9a3a13c13b3b5dbc9e'
UPLOAD_FOLDER = '/Documents/cs2340/SpaceTrader/images_regions'
ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
skills = None

# def allowed_file(filename):
#     return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/', methods=['GET', 'POST'])
# def upload_file():
#     if request.method == 'POST':
#         # check if the post request has the file part
#         if 'file' not in request.files:
#             flash('No file part')
#             return redirect(request.url)
#         file = request.files['file']
#         # if user does not select file, browser also
#         # submit a empty part without filename
#         if file.filename == '':
#             flash('No selected file')
#             return redirect(request.url)
#         if file and allowed_file(file.filename):
#             filename = secure_filename(file.filename)
#             file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
#             return redirect(url_for('uploaded_file', filename=filename))
@app.route('/welcome')
def welcome():
    return render_template('welcome.html')


@app.route('/configuration', methods=['GET', 'POST'])
def configuration():
    form = RegistrationForm()
    if form.validate_on_submit():
        value = form.selectDifficulty.data
        pilotSkill = form.allocatePilot.data
        engineerSkill = form.allocateEngineer.data
        merchantSkill = form.allocateMerchant.data
        fighterSkill = form.allocateFighter.data
        name = form.username.data
        sum = int(pilotSkill) + int(engineerSkill) + int(merchantSkill) + int(fighterSkill)
        if (value == 'easy' and sum <= 16) or (value == 'medium' and sum <= 12) or (value == 'hard' and sum <= 8):
            return redirect(url_for('game', difficulty=value, pilotSkill=pilotSkill, engineerSkill=engineerSkill,
                                    merchantSkill=merchantSkill, fighterSkill=fighterSkill, name=name))
    else:
        return render_template('configuration.html', form=form)


@app.route('/game')
def game():
    if Game.get_instance() is None:
        difficulty_string = request.args.get('difficulty')
        difficulty = None
        if difficulty_string == 'easy':
            difficulty = DifficultyEnum.EASY
        elif difficulty_string == 'medium':
            difficulty = DifficultyEnum.MEDIUM
        else:
            difficulty = DifficultyEnum.HARD
        skills = (int(request.args.get('pilotSkill')), int(request.args.get('engineerSkill')), int(request.args.get('merchantSkill')), int(request.args.get('fighterSkill')))
        Game(difficulty, request.args.get('name'), skills)
        game2 = Game.get_instance()
    return render_template('game.html', game=Game.get_instance(), len = len(game2.universe.regions))




if __name__ == '__main__':
    app.config['ENV'] = 'development'
    app.config['DEBUG'] = True
    app.config['TESTING'] = True
    app.run(debug=True)
