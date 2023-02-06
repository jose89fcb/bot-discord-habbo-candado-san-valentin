import urllib
import json
import requests
import discord
from discord.ext import commands
import datetime
import io
 
from urllib import parse, request
from PIL import Image, ImageDraw, ImageFont, ImageFile
import time


with open("configuracion.json") as f:
    config = json.load(f)

bot = commands.Bot(command_prefix='!', description="ayuda bot") #Comando
bot.remove_command("help") # Borra el comando por defecto !help

@bot.command()
async def keko(ctx,  keko1, keko2):
    await ctx.message.delete()
    await ctx.send("Generando candado...", delete_after=0)
    time.sleep(3)
    
    response = requests.get(f"https://www.habbo.es/api/public/users?name={keko1}")
    response1 = requests.get(f"https://www.habbo.es/api/public/users?name={keko2}")
    
    try:

     habbo = response.json()['figureString']
   

  

     habbo1 = response1.json()['figureString']
    except KeyError:
        await ctx.send("Uno de los kekos no existe!")


   
    

    
    
   
    try:

     url = "https://www.habbo.com/habbo-imaging/avatarimage?size=l&figure="+ habbo +"&direction=2&head_direction=2"
     img1 = Image.open(io.BytesIO(requests.get(url).content))
     img1 = img1.resize((64,110), Image.ANTIALIAS)#tamaño del keko 1
    
   

     url1 = "https://www.habbo.com/habbo-imaging/avatarimage?size=l&figure="+ habbo1 +"&direction=4&head_direction=2"
     habbol = Image.open(io.BytesIO(requests.get(url1).content))
     habbol = habbol.resize((64,110), Image.ANTIALIAS)#tamaño del keko 2


    
    


    

   

    

    
    
    



     img2 = img1.copy()
    
    
    
     img1 = Image.open(r"Candado San Valentin/Candado San Valentin.png").convert("RGBA") #Imagen del candado de amor sant valentin
     img1.paste(img2,(124,3), mask = img2) #Posicion del keko 1
    
    ###
    

     img1.paste(habbol,(190,3), mask = habbol) #Posicion del keko 2
    
  
     draw = ImageDraw.Draw(img1)
     font = ImageFont.truetype("Fuente/UbuntuRegular-latin.246ea4b3.otf", 13) #Tamaño de la fuente (textos)

     draw.text((110, 120), f"Hasta que los pixels nos separen", font=font, fill=(101,36,97))  #Texto y color
    
    
     fecha = time.strftime("%d/%m/%Y", time.gmtime()) #Fecha
     draw.text((170, 150), f"{fecha}", font=font, fill=(101,36,97))


     draw.text((150, 175), f"{keko1}         {keko2}", font=font, fill=(101,36,97)) #Nombres de los kekos
    
    

 
    
    

    




    

    
    
    
   
    
   
       


      
    
       
      

      
    
       
            
        
        
        
       
        
     with io.BytesIO() as image_binary:
        img1.save(image_binary, 'PNG')
        image_binary.seek(0)

        await ctx.send(file=discord.File(fp=image_binary, filename=f'kekos-{keko1}{keko2}.png'))
    except UnboundLocalError:
        
        habbo1=":("
        habbo=":("
            
         
        
        
        
        


@bot.event
async def on_ready():
    print("BOT listo!")
    
bot.run(config["tokendiscord"])       
