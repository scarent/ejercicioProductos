from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request,'appTemplates/index.html') #app/archivo

def renderMenu(request, Categoria,producto1,producto2,producto3):
    datos={
        "Categoria":Categoria,
        "Producto1":producto1,
        ""
        "Producto2":producto2,
        "Producto3":producto3
    }
    return render(request,'/appTemplates/tienda.html,',datos)

def renderJuguetes(request):
    datos={"Categoria":"Juguetes",
           "Producto1":"Rayo mcqueen",
           "Descripcion1":"Auto Rayo Mcqueen",
           "img1":"rayo.jpg",
           "Precio1":"5000",

           "Producto2":"Paw patrol",
           "img2":"patrol.png",
           "Descripcion2":"Peluche paw patrol",
           "Precio2":"12.000",

           "Producto3":"Figura dinosaurio",
           "img3":"dino.png",
           "Descripcion3":"Dinosaurio Jurassic park",
           "Precio3":"10.000"}
    
    return render(request,'appTemplates/tienda.html',datos)

def renderElectronica(request):
    datos={"Categoria":"Electronica",
           "Producto1":"Television LG",
           "img1":"tv.png",
           "Precio1":"450.000",

           "Producto2":"Mouse Gamer",
           "img2":"mouse.png",
           "Precio2":"60.000",

           "Producto3":"Teclado rgb",
           "img3":"teclado.png",
           "Precio3":"40.000"}
    
    return render(request,'appTemplates/tienda.html',datos)

def renderRopa(request):
    datos={"Categoria":"Ropa",
           "Producto1":"Jeans",
           "img1":"YINES.png",
           "Precio1":"25.990",

           "Producto2":"Zapatilla",
           "img2":"tilla.png",
           "Precio2":"35.000",

           "Producto3":"Polera",
           "img3":"polera.png",
           "Precio3":"15.000"}
    
    return render(request,'appTemplates/tienda.html',datos)
    
    