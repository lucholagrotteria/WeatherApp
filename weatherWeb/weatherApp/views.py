from django.shortcuts import render
#Importamos la librería json para que devuelva en ese formato la info
import json
import urllib.request

# Create your views here.

def index(request):
    
    #Configuramos para obtener la data introducida en el form
    #Usamos el método POST para cuando mandamos el form y nos devuelva el valor pedido 
    if request.method == "POST":
        
        city = request.POST["city"]
        #Variable res por request de info a la api
        
        res = urllib.request.urlopen("http://api.openweathermap.org/data/2.5/weather?q="+city+"&appid=dbda734a0ec7d3ee86d2af04db03f9fe").read()
        #A traves de esta variable obtenemos la data después de mandar la solicitud a la URL
        
        json_data = json.loads(res)
        #Ahora tenemos info de lo que pedimos, almacenada en la variable json_data
        
        #Creamos un diccionario para que sea mas fácil ingresar a la data
        data = {
            "country_code":str(json_data["sys"]["country"]),
            "coordinate":str(json_data["coord"]["lon"]) + " " +
            str(json_data["coord"]["lat"]),
            "temp":str(json_data["main"]["temp"]) + "k",
            "pressure":str(json_data["main"]["pressure"]),
            "humidity":str(json_data["main"]["humidity"]), 
        }
    
    else:
        city = ""
        data = ""
    return render(request, "index.html", {"city":city,"data":data})