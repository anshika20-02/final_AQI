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
    in1 = int(request.GET.get('in1', 0))
    in2 = int(request.GET.get('in2', 0))
    in3 = int(request.GET.get('in3', 0))

    result = getPredictions(in1,in2,in3)

    return render(request, 'result.html', {'result': result})

