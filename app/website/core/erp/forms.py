from django import forms
from .models import Evaluation

class ScheduleForm(forms.Form):
    opciones_carrera = (
        ('INCE', 'INCE'),
        ('IGFO', 'IGFO'),
        ('INBI', 'INBI'),
        ('INRO', 'INRO'),
        ('INNI', 'INNI'),
        ('INCO', 'INCO'),
        ('INFO', 'INFO'),
        ('ICOM', 'ICOM'),
    )
    opciones_ciclo = (
        ('202410', '202410 - Calendario 24 A'),
        ('2023Z', '2023Z - Calendario 23Z Cuatrimestre'),
        ('2023Y', '2023Y - Calendario 23Y Cuatrimestre'),
        ('2023X', '2023X - Calendario 23X Cuatrimestre'),
        ('2023J', '2023J - Calendario 23 J'),
        ('2023F', '2023F - Promocion 2023F'),
        ('2023E', '2023E - Promocion 2023E'),
        ('2023C', '2023C - Promocion 2023C'),
        ('202380', '202380 - Ciclo de Verano 2023'),
        ('202320', '202320 - Calendario 23 B'),
        ('202310', '202310 - Calendario 23 A'),
        ('2022Z', '2022Z - Calendario 22Z Cuatrimestre'),
        ('2022Y', '2022Y - Calendario 22Y Cuatrimestre'),
        ('2022X', '2022X - Calendario 22X Cuatrimestre'),
        ('2022H', '2022H - Promocion 2022H'),
        ('2022F', '2022F - Promocion 2022F'),
        ('2022E', '2022E - Promocion 2022E'),
        ('2022C', '2022C - Promocion 2022C'),
        ('202220', '202220 - Calendario 22 B'),
        ('202210', '202210 - Calendario 22 A'),
        ('2021Z', '2021Z - Calendario 21Z Cuatrimestre'),
        ('2021Y', '2021Y - Calendario 21Y Cuatrimestre'),
        ('2021X', '2021X - Calendario 21X Cuatrimestre'),
        ('2021I', '2021I - Promocion 2021I'),
        ('2021G', '2021G - Promocion 2021G'),
        ('2021F', '2021F - Promocion 2021F'),
        ('2021D', '2021D - Promocion 2021D'),
        ('2021C', '2021C - Promocion 2021C'),
        ('202120', '202120 - Calendario 21 B'),
        ('202110', '202110 - Calendario 21 A'),
        ('2020Z', '2020Z - Calendario 20Z Cuatrimestre'),
        ('2020G', '2020G - Promocion 2020G'),
        ('2020D', '2020D - Promocion 2020D'),
        ('202080', '202080 - Ciclo de Verano 2020'),
        ('202020', '202020 - Calendario 20 B'),
        ('202010', '202010 - Calendario 20 A'),
        ('2019E', '2019E - Promocion 2019E'),
        ('2019D', '2019D - Promocion 2019D'),
        ('2019C', '2019C - Promocion 2019C'),
        ('201980', '201980 - Ciclo de Verano 2019'),
        ('201920', '201920 - Calendario 19 B'),
        ('201910', '201910 - Calendario 19 A'),
        ('2018G', '2018G - Promocion 2018G'),
        ('2018F', '2018F - Promocion 2018F'),
        ('2018E', '2018E - Promocion 2018E'),
        ('2018D', '2018D - Promocion 2018D'),
        ('201880', '201880 - Ciclo de Verano 2018'),
        ('201820', '201820 - Calendario 18 B'),
        ('201810', '201810 - Calendario 18 A'),
        ('2017I', '2017I - Promocion 2017I'),
        ('2017F', '2017F - Promocion 2017F'),
        ('2017E', '2017E - Promocion 2017E'),
        ('2017D', '2017D - Promocion 2017D'),
        ('201780', '201780 - Ciclo de Verano 2017'),
        ('201720', '201720 - Calendario 17 B'),
        ('201710', '201710 - Calendario 17 A'),
        ('2016T', '2016T - Promocion 2016T'),
        ('2016S', '2016S - Promocion 2016S'),
        ('2016R', '2016R - Promocion 2016R'),
        ('2016E', '2016E - Promocion 2016E'),
        ('201680', '201680 - Ciclo de Verano 2016'),
        ('201620', '201620 - Calendario 16 B'),
        ('201610', '201610 - Calendario 16 A'),
        ('2015T', '2015T - Promocion 2015T'),
        ('2015S', '2015S - Promocion 2015S'),
        ('2015G', '2015G - Promocion 2015G'),
        ('2015E', '2015E - Promocion 2015E'),
        ('201580', '201580 - Ciclo de Verano 2015'),
        ('201520', '201520 - Calendario 15 B'),
        ('201510', '201510 - Calendario 15 A'),
        ('2014T', '2014T - Promocion 2014T'),
        ('2014S', '2014S - Promocion 2014S'),
        ('2014R', '2014R - Promocion 2014R'),
        ('2014D', '2014D - Promocion 2014D'),
        ('201480', '201480 - Cursos de Verano 2014'),
        ('201420', '201420 - Calendario 14 B'),
        ('201410', '201410 - Calendario 14 A'),
        ('2013S', '2013S - Promocion 2013S'),
        ('2013R', '2013R - Promocion 2013R'),
        ('201380', '201380 - Cursos de Verano 2013'),
        ('201320', '201320 - Calendario 13 B'),
        ('201310', '201310 - Calendario 13 A'),
        ('2012T', '2012T - Promocion 2012T'),
        ('2012S', '2012S - Promocion 2012S'),
        ('2012P', '2012P - Promocion 2012P'),
        ('201280', '201280 - Cursos de Verano 2012'),
        ('201220', '201220 - Calendario 12 B'),
        ('201210', '201210 - Calendario 12 A'),
        ('2011Z', '2011Z - Promocion 2011Z'),
        ('2011T', '2011T - Promocion 2011T'),
        ('2011S', '2011S - Promocion 2011S'),
        ('2011H', '2011H - Promocion 2011H'),
        ('201180', '201180 - Cursos de Verano 2011'),
        ('201120', '201120 - Calendario 11 B'),
        ('201110', '201110 - Calendario 11 A'),
        ('2010S', '2010S - Promocion 2010S'),
        ('201090', '201090 - Calendario 10 U'),
        ('201080', '201080 - Cursos de Verano 2010'),
        ('201020', '201020 - Calendario 10 B'),
        ('201010', '201010 - Calendario 10 A'),
        ('200990', '200990 - Calendario 09 U'),
        ('200980', '200980 - Cursos de Verano 2009'),
        ('200920', '200920 - Calendario 09 B'),
        ('200910', '200910 - Calendario 09 A'),
        ('200890', '200890 - Calendario 08 U'),
        ('200880', '200880 - Cursos de Verano 2008'),
        ('200820', '200820 - Calendario 08 B'),
        ('200810', '200810 - Calendario 08 A'),
        ('200790', '200790 - Calendario 07 U'),
        ('200780', '200780 - Cursos de Verano 2007'),
        ('200720', '200720 - Calendario 07 B'),
        ('200710', '200710 - Calendario 07 A'),
        ('200690', '200690 - Calendario 06 U'),
        ('200680', '200680 - Cursos de Verano 2006'),
        ('200620', '200620 - Calendario 06 B'),
        ('200610', '200610 - Calendario 06 A'),
        ('200580', '200580 - Cursos de Verano 2005'),
        ('200520', '200520 - Calendario 05 B'),
        ('200510', '200510 - Calendario 05 A'),
        ('200480', '200480 - Cursos de Verano 2004'),
        ('200420', '200420 - Calendario 04 B'),
        ('200410', '200410 - Calendario 04 A'),
        ('200380', '200380 - Cursos de Verano 2003'),
        ('200320', '200320 - Calendario 03 B'),
        ('200310', '200310 - Calendario 03 A'),
        ('200280', '200280 - Cursos de Verano 2002'),
        ('200220', '200220 - Calendario 02 B'),
        ('200210', '200210 - Calendario 02 A'),
        ('200160', '200160 - Calendario 01 "A" Anualidades'),
        ('200130', '200130 - Calendario 01"C" cuatrimestres'),
        ('200120', '200120 - Calendario 01 B'),
        ('200110', '200110 - Calendario 01 A'),
        ('200099', '200099 - Calendario de prueba'),
        ('200060', '200060 - Calendario 2000 "B" anualidades'),
        ('200050', '200050 - Calendario 2000 "E"'),
        ('200030', '200030 - Calendario 2000 C'),
        ('200020', '200020 - Calendario 00 B'),
        ('200010', '200010 - Calendario 00 A'),
        ('199990', '199990 - Calendario de Prueba'),
        ('199960', '199960 - Calendario 99 "A" anualidades'),
        ('199950', '199950 - Calendario 99 "E" cuatrimestre'),
        ('199921', '199921 - Calendario 99 \'B\''),
        ('199920', '199920 - Calendario 99 B'),
        ('199911', '199911 - Calendario 99 \'A\' bis'),
        ('199910', '199910 - Calendario 99 A'),
        ('199870', '199870 - Calendario 98 "B" anualidades'),
        ('199860', '199860 - Calendario 98 "A" anualidades'),
        ('199850', '199850 - Calendario 98 "E"'),
        ('199840', '199840 - Calendario 98 "D" cuatrimestre'),
        ('199830', '199830 - Calendario 98 "C"'),
        ('199820', '199820 - Calendario 98 B'),
        ('199810', '199810 - Calendario 98 A'),
        ('199720', '199720 - Calendario 97 B'),
        ('199710', '199710 - Calendario 97 A'),
        ('199620', '199620 - Calendario 96 B'),
        ('199611', '199611 - Calendario 1996 Extra'),
        ('199610', '199610 - Calendario 96 A'),
        ('199520', '199520 - Calendario 95 B'),
        ('199510', '199510 - Calendario 95 A'),
        ('199420', '199420 - Calendario 94 B'),
        ('199410', '199410 - Calendario 94 A'),
        ('199320', '199320 - Calendario 93 B'),
        ('199310', '199310 - Calendario 93 A'),
        ('199220', '199220 - Calendario 92 B'),
        ('199110', '199110 - Calendario 91 A'),
        ('199030', '199030 - Calendario 90 "C"'),
        ('199010', '199010 - Calendario 90 A'),
        ('198810', '198810 - Calendario 88 A'),
        ('198210', '198210 - Calendario 82 A'),
        ('198010', '198010 - Calendario 80 A'),
    )
    opciones_inicio = [(hora, f'{hora:02}:00') for hora in range(7, 21)]
    opciones_fin = [(hora, f'{hora:02}:00') for hora in range(8, 22)]

    carrera = forms.ChoiceField(choices=opciones_carrera, label='Carrera', widget=forms.Select(attrs={'class': 'form-control select2'}))
    ciclo = forms.ChoiceField(choices=opciones_ciclo, label='Ciclo', widget=forms.Select(attrs={'class': 'form-control select2'}))
    materias = forms.CharField(max_length=100, label='Materias')

    lunes = forms.BooleanField(required=False, widget=forms.CheckboxInput(attrs={'class': 'icheck-success', 'id': 'lunes'}), label='')
    inicioL = forms.ChoiceField(choices=opciones_inicio, label='Inicio', widget=forms.Select(attrs={'class': 'form-control select2'}))
    finL = forms.ChoiceField(choices=opciones_fin, label='Fin', widget=forms.Select(attrs={'class': 'form-control select2'}))

    martes = forms.BooleanField(required=False, widget=forms.CheckboxInput(attrs={'class': 'icheck-success', 'id': 'martes'}), label='')
    inicioM = forms.ChoiceField(choices=opciones_inicio, label='Inicio', widget=forms.Select(attrs={'class': 'form-control select2'}))
    finM = forms.ChoiceField(choices=opciones_fin, label='Fin', widget=forms.Select(attrs={'class': 'form-control select2'}))

    miercoles = forms.BooleanField(required=False, widget=forms.CheckboxInput(attrs={'class': 'icheck-success', 'id': 'miercoles'}), label='')
    inicioMi = forms.ChoiceField(choices=opciones_inicio, label='Inicio', widget=forms.Select(attrs={'class': 'form-control select2'}))
    finMi = forms.ChoiceField(choices=opciones_fin, label='Fin', widget=forms.Select(attrs={'class': 'form-control select2'}))

    jueves = forms.BooleanField(required=False, widget=forms.CheckboxInput(attrs={'class': 'icheck-success', 'id': 'jueves'}), label='')
    inicioJ = forms.ChoiceField(choices=opciones_inicio, label='Inicio',widget=forms.Select(attrs={'class': 'form-control select2'}))
    finJ = forms.ChoiceField(choices=opciones_fin, label='Fin', widget=forms.Select(attrs={'class': 'form-control select2'}))

    viernes = forms.BooleanField(required=False, widget=forms.CheckboxInput(attrs={'class': 'icheck-success', 'id': 'viernes'}), label='')
    inicioV = forms.ChoiceField(choices=opciones_inicio, label='Inicio', widget=forms.Select(attrs={'class': 'form-control select2'}))
    finV = forms.ChoiceField(choices=opciones_fin, label='Fin', widget=forms.Select(attrs={'class': 'form-control select2'}))

    sabado = forms.BooleanField(required=False, widget=forms.CheckboxInput(attrs={'class': 'icheck-success', 'id': 'sabado'}), label='')
    inicioS = forms.ChoiceField(choices=opciones_inicio, label='Inicio', widget=forms.Select(attrs={'class': 'form-control select2'}))
    finS = forms.ChoiceField(choices=opciones_fin, label='Fin', widget=forms.Select(attrs={'class': 'form-control select2'}))
    
    def save(self):
        Schedule = super().save(commit=False)
        return Schedule


class EvaluationForm(forms.ModelForm):
    class Meta:
        model = Evaluation
        fields = ['knowledge', 'punctuality', 'difficult', 'dedication']

class CommentForm(forms.ModelForm):
    class Meta:
        model = Evaluation
        fields = ['comment']
        widgets = {
            'comment': forms.Textarea(attrs={'rows': 2, 'cols': 95}),
        }
