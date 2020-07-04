from flask import Flask, request, jsonify, abort, render_template
import requests

app = Flask(__name__)

app.config['JSON_SORT_KEYS'] = False

distribution = [{'type' : 'chuck-norris-joke' , 'count' : 0}, 
                {'type' : 'kanye-quote' , 'count' : 0}, 
                {'type' : 'name-sum' , 'count' : 0}, 
                {'type' : 'taco-recipe' , 'count' : 0}, 
                {'type' : 'surprising-dog' , 'count' : 0}]

#errors
@app.errorhandler(404)
def error404(error):
    return 'No Surprise For You!', 404

@app.errorhandler(400)
def error400(error):
    return 'name or birth year are missing!', 400


#routes
@app.route('/api/surprise')
def index():
    name = request.args['name'] 
    birth_year = int(request.args['birth_year']) 

    if birth_year >= 2015: 
        type = 'surprising-dog'
        inc(type)
        res = surprisingDog()
        return render_template("dogPic.html", url= res)
    if birth_year >= 2010:
        type = 'taco-recipe'
        inc(type)
        res = tacoRecipe()
        return jsonify({'type' : type , 'result' : res})
    if birth_year <= 2000:
        type = 'chuck-norris-joke'
        inc(type)
        res = chuckNorrisJoke()
        return jsonify({'type' : type , 'result' : res})
    else:
        if name[0] != 'A' and name[0] != 'Z':
            type = 'kanye-quote'
            inc(type)
            res = kenyeQuate()
            return jsonify({'type' : type , 'result' : res})
        else :
            if name[0] != 'Z':
                type = 'name-sum'
                inc(type)
                res = nameSum(name)
                return jsonify({'type' : type , 'result' : res})
            else:
                abort(404)

@app.route('/api/stats')
def getStats():
    return jsonify({'requests' : countRequests() , 'distribution' : distribution})

#help functions
def nameSum(name):
    sum = 0
    name = name.lower() #to lower case
    for c in name:
        num  = ord(c) - 96 # character to order number
        sum += num
    return sum

def chuckNorrisJoke():
    r = requests.get("https://api.chucknorris.io/jokes/random")
    json_obj = r.json()
    joke= json_obj['value']
    return joke

def kenyeQuate():
    r = requests.get("https://api.kanye.rest")
    json_obj = r.json()
    quote = json_obj['quote']
    return quote

def tacoRecipe():
    r = requests.get("http://taco-randomizer.herokuapp.com/random/?full-taco=true")
    json_obj = r.json()
    recipe = json_obj['recipe']
    return recipe

def surprisingDog():
    r = requests.get("https://dog.ceo/api/breeds/image/random")
    json_obj = r.json()
    image = json_obj['message']
    return image

#returns the number of all requests
def countRequests():
    sum = 0
    for d in distribution:
        sum += d['count']
    return sum

#increment the number of times type requested
def inc(type):
   for d in distribution:
       if d['type'] == type :
           d['count'] += 1
    



if __name__ =="__main__":
    app.run(debug=True)







