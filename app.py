from flask import Flask, request, render_template, url_for, redirect
from forms import RegistrationForm
from game import Game, DifficultyEnum

app = Flask(__name__)
app.config['SECRET_KEY'] = 'cd291fd59e221b9a3a13c13b3b5dbc9e'
UPLOAD_FOLDER = '/Documents/cs2340/SpaceTrader/images_regions'
ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Contributors: Leyan Pan, Jintong Jiang, Hanzhong Kang, Wanli Qian

@app.route('/', methods=['GET', 'POST'])
@app.route('/welcome')
def welcome():
    return render_template('welcome.html')


@app.route('/configuration', methods=['GET', 'POST'])
def configuration():
    form = RegistrationForm()
    if form.validate_on_submit():
        value = form.selectDifficulty.data
        pilot_skill = form.allocatePilot.data
        engineer_skill = form.allocateEngineer.data
        merchant_skill = form.allocateMerchant.data
        fighter_skill = form.allocateFighter.data
        name = form.username.data
        sum_value = int(pilot_skill) + int(engineer_skill) +\
                    int(merchant_skill) + int(fighter_skill)
        Game.remove_instance()
        if (value == 'easy' and sum_value <= 16):
            return redirect(url_for('game', difficulty=value, pilotSkill=pilot_skill,\
                                    engineerSkill=engineer_skill, merchantSkill=merchant_skill,\
                                    fighterSkill=fighter_skill, name=name))
        if (value == 'medium' and sum_value <= 12):
            return redirect(url_for('game', difficulty=value, pilotSkill=pilot_skill,\
                                    engineerSkill=engineer_skill, merchantSkill=merchant_skill,\
                                    fighterSkill=fighter_skill, name=name))
        if (value == 'hard' and sum_value <= 8):
            return redirect(url_for('game', difficulty=value, pilotSkill=pilot_skill,\
                                    engineerSkill=engineer_skill, merchantSkill=merchant_skill,\
                                    fighterSkill=fighter_skill, name=name))
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
        skills = (int(request.args.get('pilotSkill')), int(request.args.get('engineerSkill')),\
                  int(request.args.get('merchantSkill')), int(request.args.get('fighterSkill')))
        Game(difficulty, request.args.get('name'), skills)
    else:
        game_instance = Game.get_instance()
        game_instance.travel_to_region_string(request.args.get('travel'))
    return render_template('game.html', game=Game.get_instance(),\
                           len=len(Game.get_instance().universe.regions))



@app.route('/Region')
def region():
    return render_template('region.html')



if __name__ == '__main__':
    app.config['ENV'] = 'development'
    app.config['DEBUG'] = True
    app.config['TESTING'] = True
    app.run(debug=True)
