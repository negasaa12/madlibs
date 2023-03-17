from flask import Flask, render_template, request, g
from flask_debugtoolbar import DebugToolbarExtension

from stories import Story, story


# from stories import story

app = Flask(__name__)
app.config['SECRET_KEY'] = "chickensarecool1"
debug = DebugToolbarExtension(app)

@app.route('/')
def questionaire():
    
  
 

   
    story_list = story.prompts
    # place = request.args.get("place")
    # print(f"place : {place}")
    # g.place = place 
    # noun = request.args["noun"]
    # verb = request.args["verb"]
    # adjective = request.args["adjective"]
    # plural_noun = request.args["plural_noun"]
    return  render_template('questions.html', story_list=story_list)
    

@app.route('/story')
def your_story():
    # print(g.place)
    place = request.args.get("place")
    noun = request.args["noun"]
    verb = request.args["verb"]
    adjective = request.args["adjective"]
    plural_noun = request.args["plural_noun"]

    first_story = story.generate({'place': place, 'noun': noun, 'verb': verb, 'adjective': adjective, 'plural_noun' : plural_noun})
   
    return render_template('stories.html', place=place, noun=noun, verb=verb, adjective=adjective, plural_noun=plural_noun, first_story=first_story)