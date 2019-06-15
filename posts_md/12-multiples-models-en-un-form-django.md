Title: Multiples Models en un Form Django
Date: 2016-01-29T06:42:23+00:00
Description: 
Tags: Django
---
# Multiples Models en un Form Django


Dando mis primeros pasos en django, me encontré con el ligero problema de no saber como subir datos a varios modelos desde una sola vista, bueno inicialmente me di cuenta que en un template view puedo hacer algo como 

```
class MiTemplateView(TemplateView):
    template_name='ruta/al/template'
    formulario1=MiFormulario1(prefix='formulario1')
    formulario2=MiFormulario1(prefix='formulario2')
... etc
```


```
def get_context_data(self, **kwargs):  
	context=super(SubirMaterial, self).get_context_data(**kwargs)  
    if 'formulario1' not in context:  
    context['formulario1']=self.formulario1  
    if 'formulario2' not in context:  
 		context['formulario2']=self.formulario2  
 	... etc  
 	return context 
```
 Y ya con eso tengo los forms en el template, en el template es tan facil como
 
```
<form enctype="multipart/form-data" method="POST">
	{% csrf_token %}  
 	{{formulario1.as_p}}  
 	{{formulario2.as_p}}  
 	…etc
</form>
```

 Y ahora solo escribo el post
```
def post(self, request, *args, **kwargs):
	formulario1=MiFormulario1(request.POST, prefix=’formulario1?)  
 	formulario2=MiFormulario2(request.POST, prefix=’formulario2?)  
 	… etc  
 	if formulario1.is_valid():  
 		formulario1.save()  
 	if formulario2.is_valid():  
 		formulario2.save()  
 	…etc
```

Ahora puede que algunos formularios requieran algunas Llaves Foraneas, digamos es el caso de formulario1 y formulario2, tan facil como
```
	id_formulario1=formulario1.save()  
	elemento_modelo_formulario2=formulario2.save(commit=False)  
	elemento_modelo_formulario2.llaveForaneaFormulario1 = id_formulario1  
	formulario2.save()
```

Y ét violá, ojalá algún día aprenda bastante de django y me de cuenta como hacerlo mas elegantemente


