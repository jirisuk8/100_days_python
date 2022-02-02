from flask import Flask, render_template
from datetime import date
import random
import requests

app = Flask(__name__)


@app.route('/')
def home():
    random_number = random.randint(1, 10)
    current_year = date.today().year
    return render_template("index.html", num=random_number, year=current_year)


@app.route('/guess/<name>')
def get_name(name):
    parameters = {
        'name': name,
    }
    with requests.get(url=f"https://api.genderize.io/", params=parameters) as response:
        response.raise_for_status()
        gender_data = response.json()
        name_gender = gender_data["gender"]

    with requests.get(url=f"https://api.agify.io/", params=parameters) as response:
        response.raise_for_status()
        age_data = response.json()
        name_age = age_data["age"]

    with requests.get(url=f"https://api.nationalize.io/", params=parameters) as response:
        response.raise_for_status()
        nation_data = response.json()
        nations_probability = nation_data["country"]
        us_probability = nations_probability[0]["probability"]
        au_probability = nations_probability[1]["probability"]
        nz_probability = nations_probability[2]["probability"]

    return render_template("name_data.html", name=name.capitalize(), gender=name_gender, age=name_age,
                           us=us_probability, au=au_probability, nz=nz_probability)


@app.route('/blog/<num>')
def get_blog(num):
    blog_url = 'https://api.npoint.io/c790b4d5cab58020d391'
    response = requests.get(blog_url)
    response.raise_for_status()
    all_posts = response.json()
    return render_template("blog.html", posts=all_posts)


if __name__ == "__main__":
    app.run(debug=True)


