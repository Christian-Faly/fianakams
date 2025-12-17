from django import forms
from django.urls import reverse
from .models import Olona
from .models import Faritra, Fivondronana, Firaisana 


class OlonaForm(forms.ModelForm):
    lahy_vavy = forms.ChoiceField(
        choices=[
            ('Lahy', 'Lahy'),
            ('Vavy', 'Vavy'),
        ]
    )
    class Meta:
        model = Olona
        fields = [
            'anarana','fanampiny','fiantsoana','daty_nahaterahana','lahy_vavy','toerana_nahaterahana',
            'firenena_onenana','faritra','fivondronana','firaisana','adiresy','diplaoma','asa'
        ]


class OlonaRawForm(forms.Form):
    anarana = forms.CharField(max_length=50)
    fanampiny = forms.CharField(max_length=50)
    fiantsoana = forms.CharField(max_length=20)
    daty_nahaterahana = forms.DateField()
    lahy_vavy = forms.ChoiceField(
        choices=[
            ('Lahy', 'Lahy'),
            ('Vavy', 'Vavy'),
        ]
    )
    toerana_nahaterahana = forms.CharField(max_length = 50)
    firenena_onenana = forms.CharField(max_length = 50)
    faritra = forms.ModelChoiceField(required=False, queryset=Faritra.objects.only('anarana'),
        widget=forms.Select(attrs={"hx-get": "/load_fivs/", "hx-target": "#id_fivondronana"}))
    fivondronana = forms.ModelChoiceField(required=False,queryset=Fivondronana.objects.none(),
        widget=forms.Select(attrs={"hx-get": "/load_firs/", "hx-target": "#id_firaisana"}))
    firaisana = forms.ModelChoiceField(required=False, queryset=Firaisana.objects.none())
    adiresy = forms.CharField(max_length = 50)
    diplaoma = forms.CharField(max_length = 50)
    asa = forms.CharField(max_length = 50)
    ray = forms.IntegerField()	
    reny = forms.IntegerField()
    fizokiana = forms.IntegerField()
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        
        if "faritra" in self.data:
            faritra_id = int(self.data.get("faritra"))
            self.fields["fivondronana"].queryset = Fivondronana.objects.filter(faritra_id=faritra_id)

        if "fivondronana" in self.data:
            fivondronana_id = int(self.data.get("fivondronana"))
            self.fields["firaisana"].queryset = Firaisana.objects.filter(fivondronana_id=fivondronana_id)


