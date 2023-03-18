from flask import Flask, render_template, request, g
from flask_debugtoolbar import DebugToolbarExtension

from stories import Story, story, story2, story3, story_log


# from stories import story

app = Flask(__name__)
app.config['SECRET_KEY'] = "chickensarecool1"
debug = DebugToolbarExtension(app)

@app.route('/question')
def questionaire():
    

    selected_story = request.args.get('story_template')
    print(f"Selected story: {selected_story}")
    story_obj = story_log[selected_story]
    prompts = story_obj.prompts
    return render_template('questions.html', prompts=prompts, story=selected_story)

    
@app.route('/')
def pick_story():

    title1 = story.__str__()
    title2 = story2.__str__()
    title3 = story3.__str__()
    return render_template('home.html', title1=title1, title2=title2, title3=title3, story_log=story_log)




@app.route('/story')
def your_story():
    # print(g.place)
    place = request.args.get("place")
    noun = request.args["noun"]
    verb = request.args["verb"]
    adjective = request.args["adjective"]
    plural_noun = request.args["plural_noun"]

    first_story = story.generate({'place': place, 'noun': noun, 'verb': verb, 'adjective': adjective, 'plural_noun' : plural_noun})
    second_story = story2.generate({'place': place,'noun': noun, 'verb': verb, 'adjective': adjective})
   
    return render_template('stories.html', place=place, noun=noun, verb=verb, adjective=adjective, plural_noun=plural_noun, first_story=first_story)