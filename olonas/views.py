from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Olona, Vady
from .querydb import query_taranaka, test_lahyvavy, query_dada, query_neny
from .forms import OlonaForm, OlonaRawForm
from .models import Fivondronana, Firaisana 


def get_taranaka(id_dadabe, id_bebe):    
    taranaka = query_taranaka(id_dadabe, id_bebe)
    id_zanaka_tal = 0
    id_vady_tal = 0
    lv_zanaka_tal = 'Lahy'
    for i, ol in enumerate(taranaka):
        taranaka[i] = taranaka[i] + (id_zanaka_tal,)+ (id_vady_tal,)+ (lv_zanaka_tal,)
        # rehefa zanaka vao miova
        if ol[1]==2:
            id_zanaka_tal = ol[0]
            id_vady_tal = ol[8]
            lv_zanaka_tal = ol[7]

    dada_lahy = query_dada(id_dadabe,'lahy')
    neny_lahy = query_neny(id_dadabe,'lahy')
    dada_vavy = query_dada(id_bebe,'vavy')
    neny_vavy = query_neny(id_bebe,'vavy')
    rar = {
        'dada_lahy' : dada_lahy[0],
        'neny_lahy' : neny_lahy[0],
        'dada_vavy' : dada_vavy[0],
        'neny_vavy' : neny_vavy[0]
    }
    info_taranaka = {
        'taranaka': taranaka,
        'id_dada' : id_zanaka_tal,
        'rar': rar
    }
    # print(rar)
    print(info_taranaka)
    return info_taranaka


@login_required(login_url='/login/')
def edit_olona_view(request, id_dadabe, id_bebe, id_olona):
    obj=Olona.objects.get(id=id_olona)
    #print(obj)
    form = OlonaForm(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
 #       form.OlonaForm()
    info_taranaka = get_taranaka(id_dadabe, id_bebe)
    print(info_taranaka)
    context = {
        'taranaka': info_taranaka['taranaka'],
        'rar':info_taranaka['rar'],
		'id_dada': info_taranaka['id_dada'],
        'id_dadabe':id_dadabe,
        'id_bebe':id_bebe,
        'form' : form,
		}
    return render(request, 'edit_olona.html', context)

@login_required(login_url='/login/')
def edit_olona232_view(request):
    return edit_olona_view(request, 2, 3, 2)

@login_required(login_url='/login/')
def new_zanaka_view(request,id_dadabe,id_bebe):
    initial_data = {
        'ray':id_dadabe,
        'reny':id_bebe
    }
    my_form = OlonaRawForm(initial = initial_data)
    if request.method == "POST":
        my_form = OlonaRawForm(request.POST or None)
        if my_form.is_valid():
            # print(my_form.cleaned_data)
            Olona.objects.create(**my_form.cleaned_data)


    info_taranaka = get_taranaka(id_dadabe,id_bebe)
    # print(info_taranaka)
    context = {
        'taranaka': info_taranaka['taranaka'],
        'rar':info_taranaka['rar'],
		'id_dada': info_taranaka['id_dada'],
        'id_dadabe':id_dadabe,
        'id_bebe':id_bebe,
        'form' : my_form,
        }
    return render(request, 'new_zanaka.html', context)


@login_required(login_url='/login/')
def new_zafy_view(request,id_dadabe,id_bebe,id_dada,id_neny):
    initial_data = {
        'ray':id_dada,
        'reny':id_neny
    }
    my_form = OlonaRawForm(initial = initial_data)
    if request.method == "POST":
        my_form = OlonaRawForm(request.POST or None)
        if my_form.is_valid():
            print(my_form.cleaned_data)
            Olona.objects.create(**my_form.cleaned_data)

    info_taranaka = get_taranaka(id_dadabe,id_bebe)
    print(info_taranaka)
    context = {
        'taranaka': info_taranaka['taranaka'],
        'rar':info_taranaka['rar'],
		'id_dada': info_taranaka['id_dada'],
        'id_dadabe':id_dadabe,
        'id_bebe':id_bebe,
        'id_dada':id_dada,
        'id_neny':id_neny,
        'form' : my_form,
        }
    return render(request, 'new_zafy.html', context)


@login_required(login_url='/login/')
def new_vady_view(request,id_dadabe,id_bebe, id_tompony):
    initial_data = {
        'ray':0,
        'reny':0
    }
    my_form = OlonaRawForm(initial = initial_data)
    if request.method == "POST":
        my_form = OlonaRawForm(request.POST or None)
        if my_form.is_valid():
            new_obj =  Olona.objects.create(**my_form.cleaned_data)
            last_id = new_obj.id
            sexe = test_lahyvavy(id_tompony)
            if sexe == 'lahy':
               new_object = Vady(id_lahy=id_tompony, id_vavy=last_id)
            else:
               new_object = Vady(id_lahy=last_id, id_vavy=id_tompony)
            new_object.save()
            
    info_taranaka = get_taranaka(id_dadabe,id_bebe)
    context = {
        'taranaka': info_taranaka['taranaka'],
        'rar':info_taranaka['rar'],
		'id_dada': info_taranaka['id_dada'],
        'id_dadabe':id_dadabe,
        'id_bebe':id_bebe,
        'id_tompony':id_tompony,
        'form' : my_form,
        }
    return render(request, 'new_vady.html', context)


def new_rar_view(request,id_dadabe,id_bebe, lahy_vavy, dada_neny):
    initial_data = {
        'ray':0,
        'reny':0
    }
    my_form = OlonaRawForm(initial = initial_data)
    if request.method == "POST":
        my_form = OlonaRawForm(request.POST or None)
        if my_form.is_valid():
            new_obj =  Olona.objects.create(**my_form.cleaned_data)
            last_id = new_obj.id
            if lahy_vavy == 'lahy' and dada_neny == 'dada':
                olona = Olona.objects.get(id = id_dadabe)
                olona.ray =  last_id 
                olona.save()
            if lahy_vavy == 'lahy' and dada_neny == 'neny':
                olona = Olona.objects.get(id = id_dadabe)
                olona.reny =  last_id 
                olona.save()
            if lahy_vavy == 'vavy' and dada_neny == 'dada':
                olona = Olona.objects.get(id = id_bebe)
                olona.ray =  last_id 
                olona.save()
            if lahy_vavy == 'vavy' and dada_neny == 'neny':
                olona = Olona.objects.get(id = id_bebe)
                olona.reny =  last_id 
                olona.save()
    info_taranaka = get_taranaka(id_dadabe,id_bebe)
    context = {
        'taranaka': info_taranaka['taranaka'],
        'rar':info_taranaka['rar'],
		'id_dada': info_taranaka['id_dada'],
        'id_dadabe':id_dadabe,
        'id_bebe':id_bebe,
        'lahy_vavy':lahy_vavy, 
        'dada_neny':dada_neny,
        'form' : my_form,
        }
    return render(request, 'new_rar.html', context)


@login_required(login_url='/login/')
def new_vady_view(request,id_dadabe,id_bebe, id_tompony):
    initial_data = {
        'ray':0,
        'reny':0
    }
    my_form = OlonaRawForm(initial = initial_data)
    if request.method == "POST":
        my_form = OlonaRawForm(request.POST or None)
        if my_form.is_valid():
            new_obj =  Olona.objects.create(**my_form.cleaned_data)
            last_id = new_obj.id
            sexe = test_lahyvavy(id_tompony)
            if sexe == 'lahy':
               new_object = Vady(id_lahy=id_tompony, id_vavy=last_id)
            else:
               new_object = Vady(id_lahy=last_id, id_vavy=id_tompony)
            new_object.save()
            
    info_taranaka = get_taranaka(id_dadabe,id_bebe)
    context = {
        'taranaka': info_taranaka['taranaka'],
        'rar':info_taranaka['rar'],
		'id_dada': info_taranaka['id_dada'],
        'id_dadabe':id_dadabe,
        'id_bebe':id_bebe,
        'id_tompony':id_tompony,
        'form' : my_form,
        }
    return render(request, 'new_vady.html', context)
    
def load_fivs(request):
    faritra_id = request.GET.get("faritra")
    fivs = Fivondronana.objects.filter(faritra_id=faritra_id)
    return render(request, "fivondronana_options.html", {"fivs": fivs})


def load_firs(request):
    fivondronana_id = request.GET.get("fivondronana")
    #print(fivondronana_id)
    firs = Firaisana.objects.filter(fivondronana_id=fivondronana_id)
    #print(firs)
    return render(request, "firaisana_options.html", {"firs": firs})