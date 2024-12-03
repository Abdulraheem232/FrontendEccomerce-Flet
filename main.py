from flet import *
import requests
from data import *

def main(page:Page):
    page.theme_mode = ThemeMode.DARK
    page.title = "Eccomerce frontend flet"
    page.horizontal_alignment = CrossAxisAlignment.CENTER
    page.vertical_alignment = MainAxisAlignment.CENTER
    userproduct = []

    def homepage():
        def detailpage(id):
            page.clean()
            
            for productdetail in data:
               if productdetail["id"] == id:
                  detailsection = Container(bgcolor="#1e1e1e",width=1000,padding=30, alignment=alignment.center ,content=Column(controls=[
                     Image(src=productdetail["image"] , width=400 , height=400 ,fit=ImageFit.CONTAIN,),
                     Text(productdetail["title"] , weight="bold" , size=50),
                     Text(productdetail["description"] , size=25),
                     Text(f"Category : {productdetail["category"]}" , size=15),
                     Text(f"Rating : {productdetail["rating"]["rate"]} given by {productdetail["rating"]["count"]} peoples" , size=15),
                     Text(f"Price : ${productdetail["price"]}"),
                     ElevatedButton(icon=icons.ADD , text="Add to cart" , on_click=lambda e , p=productdetail : addtocart(p))
                  ] , alignment=alignment.center))
                 
                  detailsectionscroll = Column(controls=[detailsection] ,scroll=ScrollMode.ALWAYS , expand=True)
                  
                  page.add(detailsectionscroll)
            
            page.add(navbar)          
            
        def addtocart(product):
         userproduct.append(product)

        productsdata = Row(wrap=True , alignment=alignment.center , spacing=40, scroll=ScrollMode.AUTO , expand=True)
        for product in data:
         product_container = Container(
            width=500,
            padding=30,
            bgcolor="#1e1e1e",
            margin=30,
            content=Column(
                controls=[
                    Image(src=product["image"] , fit=ImageFit.CONTAIN ,height=300,width=500),
                    Text(product["title"], size=30, weight="bold"),
                    Text(product["description"]),
                    Text(product["price"] , color="red" , weight="bold"),
                    ElevatedButton(icon=icons.ADD , text="Add to cart" , on_click=lambda e, p=product:addtocart(p) )
                ]
            ),
            on_click=lambda e, id=product["id"]:detailpage(id)
        )

         productsdata.controls.append(product_container)
       
        return productsdata
    
    def loadcart():
        cartdata  = Column(scroll=ScrollMode.AUTO  ,expand=True , spacing=20)
         
        for cart in userproduct:
           item = Container(bgcolor="#1e1e1e", height=120 ,width=600,padding=20 , content=Row(controls=[Image(cart["image"] , width=70 ,height=70) , Text(cart["title"] , width=None) ,Text(cart["price"] , color="red" , weight="bold")] ,spacing=60))
           cartdata.controls.append(item)
        
        return cartdata

    def navigationchange(e):
        page.clean()
        print(e)
        if e.control.selected_index == 1:
            page.add(Text(size=80 , weight="bold", value="Your cart 🛒 items!"),loadcart())
        if e.control.selected_index == 0:
            page.add(homepage())
        if e.control.selected_index == 2:
           page.add(Text("Your account"))
        page.add(navbar)

    navbar = NavigationBar(destinations=[NavigationBarDestination(icon=icons.HOME, label="Home",),NavigationBarDestination(icon=icons.ADD_BOX , label="Cart"),NavigationBarDestination(icon=icons.ACCOUNT_CIRCLE , label="Account")] , on_change=navigationchange ,selected_index=0)
    page.add(homepage(),navbar)

app(target=main ,view=AppView.WEB_BROWSER , port=8550)