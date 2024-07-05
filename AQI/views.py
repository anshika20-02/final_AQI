from django.shortcuts import render
import pickle
from sklearn.linear_model import LinearRegression


def index(request):
    return render(request, 'index.html')

def getPredictions(in1,in2,in3):

    model = pickle.load(open('IAQ.pkl', 'rb'))
        
    if isinstance(model,LinearRegression):
        input_features = [[in1,in2,in3]]

        prediction=model.predict(input_features)

        return str(prediction[0])
    else:
        return "Error"
    



def prediction(request):
    return render(request, 'prediction.html',{'result': result})




def result(request):
    if request.method == 'GET':
           
        in1 = float(request.GET.get('in1', 0))
        in2 = float(request.GET.get('in2', 0))
        in3 = float(request.GET.get('in3', 0))

    result = getPredictions(in1,in2,in3)
    # Convert 'result' to integer if it's a string representation of a number
    if isinstance(result, str):
        try:
            result = float(result)
        except ValueError:
            return render(request, 'index.html', {'error': 'Invalid result format.'})
 # Determine AQI range and corresponding health implications
    if result <= 50:
        aqi_text = "Good"
        health = "Air quality is considered satisfactory, and air pollution poses little or no risk."
    elif result <= 100:
        aqi_text = "Moderate"
        health = " Air quality is acceptable; however, some pollutants may be a moderate health concern for a very small number of people who are unusually sensitive to air pollution.."
    elif result <= 150:
        aqi_text = "Unhealthy for Sensitive Groups"
        health = "Members of sensitive groups (e.g., children, elderly, individuals with respiratory or heart conditions) may experience health effects. The general public is not likely to be affected."
    elif result <= 200:
        aqi_text = "Unhealthy"
        health = "Everyone may begin to experience health effects; members of sensitive groups may experience more serious health effects."
    elif result <= 300:
        aqi_text = "Very Unhealthy"
        health = "Health alert: everyone may experience more serious health effects."
    else:
        aqi_text = "Hazardous"
        health = "Health warnings of emergency conditions. The entire population is more likely to be affected."

    return render(request, 'result.html', {'aqi': result, 'aqi_text': aqi_text, 'health': health})

    return render( result, 'index.html')