from flaskblog import app
from flask import request,render_template
from flaskblog.forms import RegistrationForm
from flaskblog.model import FoodDB
from flaskblog.entity import Food

@app.route("/")
def hello():
    return "YOOOO"

@app.route('/searchfood', methods=['GET', 'POST'])
def displaySearchFood():
    food_item_list = []
    form = RegistrationForm(request.form)
    if request.method == 'POST' and form.validate():
        foodToBeSearched = form.foodname.data
        # convert user entered data into lowercase
        editedfoodToBeSearched = foodToBeSearched.lower()
        # find in FoodDB
        results = FoodDB.query.filter(FoodDB.food_name.contains(editedfoodToBeSearched)).all()

        if results is not None:
            for result in results:
                splitted_result = result.food_name.split(", ")
                # only display the result if first word of the food name contains the searched food name
                if editedfoodToBeSearched in splitted_result[0]:
                    # create a food object from entity.py
                    food_item = Food(result.food_id,result.food_name,round(result.food_calories,2),round(result.food_protein,2),round(result.food_carb,2),round(result.food_fat,2),round(result.food_fibres,2),round(result.food_saturatedfat,2),round(result.food_sodium,2))
                    food_item_list.append(food_item)
    return render_template('searchFood.html', form=form,foodList=food_item_list)

