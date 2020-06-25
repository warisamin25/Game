from flask import Flask
from flask import request
from flask import render_template

app = Flask(__name__)

@app.route('/')
def Start():
    return render_template('Welcome.html')
    
@app.route('/user_inputs',  methods=[ 'GET', 'POST'])
def inputs():
    results = {}
    if request.method == 'POST':
        # import pdb;pdb.set_trace()
        mood = request.form['input1']
        games = request.form['input2']
        set_mood = mood
        set_games = games
        from Games import main
        games_result, mood = main(set_mood, set_games)
        print(games_result, mood)
        return render_template('output.html', methods = ['POST'])
    return render_template('User_inputs.html', results=results)
 
    
if __name__ == "__main__":
    app.run(debug=True)
    
    
