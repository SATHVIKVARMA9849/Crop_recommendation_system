from flask import Flask, render_template, request, jsonify
import joblib

import pickle

app = Flask(__name__, template_folder='templates')

# Load the Random Forest model
#model = joblib.load('C:\Users\satvik Varma\Downloads\FARMEASYY_NEW\model_NaiveBayes.pkl')
#model = pickle.load(open('model_NaiveBayes.pkl', 'rb'))
with open('model_NaiveBayes.pkl', 'rb') as model_file:
    model = pickle.load(model_file)

# Define a route to render the HTML form
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/service')
def service():
    return render_template('service.html')

@app.route('/blog')
def blog():
    return render_template('blog.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/recommendation_page')
def recommendation_page():
    return render_template('recommendation_page.html')

@app.route('/result_page')
def result_page():
    return render_template('result_page.html')

@app.route('/testimonail')
def testimonail():
    return render_template('testimonail.html')



# Define a route to handle form submission and make a prediction
@app.route('/predict', methods=['POST'])
def predict():
    # Get the input data from the form
    
        param1 = float(request.form['param1'])
        param2 = float(request.form['param2'])
        param3 = float(request.form['param3'])
        param4 = float(request.form['param4'])
        param5 = float(request.form['param5'])
        param6 = float(request.form['param6'])
        param7 = float(request.form['param7'])
    

        # Make a prediction using the loaded model
        prediction = model.predict([[param1, param2, param3, param4, param5, param6, param7]])

        # Return the prediction as JSON
        # return jsonify({'prediction': prediction.tolist()[0]})

        crop_description = get_crop_description(prediction[0])  # Function to get crop description
        return render_template('result_page.html', prediction=prediction[0], crop_description=crop_description)
    
   

def get_crop_description(prediction):
    crop_descriptions = {
        "rice": "rice, (Oryza sativa), edible starchy cereal grain and the grass plant (family Poaceae) by which it is produced. Roughly one-half of the world population, including virtually all of East and Southeast Asia, is wholly dependent upon rice as a staple food, 95 percent of the world's rice crop is eaten by humans.",
        "maize": "Maize, also known as corn, is a cereal grain that has been cultivated by humans for thousands of years. It's one of the most widely grown and consumed crops globally, with a diverse range of uses in food, animal feed, and industrial applications.",
        "chickpea": "Chickpea is the common name for an annual plant, Cicer arietinum, of the Fabaceae (or Leguminosae) family that is widely cultivated for its typically yellow-brown, pea like seeds. The name also is used for these edible seeds, which form in short pods and are popular in various cuisines.",
        "kidneybeans": "Kidney beans are small, reddish-brown beans that are eaten as a vegetable. They are the seeds of a bean plant. Kidney beans are long, very narrow beans that are green in colour and are eaten as a vegetable. They grow on a tall climbing plant and are the cases that contain the seeds of the plant.",
        "pigeonpeas": "Pigeon pea is an erect, short-lived perennial leguminous shrub that usually grows to a height of about 1-2 m, but can reach up to 2-5 m high. It quickly develops a deep (2 m depth) poisonous taproot. The stems are woody at the base, angular and branching. The leaves are alternate and trifoliate.",
        "mothbeans": "Moth bean is a creeping annual herbaceous plant which grows to approximately 40 cm high. Yellow flowers on its hairy and densely packed branches develop into yellow-brown pods, 2 to 3 inches in length The seeds of these pods contain approximately 22 to 24% protein.",
        "mungbean": "The mung bean is a fast-growing erect or semi-erect annual plant with a sturdy taproot. Like many other members of the pea family, mung bean plants add nitrogen to the soil by means of nitrogen-fixing bacteria housed in nodules on their roots.",
        "blackgram": "Black gram (Vigna mungo (L.) Hepper) is an erect, fast-growing annual, herbaceous legume reaching 30-100 cm in height. It has a well-developed taproot and its stems are diffusely branched from the base. Occasionally it has a twining habit and it is generally pubescent.",
        "lentil": "lentil, (Lens culinaris), small annual legume of the pea family (Fabaceae) and its edible seed. Lentils are widely cultivated throughout Europe, Asia, and North Africa but are little grown in the Western Hemisphere. The seeds are used chiefly in soups and stews, and the herbage is used as fodder in some places.",
        "pomegranate": "The pomegranate plant is a large shrub or small tree that has smooth, evergreen leaves and showy orange to red flowers. It has rounded fruit with a dry outer covering (husk) made up of two layers: (1) a hard-outer layer called an epicarp, (2) a soft inner layer called a mesocarp.",
        "banana": "Bananas are long, curved fruits with smooth, yellow, and sometimes slightly green skin. The average length of a banana is about 7 to 9 inches, and it is about 2 to 3 inches in diameter. The skin of the banana is usually yellow when it is ripe, but it can also be green, red, or purple depending on the variety.",
        "mango": "Mango is the national fruit of India which is loved by one and all. It is a very juicy, pulpy and luscious fruit. Ripe mangoes can either be consumed raw or in the form of salad, juice, jams, milkshake or pickles. Mango is a rich source of various vitamins and minerals.",
        "grapes": "A grape is a fruit, botanically a berry, of genus Vitis and family Vitaceae. Grapes grow in clusters of 15 to 300 in different colors (crimson, black, dark blue, yellow, green, orange, pink, and white) and are specifically a nonclimacteric type and deciduous crop.",
        "watermelon": "Watermelon is grown in favorable climates from tropical to temperate regions worldwide for its large edible fruit, which is a berry with a hard rind and no internal divisions, and is botanically called a pepo. The sweet, juicy flesh is usually deep red to pink, with many black seeds, although seedless varieties exist.",
        "muskmelon": "muskmelon, any of several varieties of netted-rind melons in the gourd family (Cucurbitaceae), noted for their musky-scented sweet juicy orange flesh. Muskmelons are among the most-important commercial melons and are commonly eaten fresh.",
        "apple": "The apple is one of the pome (fleshy) fruits. Apples at harvest vary widely in size, shape, colour, and acidity, but most are fairly round and some shade of red or yellow. The thousands of varieties fall into three broad classes: cider, cooking, and dessert varieties.",
        "orange": "Oranges are citrus fruits with fragrant, leathery skin and juicy flesh. The most common types are the sweet (or common) orange, the sour (or Seville) orange, and the mandarin orange. The sweet orange is the most widely grown citrus fruit in the world.",
        "papaya": "The papaya fruit is slightly sweet, with an agreeable musky tang, which is more pronounced in some varieties and in some climates than in others. It is a popular breakfast fruit in many countries and is also used in salads, pies, sherbets, juices, and confections. The unripe fruit can be cooked like squash.",
        "coconut": "Coconut is the fruit of a tropical palm plant. It has a hard shell, edible white flesh and clear liquid, sometimes referred to as water, which is often used as a beverage. Coconut flesh or “meat” is aromatic, chewy in texture and rich in taste.",
        "cotton": "Cotton fibers are natural hollow fibers; they are soft, cool, known as breathable fibers and absorbent. Cotton fibers can hold water 24 to 27 times their own weight. They are strong, dye absorbent and can stand up against abrasion wear and high temperature.",
        "jute": "Jute fabric is a type of natural fabric made from the fibers of the jute plant. The jute plant consists of long, soft, lustrous plant fibers that can be spun into thick, strong yarns. These fibers are often used to make burlap, a coarse, inexpensive material used for bags, sacks and other industrial purposes.",
        "coffee": "Coffee is a beverage prepared from roasted coffee beans. It's also a plant (Coffea) and the name of the drink that is made from this plant. The coffee plant is a bush or tree that can grow up to ten meters (about 32 feet) high, but is usually cut shorter. Coffee plants originally grew in Ethiopia, and now also grow in South America, Central America and Southeast Asia.",
         # Add more descriptions for other crops as needed
        
    }
    return crop_descriptions.get(prediction, "No description available")


# Add a route to handle the fertilizer suggestion page
#@app.route('/fertilizer_suggestion_page')
#def fertilizer_suggestion():
#    return render_template('fertilizersuggestion_page.html')
    
# Add a route to handle the result page
#@app.route('/result_page')
#def result_page():
#    return render_template('resultpage_final.html', prediction="Your Prediction")

if __name__ == '__main__':
    app.run(debug=True,port=8001)