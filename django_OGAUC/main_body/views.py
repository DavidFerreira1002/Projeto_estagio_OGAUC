from django.shortcuts import render

def home(request):
    tab_title = "Home"

    class home:
        def __init__(self,titulo,texto):
                super().__init__()
                self.titulo = titulo
                self.texto = texto

    ct_titulo = "OGAUC"
    ct_texto = "Lorem ipsum dolor, sit amet consectetur adipisicing elit. Tempora corporis magnam voluptatibus maxime vel odio fugiat dolore, asperiores aliquid? Atque optio perferendis ut molestiae blanditiis odio quibusdam temporibus. Accusantium, alias."

    ct_home = home(ct_titulo,ct_texto)

    return render(request,'homeTP.html',{"tab_title":tab_title ,"home":ct_home})