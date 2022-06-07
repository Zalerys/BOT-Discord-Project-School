import giphy_client
from giphy_client.rest import ApiException
import random
import discord
from discord.ext import commands
import requests
import json
import youtube_dl
import ffmpeg



TOKEN = "OTc4MjI4OTkzNTk1Njk1MTM0.Gnedy5.ZWK4frPHZf1aSu5EGEE1w1_6VH-ovPkkrR_g1c"
api_key='Aoczl3jtpbQ6T5G6pS3Q5lRGGDpgbQxb'
api_instance = giphy_client.DefaultApi()

bot = commands.Bot(command_prefix=".", intents=discord.Intents.all())



@bot.command()
async def Help(ctx):
    #montrer les commandes disponibles 
    await ctx.channel.send(".help permet d'expliquer les commandes"+
                            "\n.sup permet de supprimer le message ecris avant"+
                            "\n.print ... permet de faire encire ton message par le bot"+
                            "\n.gif_random renvoie un gif aleatoire"+
                            "\n.gif ... renvoie le gif correspondant au message que tu as ecris"+
                            "\n.talk_help explique toute les commande de conversation/aide avec le bot"+
                            "\n.join fait rejoindre le bot au channel vocal ou tu es connecté"+
                            "\n.play ... permet d'ecouter la musique que tu as selectionner"+
                            "\n.pause met en pause la musique"+
                            "\n.resume relance la musique si elle etait en pause"+
                            "\n.leave le bot quitte le salon vocal ou il etait connecter"+
                            "\n.meteo ... donne la meteo de la ville selectioner"
                        )   
    


@bot.command()
async def sup(ctx):
    #commande pour supprimer des messages 
    await ctx.channel.purge(limit=3)

@bot.command()
async def print(ctx, *args):
    response = ""

    # loop pour re écris la phrase avec le bot 
    for arg in args:
        response = response + " " + arg

    if response == "":
        await ctx.channel.send("Tu n'as rien ecris")
    #Envoie le message dans le bon channel 
    else :
        await ctx.channel.send(response)

@bot.command()
async def gif_random(ctx,q="random"):
    #API giphy renvoie un gipf dans la categorie random en random
    try:
        api_responce = api_instance.gifs_search_get(api_key, q, limit=100, rating='R')
        lst = list(api_responce.data)
        giff = random.choice(lst)
        await ctx.channel.send(giff.embed_url)
    except ApiException as e :
        print("Exception when calling Api")


@bot.command()
async def gif(ctx,*args):
    #API giphy avec la categorie souhaité 
    i = ""
    for arg in args:
        i = i + " " + arg

    api_responce = api_instance.gifs_search_get(api_key, i, limit=100, rating='R')
    lst = list(api_responce.data)
    giff = random.choice(lst)
    await ctx.channel.send(giff.embed_url)
    
    

@bot.event
async def on_member_join(member):
    #DM la personne quand elle rejoins le discord 
    await member.send(f'Bonjour {member.name}, Bienvenue sur le discord !'+
                    "\n.help permet d'expliquer les commandes"+
                    "\n.sup permet de supprimer le message ecris avant"+
                    "\n.print ... permet de faire encire ton message par le bot"+
                    "\n.gif_random renvoie un gif aleatoire"+
                    "\n.gif ... renvoie le gif correspondant au message que tu as ecris"+
                    "\n.talk_help explique toute les commande de conversation/aide avec le bot"+
                    "\n.join fait rejoindre le bot au channel vocal ou tu es connecté"+
                    "\n.play ... permet d'ecouter la musique que tu as selectionner"+
                    "\n.pause met en pause la musique"+
                    "\n.resume relance la musique si elle etait en pause"+
                    "\n.leave le bot quitte le salon vocal ou il etait connecter"+
                    "\n.meteo ... donne la meteo de la ville selectioner"
                    )

#list des user
list_user=[]
#toute les donées utile pour le .talk
Paliers=[
    ['Python','JavaScript','PHP'],
    ['debute','specifique'],
    ['Dictionnaire','List','Class','Arbre'],
    ['https://python.doctor/page-cours-python-debutant-documentation','https://developer.mozilla.org/fr/docs/Learn/JavaScript/First_steps','http://www.lephpfacile.com/cours/'],#lien pour debutant
    ['https://courspython.com/classes-et-objets.html','https://courspython.com/dictionnaire.html','https://docs.python.org/fr/3/tutorial/datastructures.html','https://pixees.fr/informatiquelycee/n_site/nsi_term_projet_4.html'],#lien specifique pour python 1)Class 2)dictionnaire 3)list 4)arbre
    ['https://www.digitalocean.com/community/tutorials/understanding-classes-in-javascript-fr','https://developer.mozilla.org/fr/docs/Web/JavaScript/Guide/Keyed_collections','https://www.w3schools.com/js/js_arrays.asp','https://blog.lesjeudis.com/structures-de-donnees-courantes-javascript'],#lien specifique pour JavaScript 1)Class 2)dictionnaire 3)list 4)arbre
    ['https://www.php.net/manual/fr/language.oop5.php','https://www.php.net/manual/fr/language.types.array.php','https://www.php.net/manual/fr/function.list.php','https://askcodez.com/php-arbre-binaire-de-recursivite-algorithme.html'],#lien specifique pour PHP 1)Class 2)dictionnaire 3)list 4)arbre
    ['reprend','zero']
    ]



#class qui sauvegarde par utilisateur chaque etape
class user:
    def __init__(self,name,etape,langue,option):
        self.NameUser=name
        self.Etape=etape
        self.Language=langue
        self.Option=option
        



@bot.event 
async def on_message(ctx):
    if ctx.author == bot.user:
        return
    if ctx.content == 'Hello':
        await ctx.channel.send(f'Bonjour {ctx.author}')
    if ctx.content == 'Adieu':
        await ctx.channel.send(f'Adieu {ctx.author}')
    if ctx.content == 'Ping':
        await ctx.channel.send('Pong')
    if ctx.content == 'Qui est la pute ?':
        await ctx.channel.send('Martin bien sur !')
    if ctx.content == 'test':
        await ctx.channel.send('test reussi connard')

    #regarde si les message contienne le mot python et aide, envoie un message si les deux sont cumulés
    stock = ctx.content
    langue=["JavaScript","PHP","Python","python","php","javascript"]
    x = stock.split()
    for i in x :
        for l in langue:
            if l == i:
                supply=l
        if i == 'aide' or i=="d'aide":
            aide=i
              
    if aide != None and supply != None:
        if supply == "Python" or supply=="python":
            await ctx.channel.send('Si tu as besoin d\'aide en python, voila un lien qui peut etre utile : https://courspython.com/')
        elif supply=="PHP" or supply=="php":
            await ctx.channel.send('Si tu as besoin d\'aide en PHP, voila un lien qui peut etre utile : http://www.lephpfacile.com/cours/')
        elif supply=="JavaScript" or supply=="javascript":
            await ctx.channel.send('Si tu as besoin d\'aide en python, voila un lien qui peut etre utile : https://developer.mozilla.org/fr/docs/Learn/Getting_started_with_the_web/JavaScript_basics')

    #debut du .talk
    if not list_user:
        #creation du premier user
        if ctx.content=='.talk':
            await ctx.channel.send(etape0(ctx))
            return
    else : #si il y a deja un user de créer 
        
            for x in list_user:#regarde si l'utilisteur existe ou non
                if ctx.content=='.talk':
                    if x.NameUser==ctx.author:
                        
                        await ctx.channel.send(retour(ctx))
                        return
                    else :
                        await ctx.channel.send(etape0(ctx))
                        return
    for x in list_user: #regarde quel utilisateur utilise une commande et à quelle etape il est     
        if x.NameUser==ctx.author:
            if x.Etape==0:
                for e in Paliers[0]:
                    if e == ctx.content:
                        x.Language=e
                        await ctx.channel.send(etape1(x))
                        return
            if x.Etape==1:
                for e in Paliers[1]:
                    if e == ctx.content:
                        x.Option=e
                        await ctx.channel.send(etape2(x))
                        return
            if x.Etape==2:
                for e in Paliers[2]:
                    if e == ctx.content:
                        x.Option=e
                        await ctx.channel.send(etape3(x))
                        return
        
    await bot.process_commands(ctx)
              
@bot.command()
async def talk_zero(ctx):#supprime l'user
    for x in list_user:
        if x.NameUser==ctx.author:
            list_user.remove(x)
            await ctx.channel.send("Trés bien la conversation viens d'être remise à 0, parle moi quand tu es pret avec la commande .talk")
            return

@bot.command()
async def talk_reprendre(ctx):#remontre à l'utilisateur ou il en etait dans la conversation 
    for x in list_user:   #en fonction de l'utilisateur, il regarde à qu'elle etape il etait 
        if x.NameUser==ctx.author:
            if x.Etape==0:
                await ctx.channel.send(etape0(ctx))
                return
            if x.Etape==1:
                await ctx.channel.send(etape1(x))
                return
            if x.Etape==2:
                await ctx.channel.send(etape2(x))
                return
            if x.Etape==3:
                await ctx.channel.send(etape3(x))
                return

@bot.command()
async def talk_retour(ctx):#commande permettant de revenir en arriere dans la conversation
    for x in list_user:
        if x.NameUser==ctx.author:
            if x.Etape==0:
                await ctx.channel.send("Tu es deja au tout debut de la conversation, tu ne peux pas revenir en arriere")
                return
            if x.Etape==1:
                await ctx.channel.send(etape0(ctx))
                return
            if x.Etape==2:
                await ctx.channel.send(etape1(x))
                return
            if x.Etape==3:
                if x.Option=="debute":
                    await ctx.channel.send(etape2(x))
                for i in Paliers[2]:
                    if x.Option==i:
                        x.Option="specifique"
                        await ctx.channel.send(etape2(x))
                return


@bot.command()
async def talk_contact(ctx,*args):
    reponse = ""

    # loop pour re écris la phrase avec le bot 
    for arg in args:
        reponse = reponse + " " + arg

        if reponse == "":
            await ctx.channel.send("Tu n'as rien ecris, aucun message ne sera envoyer au moderateur")
        #Envoie le message dans le bon channel 
        else :
            ctx.name="Zalerys"
            ctx.id="3201"
            await ctx.author.send(f"Yo {ctx.name},"+reponse)





@bot.command()
async def talk_help(ctx):
    #commande qui explique les commande talk
    await ctx.channel.send("Description de toute mes commandes de conversation :"+
                        "\n .talk_reprendre ca te montre à qu'elle satde de la conversation ou tu étais."+
                        "\n .talk_retour reviens en arriere dans la conversation "+
                        "\n .talk_zero remet à zero la conversation"+
                        "\n .talk_contact une commande qui permet d'envoyer un message expliquant le probleme au support")
            
                        
                        
                        
                        




#Toute les fonctions, de chaque etape de la conversation  
        
def etape0(ctx):
    i = user(ctx.author,0,"Aucune","Aucune")
    list_user.append(i)
    return (f"Bonjour {ctx.author.mention}, je suis la pour t'aider."+ 
    "\n Pour qu'on puisse bien ce comprendre tu devras me repondre par les mots avec un / devant.. " +
    "\n Tu n'as pas besoin d'écire le /, bien commençons.."
    "\n Tu as besoin d'aide pour quel language ? /Python, /JavaScript, /PHP ?")
    
def etape1(player):
    player.Etape=1
    phrase = "Tu /debute " +player.Language+ " ? Ou tu as besoin d'aide dans quelque chose /specifique ?" 
    return phrase
   
def etape2(player):
    player.Etape=2
    if player.Option=="debute":
        if player.Language=="Python":
            return ("Je te conseil pour debuter en Python ce lien : "+Paliers[3][0])
        if player.Language=="JavaScript":
            return ("Je te conseil pour debuter en JavaScript ce lien : "+Paliers[3][1])
        if player.Language=="PHP":
            return ("Je te conseil pour debuter en PHP ce lien : "+Paliers[3][2])
    if player.Option=="specifique":
        return ("Pour "+player.Language+", tu veux de l'aide en quoi ?"
        "\n /Class, /Dictionnaire, /List, /Arbre ?")
    
def etape3(player):
    player.Etape=3
    if player.Language=="Python":
        if player.Option=="Class":
            return("Pour les class je pense que ce lien peut t'aider : "+Paliers[4][0])
        if player.Option=="List":
            return("Pour les list je pense que ce lien peut 'aider : "+Paliers[4][2])
        if player.Option=="Dictionnaire":
            return("Pour les dictionnaires je pense que ce lien peut t'aider : "+Paliers[4][1])
        if player.Option=="Arbre":
            return("Pour faire un arbre je pense que ce lien peut t'aider : "+Paliers[4][3])


    if player.Language=="JavaScript":
        if player.option=="Class":
            return("Pour les class je pense que ce lien peut t'aider : "+Paliers[5][0])
        if player.option=="List":
            return("Pour les list je pense que ce lien peut 'aider : "+Paliers[5][2])
        if player.option=="Dictionnaire":
            return("Pour les dictionnaires je pense que ce lien peut t'aider : "+Paliers[5][1])
        if player.option=="Arbre":
            return("Pour faire un arbre je pense que ce lien peut t'aider : "+Paliers[5][3])

    if player.Language=="PHP":
        if player.option=="Class":
            return("Pour les class je pense que ce lien peut t'aider : "+Paliers[6][0])
        if player.option=="List":
            return("Pour les list je pense que ce lien peut 'aider : "+Paliers[6][2])
        if player.option=="Dictionnaire":
            return("Pour les dictionnaires je pense que ce lien peut t'aider : "+Paliers[6][1])
        if player.option=="Arbre":
            return("Pour faire un arbre je pense que ce lien peut t'aider : "+Paliers[6][3])


def retour(ctx):
    return (f"Welcome back {ctx.author.mention}. On reprend la conversation ? Ou tu veux repartir à zero ? Les commandes sont .talk_reprendre ou .talk_zero")



queue=[]


#musics = {}
ytdl = youtube_dl.YoutubeDL()


class Video:
    def __init__(self,link):
        video = ytdl.extract_info(link, download= False)
        video_format = video['formats'][0]
        self.url = video['webpage_url']
        self.stream_url = video_format["url"]


def play_song(client, song):
    source = discord.PCMVolumeTransformer(discord.FFmpegPCMAudio(song.stream_url))
    client.play(source)
    
@bot.command()
async def join(ctx):
    channel = ctx.author.voice.channel
    print(channel)
    await channel.connect()


        
@bot.command()
async def play(ctx,url):
    if not ctx.voice_client:
        client = ctx.voice_client
        channel = ctx.author.voice.channel
        video = Video(url)
        #musics[ctx.guild] = []
        client = await channel.connect()
        await ctx.send(f"je lance : {video.url}")
        play_song(client,video)

    elif ctx.voice_client:
        client = ctx.voice_client
        if not client.is_playing():
            video = Video(url)
            #musics[ctx.guild] = []
            await ctx.send(f"je lance : {video.url}")
            play_song(client,video)
        if client.is_playing:
            queue.append(url)
            #await ctx.send(queue[0])
            


@bot.command()
async def resume(ctx):
    voice_client = ctx.message.guild.voice_client

    if voice_client.is_paused():
        await voice_client.resume()
    else:
        await ctx.send("resume")

@bot.command()
async def pause(ctx):
    voice_client = ctx.message.guild.voice_client

    if voice_client.is_playing():
        await voice_client.pause()
    else:
        await ctx.send("pause")


@bot.command()
async def leave(ctx):
  player = ctx.message.guild.voice_client
  await player.disconnect()


#commande qui permet d'afficher la meteo demander

api_key_meteo = "9c561e1b44c135e7bb53f3d8e4fb69ca"
base_url = "http://api.openweathermap.org/data/2.5/weather?"


@bot.command()
async def meteo(ctx, arg):

    city_name = arg

    complete_url = base_url + "appid=" + api_key_meteo + "&q=" + city_name

    response = requests.get(complete_url)

    x = response.json()

    if x["cod"] != "404":

        y = x["main"]

        current_temperature = y["temp"]
        current_temperature = (current_temperature - 273, 15)
        current_pressure = y["pressure"]

        current_humidity = y["humidity"]

        z = x["weather"]

        weather_description = z[0]["description"]

        img = "-"

        if weather_description == "clear sky":
            img = "https://www.lejournaltoulousain.fr/wp-content/uploads/2019/09/meteo_ciel_bleu-%C2%A9-CC.jpg"

        elif weather_description == "broken clouds":
            img = "https://images.freeimages.com/images/large-previews/e83/broken-clouds-1537880.jpg"

        elif weather_description == "few clouds":
            img = "https://img.myloview.fr/images/blue-sky-with-a-few-clouds-background-400-220226288.jpg"

        elif weather_description == "scattered clouds":
            img = "https://live.staticflickr.com/2106/1909487867_de140c7eb8_b.jpg"

        elif weather_description == "overcast clouds":
            img = "https://s3.envato.com/files/135987809/Image%20Preview.jpg"

        elif weather_description == "fog":
            img = "https://www.vmcdn.ca/f/files/shared/stock-images/weather_fog_notext.jpg;w=960"

        elif weather_description == "light rain":
            img = "https://www.daily-sun.com/assets/news_images/2021/12/22/rain-in-doha.jpg"

        elif weather_description == "moderate rain":
            img = "https://www.daily-sun.com/assets/news_images/2021/12/22/rain-in-doha.jpg"

        elif weather_description == "light intensity shower rain":
            img = "https://cdn-wordpress-info.futurelearn.com/info/wp-content/uploads/8b6b0616-b3f7-42df-9395-db9ed9afa034-768x372.jpg"

        await ctx.channel.send(str(img) +
                               "\n Temperature= " +
                               str(current_temperature) +
                               "\n Pression atmoshperique (en hPa) = " +
                               str(current_pressure) +
                               "\n Humidité (en pourcentage) = " +
                               str(current_humidity) +
                               "\n Description = " +
                               str(weather_description))

    else:
        await ctx.channel.send("Je n'ai pas trouvé ta ville")




bot.run(TOKEN)




