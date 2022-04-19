
from flask import Flask, request
import pandas as pd

app = Flask(__name__)

@app.route("/create_phrase", methods=['GET','POST'])
def create_phrase():
    data = request.json
    response = ''
    if data is not None:
        inp = dict(data)
        name_out = pig_latin(inp['fullName'])
        county, pop =zip_code_pop(inp['zipcode'])
        response = f"{name_out}'s zip code is in {county} County and has a population of {pop}."
    else: pass
    return response

def pig_latin(name):
    #convert to lowercase
    name = name.lower() 
    vowels = 'aeiou'
    output = []
    #loop through name using name.split()
    for text in name.split():
        #checking if name has digits
        if sum([ch.isdigit() for ch in text]):
            output.append(text.capitalize())
        #first letter vowel add -YAY
        elif text[0] in vowels:
            text += 'yay'
            output.append(text.capitalize())
        else:
            res = ''
            for i in text:
                if i not in vowels:
                    res += i
                else: 
                    break
            out = text[len(res):]+res+'ay'
            output.append(out.capitalize())
    return ' '.join(output)

def zip_code_pop(code):
    #reading csv using pandas
    df = pd.read_csv('uszips.csv')
    county = df[df.zip == int(code)].county_name.item()
    pop = int(df[df.zip == int(code)].population.item())
    return county, pop

if __name__ == '__main__':
    app.run(debug=True)