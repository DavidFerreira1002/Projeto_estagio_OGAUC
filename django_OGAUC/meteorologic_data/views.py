from django.shortcuts import render,redirect
import json
from django.views.decorators.csrf import csrf_protect,requires_csrf_token
from .models import Meteo_24h

# Create your views here.
@csrf_protect
def meteorologic(request):
    tab_title = "Meteorologic Data"

    class Temperatura:
        def __init__(self,timestamp,temp_avg,temp_max,temp_min):
                super().__init__()
                self.timestamp = timestamp
                self.temp_avg = temp_avg
                self.temp_max = temp_max
                self.temp_min = temp_min

    class Humidade:
        def __init__(self,timestamp,hrel_avg):
                super().__init__()
                self.timestamp = timestamp
                self.hrel_avg = hrel_avg    

    class Pressao:
        def __init__(self,timestamp,pressao_avg,pnmm_avg):
                super().__init__()
                self.timestamp = timestamp
                self.pressao_avg = pressao_avg
                self.pnmm_avg = pnmm_avg

    class Precip_tot:
        def __init__(self,timestamp,precip_tot):
                super().__init__()
                self.timestamp = timestamp
                self.precip_tot = precip_tot

    #Querying database for data
    data = Meteo_24h.objects.order_by('-timestamp')[0:89]

    meteo_timestamp_array = []
    meteo_temp_avg_array = []
    meteo_temp_max_array = []
    meteo_temp_min_array = []
    meteo_hrel_avg_array = []
    meteo_pressao_avg_array = []
    meteo_pnmm_avg_array = []
    meteo_precip_tot_array = []
    for line in data:
        meteo_timestamp_array.insert(0,line.timestamp[0:10])
        meteo_temp_avg_array.insert(0,line.temp_avg)
        meteo_temp_max_array.insert(0,line.temp_max)
        meteo_temp_min_array.insert(0,line.temp_min)
        meteo_hrel_avg_array.insert(0,line.hrel_avg)
        meteo_pressao_avg_array.insert(0,line.pressao_avg)
        meteo_pnmm_avg_array.insert(0,line.pnmm_avg)
        meteo_precip_tot_array.insert(0,line.precip_tot)

    #Data for the graph
    data_graph_temperatura = Temperatura(timestamp=meteo_timestamp_array,temp_avg=meteo_temp_avg_array,temp_max=meteo_temp_max_array,temp_min=meteo_temp_min_array)
    data_graph_humidade = Humidade(timestamp=meteo_timestamp_array,hrel_avg=meteo_hrel_avg_array)
    data_graph_pressao = Pressao(timestamp=meteo_timestamp_array,pressao_avg=meteo_pressao_avg_array,pnmm_avg=meteo_pnmm_avg_array)
    data_graph_precip_tot = Precip_tot(timestamp=meteo_timestamp_array,precip_tot=meteo_precip_tot_array)

   

    return render(request,'Meteorologic/meteorologicTP.html',{"tab_title":tab_title,"temperatura":data_graph_temperatura,"humidade":data_graph_humidade,"pressao":data_graph_pressao,"precip_tot":data_graph_precip_tot})

@csrf_protect
def insert24h(request):
    if request.method == 'POST':

        data24h_list = json.loads(request.body)
        #print(data24h_list)
        for line in data24h_list:
            timestamp = line['timestamp']
            temp_avg = line['temp_avg']
            temp_max = line['temp_max']
            temp_min = line['temp_min']
            hrel_avg = line['hrel_avg']
            pressao_avg = line['pressao_avg']
            pnmm_avg = line['pnmm_avg']
            precip_tot = line['precip_tot']

            data_for_db = Meteo_24h(timestamp= timestamp,temp_avg= temp_avg,temp_max= temp_max,temp_min=temp_min,hrel_avg=hrel_avg,pressao_avg=pressao_avg,pnmm_avg=pnmm_avg,precip_tot=precip_tot)

            data_for_db.save()

    return redirect('/')           