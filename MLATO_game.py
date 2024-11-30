# Author: Florie Souday 

import sys
import time

pip install playsound

fromplaysound import playsound

playsound ('deliamusique.mp3')

a = 1
b = 0.2
c = 0.08


def intro():
    print()
    print("(Vous êtes Margaret.)")
    time.sleep(a)
    print("Vous arrivez au bureau de la banque dans laquelle vous travaillez.")
    time.sleep(a)
    print("Comme à son habitude, votre chef passe à côté de vous et vous fait une remarque sur votre physique.")
    time.sleep(a)
    print("Boss : « Bonjour Margaret vous êtes-bien belle aujourd’hui.")
    time.sleep(a)
    print("Boss : « Cette jupe vous met bien en valeur, surtout vos jambes. Vous vous êtes faites belle pour moi ? »")
    time.sleep(a)
    print()
    question = '"Quel gros lourd... je vais lui répondre : " '
    for character in question:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(b)
    time.sleep(1.0)
    print()
    print()
    print()
    print("1 :  Merci Mr.Stevens, bonne journée à vous ")
    time.sleep(a)
    print()
    print("2 : Merci Mr.Stevens mais je vous prierai de ne pas transposer vos problèmes sexuels que vous avez visiblement avec votre femme sur moi. ")
    time.sleep(a)
    print()
    firstPath = input("Qu'allez-vous répondre ?  (1/2): ")
    if firstPath == '1':
        print()
        path1()
    elif firstPath == '2':
        print()
        path2()



def path1():
    print("Super, votre patron a fait sa remarque sexiste, vous pouvez avancer.")
    time.sleep(a)
    print("Après avoir faussement remercié votre patron, vous vous installez sur votre bureau et commencer à regarder la pile de documents inintéressants à traiter.")
    time.sleep(a)
    print("Et dire que vous avez fait tant d’années d’études et que vous avez travaillé sur des projets informatiques de grande ampleur.")
    time.sleep(a)
    print("Tous ça pour que de jeunes hommes fraichement diplômés, que vous avez formé en programmation, occupent les posts que vous espériez obtenir.")
    time.sleep(a)
    print("Et oui c’est ça être une femme autodidacte avec beaucoup de connaissances mais sans diplôme.")
    time.sleep(a)
    print()
    s1 = '"Il est que 9h du matin mais aucune envie de travailler...'
    for character in s1:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(b)
    print()
    print("Vous parlez à vous-même")
    print()
    s2 = "Mais tu n'es pas obligée ? Souviens-toi les esquisses de programmes et d'objets que tu as dessiné."
    for character in s2:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(c)
    print()
    s3 = "Tu as développé tant de compétences en informatique, tu peux profiter des outils que tu as au travail pour concevoir et prototyper non ?."
    for character in s3:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(c)
    print()
    s4 = "Oui, oui comme m'avait dit Grace Hopper, lorsqu'on travaillait sur l'UNIVAC  : “Oser et faire. Il est plus facile de demander le pardon après, que la permission avant. "   
    import webbrowser
    webbrowser.open('https://fr.wikipedia.org/wiki/Grace_Hopper')
    for character in s4:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(c)
    print()
    s5 = "Que dois-je faire..."
    for character in s5:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(c)
    print()
  

    time.sleep(1)
    print()
    print()
    time.sleep(a)
    print("1 : Travailler sur les fiches de paies et CV à analyser")
    time.sleep(a)
    print("2 : Commencer à élaborer le projet que vous avez en tête depuis un moment")
    time.sleep(a)
    print()
    secondPath = input("Travailler ou prototyper ? (1/2) : ")
    if secondPath == '1':
        path1_1()
    elif secondPath == '2':
        path3()


def path1_1():
    print()
    print("Vous vous mettez au travail et vous passez votre journée à trier les dossiers. À la fin de la journée, vous rentrez chez vous : encore une journée barbante de passée...")
    print()
    time.sleep(a)
    intro()


def path2():
    print("perdu : vous venez de vous faire renvoyer pour comportement offensant… vaut mieux faire profil bas la prochaine fois !")
    time.sleep(a)
    intro()
   

def path3():
    print("Pleins d’idées émergent : de surfaces haptiques sensibles, à des claviers aux touches molles et aux symboles abstraits, en passant par des interfaces laissant libre cours à l’imagination… Vous êtes lancées !")
    time.sleep(a)
    print("Votre objectif imaginer un objet permettant une interaction entre l’ordinateur et l’humain d’une nouvelle manière.")
    time.sleep(a)
    print("Pourquoi pas se concentrer sur le clavier ? Et si les touches étaient non pas associés à des lettres et chiffres mais bien à un système symbolique atypique ? Vous aimeriez bien créer de nouveaux paradigmes d'intéractions homme-machine.")
    time.sleep(a)
    s1 = '"Par quoi commencer ?'
    print()
    print()
    time.sleep(a)
    print("1 : Contacter grâce au système ARPAnet une de vos amies informaticienne pour échanger avec elle sur vos idées. ")
    time.sleep(a)
    print("2 : Vous commencez à esquisser une idée de programme et clavier sur une feuille de brouillon.")
    time.sleep(a)
    print()
    secondPath = input("Que faites-vous? (1/2) : ")
    if secondPath == '1':
        path4()
    elif secondPath == '2':
        path5()

def path4():
    print()
    print("Oups, votre patron vous as vu brancher des câbles au modem : il veut savoir à qui vous envoyer des mails et le voit s’afficher sur l’écran. Vous êtes convoquée et licenciée…")
    print()
    time.sleep(a)
    intro()

def path5():
    print()
    print("Vous imaginez une multitude symboles afin de créer un nouveau langage entre les utilisateurs et les ordinateurs.")
    time.sleep(a)
    print("Les ordinateurs sont capables de représenter les symboles humains mais si au lieu de transposer le lexique humain dans les machines, pourquoi ne pas créer de nouvelles communications ? ")
    time.sleep(a)
    print("Les langages comme le FORTRAN sont en anglais : des symboles ne pourraient-ils pas permettre une forme d’universalisation de la programmation ?")
    time.sleep(a)
    print()
    print()
    print("1: Vous voulez réfléchir à de nouveaux programmes associant des lignes de commande à des symboles spécifiques.")
    time.sleep(a)
    print("2: Concevoir des programmes associés à des circuits électroniques pour permettre des nouvelles formes d’interaction (caméras, microphone…).")
    time.sleep(a)
    thirdPath = input("Que faites-vous ? (1/2) ")
    if thirdPath == '1':
        path3_1()
    elif thirdPath == '2':
        path3_1()


def path3_1():
    print()
    print('Vous dessinez de multiples objets et vous commencez à élaborer des langages de programmation servant à associer capteurs de mouvements et ces nouveaux symboles')
    time.sleep(a)
    s1 = '"Je devrais me concentrer sur le geste de la main et son ergonomie, analyser ses muscles et nerfs."'
    for character in s1:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(c)
    print()
    print("Lewis, votre collègue administrateur de réseau de la banque, s'approche de vous. ")
    print()
    print("Une chance sur deux qu'ils viennent vous proposer un rencard pour soi disant vous parler d'un poste de cheffe informatique ")
    time.sleep(a)
    print("Vous n'y croyez plus et surtout vous voulez obtenir un poste sans dépendre de qui que ce soit.")
    time.sleep(a)
    print()
    s3 = "Lewis : «Bien le bonjour Margaret, mais tu es ravissante aujourd'hui, cette jupe te va à merveille. Tu te dévoiles petit à petit ! »"
    for character in s3:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(c)
    print()
    s4 = "« Bonjour Lewis, que me veux-tu ? »"
    for character in s4:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(c)
    print()
    s5 = "« Oh simplement discuter et visiblement tu n'es pas débordée par le travail. » "
    for character in s5:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(c)
    print("Il jette un coup d'oeil sur votre bureau et découvre vos croquis de programmes et d'objets informatiques ")
    
    s6 = "« Visiblement toi non plus, puisque tu te pavanes dans l'open space. »"
    for character in s6:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(c)
    print()
    s7 = "« Et bien je m'octroie une petite pause et je voudrais te proposer de sortir avec moi ce soir. Bien évidemment c'est toujours à propos de cette histoire de post. »"
    for character in s7:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(c)
    print()
    s8 = "« Tu ne me la feras plus Lewis, si je veux obtenir une promotion, cela ne passera par l'intermédiaire de personne. »"
    for character in s8:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(c)
    print()
    s9 = "« Oh allez ça ne te coûte rien de juste venir dîner avec moi ! Après tant de refus... Et tu sais, je pourrai aller te dénoncer au patron pour paresse. »"
    for character in s9:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(c)
    print()
    s10 = "« Tu n'oserais pas. »"
    for character in s10:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(b)
    print()
    s11 = "« Je vais me gêner. »"
    for character in s11:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(b)
        print()
    print("1: Vous cédez et acceptez le rencard.")
    time.sleep(a)
    print("2: Vous lui dites que c'est non et que vous voudriez bien avancer votre travail.")
    time.sleep(a)
    fourPath = input("Quelle décision prenez-vous ? (1/2) ")
    if fourPath == '1':
        path6()
    elif fourPath == '2':
        path3_2()
    print()
    
def path6():
    print()
    print("Votre soirée était épouvantable. Lewis n'a pas arrêté à de vous faire du pied et à vous promettre une promotion si vous rentrez chez lui après. Vous lui jetez le vin sur son visage et vous partez. Vous rentrez chez vous en colère.")
    print()
    time.sleep(a)
    intro()

def path3_2():
    print()
    print('Vous refusez de sortir avec lui.')
    time.sleep(a)
    s1 = '  "Margaret : « Je prefère avancer mon travail ce soir, car comme tu viens de le relever, je ne fais rien et donc il faut que je finisse mon travail. "'
    for character in s1:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(c)
    print()
    s2 = '  " Lewis : « Mmm, très bien... »"'
    for character in s2:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(c)
    print()
    time.sleep(a)
    print("Bon il est parti je peux m'y remettre.")
    time.sleep(a)
    print("Je devrai contacter Delia Derbyshire. Ses compétences en compositions musicales electroniques pourraient m'aider à mieux comprendre certains circuits.")
    import webbrowser
    webbrowser.open('https://fr.wikipedia.org/wiki/Delia_Derbyshire')
    time.sleep(a)
    print("Je le ferai demain, je vais me remettre à esquisser des idées.")
    time.sleep(a)
    print("Si au lieu d'avoir des claviers rectangulaires, ne pourrait-on pas faire des claviers anthropomorphiques ? Ça serait intéressant d'avoir des claviers mains ou des formes molles pour avoir plus de confort lorsque l'on tape. Il faudrait que j'approfondisse les questions ergonomiques. ")
    time.sleep(a)
    print("Faudrait que je demande à Roberta Williams aussi plus d'informations sur son jeu interactif en programmation, «Mystery Hoouse». Élaborer un jeu dans lequel les personnes interagissent avec l'ordinateur, pourrait aider à faire comprendre les enjeux liées à l'informatique et à mieux expliquer mon projet. ")
    import webbrowser
    webbrowser.open('https://fr.wikipedia.org/wiki/Roberta_Williams')
    time.sleep(a)
    print("Il faut vraiment que je propose des alternatives et que j'aide les individus à réfléchir sur comment l'ordinateur pourrait évoluer. Je n'ai pas envie que l'ordinateur sur lequel je travaille actuellement devienne la norme. Je pense qu'il y a plusieurs manières d'intéragir avec ces ordinateurs.  ")
    time.sleep(a)
    print("...")
    time.sleep(a)
    print("...")
    time.sleep(a)
    print("...")
    time.sleep(a)
    print("...")
    time.sleep(a)
    print("...")
    time.sleep(a)
    print("Il est déjà 17h !!! La journée est passée si vite...")
    time.sleep(a)
    print("Boss : « Alors Margaret, vous avez bien fini d'étudier les CV ? Prenez 4 candidats et donnez moi leur informations. »")
    time.sleep(a)
    print("Margaret : « Il y a 180 CV... Je n'ai pas tout finir aujourd'hui car je dois en plus finir de vérifier les fiches de paies et... »")
    time.sleep(a)
    print("Boss : « Pas besoin d'entendre vos excuses, vous avez paressé et c'est tout. Faites attention Margaret, vous n'êtes pas indispensable à l'entreprise. Un profil comme le vôtre est facilement trouvable. »")
    time.sleep(a)
    print("Margaret : « Mais c'était tout bonnement impossible de finir toutes ces tâches en une seule journée... »")
    time.sleep(a)
    print("Boss : « Ne mentez pas, je vous ai vu discuter et flirter avec Lewis. Au lieu d'aguicher vos collègues et de les pertrurber, travaillez sinon ça sera des CV pour votre poste que vous devrez analyser. »")
    time.sleep(a)
    print()
    print("Vous ne faites rien car vous savez que votre travail est en jeu... Vous rentrez chez vous, vous finissez votre bouteille de vin rouge de la veille avant de vous endormir devant Deux flics à Miami. »")
    time.sleep(a)
    print()
  


# Main Function ###

print()
print()
print()                                                    
print("            uod8BBBBBBBBBBBBBBBBRPFT?l!i  ") 
print("         =m8BBBBBBBBBBBBBBBRPFT?!||||||||||||||  ")
print("         !...:!TVBBBRPFT||||||||||!!^^""'  ||||  ")
print("        !.......:!?|||||!!^^""'             ||||   ")
print("         !.........||||                      ||||  ")
print("         !.........||||    MARGARET'S LIFE   ||||  ")
print("         !.........||||        AT THE        ||||  ")
print("         !.........||||        OFFICE         ||||  ")
print("         !.........||||                      ||||  ")
print("         !.........||||                     ||||  ")
print("         `.........||||                   ,||||  ")
print("          .;.......||||               _.-!!|||||  ")
print("print(uodWBBBBb.....||||       _.-!!|||||||||!:' ")
print("!YBBBBBBBBBBBBBBb..!|||:..-!!|||||||!iof68BBBBBb....  ")
print("!..YBBBBBBBBBBBBBBb!!||||||||!iof68BBBBBBRPFT?!::   `.  ")
print("!....YBBBBBBBBBBBBBBbaaitf68BBBBBBRPFT?!:::::::::     `.  ")
print("!   ....YBBBBBBBBBBBBBBbaaitf68BBBBBBRPFT?!:::::::::     `.  ")
print("!     ....YBBBBBBBBBBBBBBbaaitf68BBBBBBRPFT?!:::::::::     `.  ")
print()
print()  
print("Florie Souday, 2023 ©")
print("Musique : Bach Air Extended par Delia Derbyshire, musicienne et compositrice britannique de musique concrète et musique électronique, 1971")
print()  
print()
print()
time.sleep(a)
print("Nous sommes en 1980.")
time.sleep(a)
print("Margaret est secrétaire d’une banque depuis plus de deux ans.")
time.sleep(a)
print("Elle a participé à la conception des ordinateurs UNIVAC I et l’IBM 650.")
time.sleep(a)
print("Ces ordinateurs servaient à exécuter des tâches administratives simples et a opérer des centaines multiplications par seconde.")
time.sleep(a)
startGame = input("Voulez-vous commencer le jeu ?(Oui (entrez O) /Non (entrez N) ): ")
if startGame == "n" or startGame == "N":
    print("Une prochaine fois")
    time.sleep(3)
elif startGame == "o" or startGame == "O":
    intro()
