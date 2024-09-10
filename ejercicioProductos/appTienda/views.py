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
           "Descripcion1":"Auto rayo",
           "img1":"rayo.jpg",
           "Precio1":"5000",

           "Producto2":"Paw patrol",
           "img2":"pawpatrol.png",
           "Descripcion2":"Peluche paw patrol",
           "Precio2":"15.000",

           "Producto3":"Figura dinosaurio",
           "img3":"dino.png",
           "Descripcion3":"Dinosaurio",
           "Precio3":"12.000"}
    
    return render(request,'appTemplates/tienda.html',datos)

def renderElectronica(request):
    datos={"Categoria":"Electronica",
           "Producto1":"Television",
           "Descripcion1":"tv 50 pulgadas",
           "img1":"tv.png",
           "Precio1":"400.000",

           "Producto2":"Mouse",
           "img2":"mouse.png",
           "Descripcion2":"Mouse logitech",
           "Precio2":"60.000",

           "Producto3":"Teclado rgb",
           "img3":"teclado.png",
           "Descripcion3":"teclado mecanico ",
           "Precio3":"40.000"}
    
    return render(request,'appTemplates/index.html',datos)

def renderRopa(request):
    datos={"Categoria":"Ropa",
           "Producto1":"Jeans",
           "Descripcion1":"Pantalon jeans ",
           "img1":"jines.jpg",
           "Precio1":"20.000",

           "Producto2":"Zapatilla",
           "img2":"tilla.png",
           "Descripcion2":"zapatillas converse",
           "Precio2":"40.000",

           "Producto3":"Polera",
           "img3":"polera.png",
           "Descripcion3":"Polera hugo boss",
           "Precio3":"15.000"}
    
    return render(request,'appTemplates/index.html',datos)
    
    