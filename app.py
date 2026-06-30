from flask import Flask,request,render_template 
import requests

app = Flask(__name__) 

@app.route("/", methods=["GET","POST"])
def home():
  
    if request.method=="POST":

        city = request.form.get("city")
        api_key = "YOUR_API_KEY "
        url = f"http://api.weatherapi.com/v1/current.json?key={api_key}&q={city}"
        response = requests.get(url)
        if city:
            data = response.json()

        # print(f"City:{data["location"]["name"]}\nTemprature:{data["current"]["temp_c"]}°C|{data["current"]["condition"]["text"]}\nHumidity:{data["current"]["humidity"]}")

        return render_template("index.html",city=data["location"]["name"],temperature=data["current"]["temp_c"],
                            condition=data["current"]["condition"]["text"],
                            humidity=data["current"]["humidity"]) 
    return render_template("index.html")

if __name__ == '__main__':
    app.run(debug=True)
