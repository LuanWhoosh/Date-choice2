define g = Character("[name]", color="#fb10a1")
define j = Character('John', color="#b41b0d")
define m = Character('Michael Fassbender', color="#e97e14")
define o = Character('Optimus Prime', color="#1454df")
define t = Character('Megatron', color="#9f14df")


label start:

    scene portada fondo
    python:
        name = renpy.input("Escribe tu nombre")

        name = name.strip() or "Catelyn"



    "Eres una persona que se ha sentido sola mucho tiempo, así que intentas algo nuevo registrándote en una app de citas."

    "Has conocido gente nueva y te han llamado la atención, pero hay dos principales: "

    "John y Optimus prime, con quienes has platicado mucho y tienen una muy buena química contigo."

    "Intentas probar suerte con alguno de los dos; sin embargo, la cosa se complica cuando ambos te invitan a salir el mismo día."

    "Por lo que, debes decidir con quien te gustaría tener una cita."

    scene bg fon1
    show eleccion

    g "Hmmm Yo elijo a:..."

menu:

    "John Wick":
        jump jw

    "Optimus prime":
        jump op

label op:

    scene bg fon 
    show optimus perfil

    "Has elegido a Optimus, parece ser un nombre extranjero, te ha llamado la atención su secretismo,"

    "pues nunca lo has visto ni en fotos, pero es capaz de inspirar una confianza y determinación que te atrapa."

    "Su plan es llevarte a pasear, pero no sabes realmente que pueda suceder en la cita."
    
    hide optimus perfil
    scene bg cosmeticos
    
    
    "¡Llegó la hora de arreglarte!, él vendrá a recogerte pronto, te maquillas y peinas como mejor puedes, quieres lucir lo más deslumbrante posible..."

    scene bg cama 
    show ambos vestidos

    "...pero no sabes elegir si ponerte tu vestido corto rojo, o tu vestido largo negro, ambos lucen hermosos."
    

menu:

    "Vestido rojo...":

        hide ambos vestidos 
        show vestido rojo

        "Pero hay algo en ese rojo que te termina de convencer..."

        jump dateop
    
    "Vestido negro...":

        hide ambos vestidos 
        show vestido negro

        "Pero el negro es un clásico que siempre luce bien..."

        jump dateop

label dateop:
    
    
    "Se escucha el timbre, !ha llegado!"

    hide vestido rojo
    hide vestido negro 
    scene bg portico
    show optimus trailer

    "Y al abrir la puerta encuentras... ¿un trailer?"

    g "Nunca mencionó ser trailero..."

    show optimus prime

    g "¿QUÉ CARAJO?"


    o "Necesito tu ayuda para encontrar la chispa suprema"

    "Intentas procesar lo que acaba de pasar..." 

    hide optimus prime

    show optimus robot: 
        xalign 0.0
        yalign 1.0
    
    show megatron tanque
    
    "...cuando de repente llega lo que parece ser un tanque alienígena, que de igual manera se transforma en un robot gigante."

    hide megatron tanque

    show megatron robot 

    t "¡VAS A CAER PRIME!"

    o "¡NUNCA, MEGATRON!"

    $ renpy.movie_cutscene("creditos.webm")

    return

label jw:

    "Has elegido a John, es una persona muy tranquila y seria, también es nuevo en las apps de citas, sentía que era tiempo de darse un nuevo aire y conocer a alguien."

    "John te manda mensaje para ponerse de acuerdo sobre la cena, tiene pensado salir a pasear contigo y llevarte a cenar a un restaurante..."

    "...pero en tu picardía se te mete la idea de que, tal vez puedan pasar una linda velada en tu casa, a lo cual no sabes qué decidir."

menu:
    "Restaurante":
        jump restaurantejw

    "Velada en tu casa":
        jump casag

label casag:

    "Decides arriesgarte, e invitarlo a pasar la cita en tu casa, a lo que acepta con gusto. Esto te hará sentir cómoda, es tu zona de confort."

    "Además, es bueno dejar una buena primera impresión como anfitrión, así como sorprenderlo preparándole algo."

    "Decides prepararle algo especial hecho por ti misma, pero no sabes decidir si..."

menu:
    "Pollo a la naranja":
        jump pollo
    "Pasta italiana":
        jump pasta

label pollo:

    "Decides preparar un delicioso pollo a la naranja, pero esto llevara más tiempo de lo esperado, por lo que... "

    "...le pides a john que llegue más tarde de lo que habían acordado, a lo que accede sin problemas."

    "Es hora de preparar la comida, la cual haces con mucho esmero, quieres que sea especial y que lo note con solo probarlo."

    "Timelapse epico"

    jump jwplanta

label pasta:

    "Decides hacerle una rica pasta italiana, un rissoto será perfecto, pero esto llevara más tiempo de lo esperado, por lo que... "

    "...le pides a john que llegue más tarde de lo que habían acordado, a lo que accede sin problemas."

    "Es hora de preparar la comida, la cual haces con mucho esmero, quieres que sea especial y que lo note con solo probarlo."

    "Timelapse epico"

    jump jwplanta

label jwplanta:

    "Ya casi es hora de que llegue John, cuando de repente suena una notificación en tu celular, es él."

    j "Lo lamento demasiado, pero no voy a poder verte hoy, acabo de tener un incidente y es de extrema urgencia que lo atienda, espero puedas comprender."

    g "Carajo, debí haber invitado al extranjero"

    return


label restaurantejw:

    "Llegó la hora de arreglarte, él vendrá a recogerte pronto, te maquillas y peinas como mejor puedes, quieres lucir lo más deslumbrante posible."

    "Pero no sabes elegir si ponerte tu vestido corto rojo, o tu vestido largo negro, ambos lucen hermosos..."

menu: 
    "Pero hay algo en ese rojo que te termina de convencer.":
        jump meetjw
    
    "Pero el negro es un clásico que siempre luce bien.":
        jump meetjw

label meetjw:

    "Se escucha el timbre, !ha llegado!"

    j "Hola, ¿cómo te va? que gusto conocerte en persona, soy John."

    j "Espero que te gusten, quería traerte un detalle."

    j "Wow, luces espectacular con ese vestido. ¿Estás lista?"

    g "Mhhh... si"

    j "Este lugar te va a encantar, sirven una pasta deliciosa"

    g "..."

    j "Te ves algo nerviosa, te entiendo, esta es mi primera cita en años, así que, relájate y disfrutemos de la noche ¿vale?"

    "Asientes timidamente con una sonrisa furtiva"

    j "Ordena lo que gustes, todo es muy rico aquí."

    j "Yo te recomendaría el rissotto, era el favorito de mi esposa."

    "El ambiente de repente cambia, y se torna un poco tenso, esto es algo que no te había comentado antes,"

    "¿Estuvo casado? ¿No cree que sea un detalle importante que debió decir?"

    "Es aquí donde te surge un dilema, ¿deberías de seguir en la cita?"

    "Si ya mintió sobre una esposa, qué te asegura que no te ha mentido sobre otras cosas."

menu: 
    "No me siento cómoda sabiendo el hecho de que existe una esposa":

        jump pauto

    "¿Esposa? ¿Estás casado? Tienes curiosidad sobre el tema":

        jump citajw

label pauto:

    g "Oye, de verdad lo siento, pero, no me siento cómoda sabiendo el hecho de que existe una esposa..."
    
    g "...y no sé sobre qué más me has mentido u ocultado, creo que, por esta ocasión, lo mejor sea que regrese a casa."

    j "Yo... lo siento, es un tema complicado, pero te aseguro que no estoy casado."

    j "Sin embargo, entiendo que es algo por lo cual te sientas así, siento no haberlo mencionado antes."

    j "Si gustas terminar con la cita, lo entiendo, pero déjame llevarte a casa, segura."

    "El ambiente es un poco tenso e incómodo, no te sentías del todo bien al saber lo de la esposa, pero parece ser que hay algo que no sabes."

    g "Así que... ¿esposa?"

    j "Sí..."

    j "Lo siento, es un tema complicado, pero siento que te debo una explicación, verás..."

    j "...hace algunos años ya, estuve casado, una gran mujer; sin embargo, ella dejó este mundo."

    j "Pasó mucho tiempo hasta que finalmente me di una oportunidad para empezar de nuevo."

    j "Lamento no comentarlo antes, y también mi comentario en el restaurante, quería decírtelo de una mejor manera."

    "Metiste un poco la pata, parece que decirle inmediatamente que te ibas fue algo precipitado."

    g "Lo siento... no tenía idea."

    g "Ahora me siento como una tonta."

    j "No te preocupes, en verdad, lo entiendo."

    g "De verdad, lo siento mucho, me gustaría enmendar mi error... no me gustaría que tu primera cita quede arruinada."

    g "Te gustaría... ¿tomar unos tragos en mi casa? y tal vez ¿pedir algo para cenar?"

    j "Creo que, eso me alegraría"

    "John esboza una sonrisa, pero esta se esfuma rápidamente, como si le hubieran tirado un balde de agua fría,"

    "su expresión ahora era completamente seria, su mirada había cambiado por completo mientras miraba el retrovisor."

    j "Mierda..."

    g "¿Qué sucede?"

    j "Quiero que mantengas la calma por favor, y también quiero que sigas mis indicaciones al pie de la letra."

    j "Algo muy malo está a punto de pasar y no hay tiempo para explicaciones."

    "Es así que, con su mano derecha procede a sacar una pistola del compartimiento de su auto, en el cual tenía dos armas."

    "Todo presagiaba que la situación estaba a punto de tornarse violenta, y no puedes terminar de comprender qué pasa..."

    "...cuando se alcanza a ver como una moto en donde dos personas, igualmente armadas, se alinean con ustedes, apuntando directamente a ambos."

    "Te das cuenta de que ahora son 3 motos, una a cada lado del vehículo, mientras que la tercera se divisaba detrás del auto, estaban rodeados."

    "Y sucedió lo inevitable, ¡fuego!"

    "Los primeros en disparar fueron aquellos al costado del piloto, John se agacho a la par de ti."

    j "¡Abajo!"

    "Acataste rápidamente la orden, evitando así las balas que rompen el cristal de la puerta izquierda del auto."

    "Se escuchan varios disparos, ahora de ambos lados del auto, a lo que John responde con un volantazo..."

    "...el cual impacta de lleno con la motocicleta a su derecha, haciendo que ambos se estampen contra el pavimento."

    "Era hora del contraataque, John responde apuntando y disparando en contra de los tipos a su lado, derribando a quien se encontraba en la parte posterior..."

    "...encajando dos balas en su torso, sin embargo; el piloto logró sostenerlo por el brazo con el que sujetaba su arma."

    "Es así que la moto que venía detrás, ahora se encuentra avanzando hacia tu lado, por lo que..."

    menu: 
        "Gritas en busca de la ayuda de John.":
            jump grito
        
        "Tomas el arma que estaba en el compartimiento.":
            jump disparo

label grito:

    "John se percata de que estás en grave riesgo, por lo que, en un arriesgado movimiento, deja de sostener el volante...."

    "...para así, de un fuerte e inhumano golpe, atravesar del casco del mercenario..."

    "...acertándole un golpe directo y con una inmensa fuerza directo en la cara ..."

    "...lo que hace que caiga violentamente de la moto, y con rapidez y habilidad, ahora dispara en contra de aquellos que buscaban lastimarte..."

    "...dando una bala directa en la cabeza del conductor, haciendo que finalmente se encuentren a salvo."

    j "¿Estás bien?"

    g "Sí... eso creo ¿Qué carajo acaba de pasar?"

    j "Tal vez, hay un par de cosas más que debo contarte."

    return


label disparo:
    "...y sin pensarlo mucho, disparas en contra de tus agresores, acertando con mucha suerte,"

    "en el cuello del conductor, lo que hace que pierda el control y ambos caigan a gran velocidad."

    "John, impresionado, decide acabar con todo de una vez por todas, y con una maniobra logra quitar aquel agarre,"

    "frenando en seco haciendo incluso que el auto derrape, y con un disparo certero,"

    "logra dar en el tanque de gasolina de aquella moto que se siguió de largo, y que, al recibir aquella bala, explota."

    j "Gracias, eso fue muy valiente de tu parte"

    j "¿Estás bien?"

    g "Sí... eso creo"

    g "¿Qué mierda fue eso?"

    g "¿Por qué nos atacaron esos tipos?"

    g "¿Quién demonios eres?"

    j "Tal vez haya más cosas que necesitas saber de mí"

    return

label citajw:

    j "No, lo estuve, pero ya no, ella murió hace tiempo, esa es la razón por la que hace tiempo no tengo una cita."

    j "Siento no haberlo mencionado antes, solamente que es un tema algo sensible para mí."

    g "No... no tenía idea, lo siento."

    j "No te preocupes, entiendo que te haya desconcertado,"

    j "todo esto es nuevo para mí y a decir verdad apesto un poco para las citas"

    g "No, para nada, estoy pasándola muy bien contigo"

    j "Me alegra mucho oír eso, que te parece si cenamos"

    g "¡Claro! creo que voy a pedir..."

    menu: 
        "Risotto":
            jump contcita
        "Lasaña":
            jump contcita

    label contcita:

        g "Es lo que más me apetece"

        "John solamente responde con una gentil sonrisa, parece que será un a agradable noche"

        "La noche transcurre con amabilidad, ha sido una cita muy amena y disfrutas de su compañía, pero en cierto momento, notaste un cambio en su manera de actuar," 

        "ya no lucía tan relajado, ahora parecía estar en un estado de alerta, como si estuviera a la espera de algo porvenir, esto te alerta de igual manera."

        g "¿Todo en orden? Te noto un poco tenso"

        g "¿Te encuentras bien?"

        j "Sí, lo siento, solo recordé que, olvidé algo en el auto, ¿podrías esperarme un momento aquí?"


        menu:
            "claro, esperaré aquí":
                jump michcit
            "Tal vez podría acompañarte":
                jump michcit1
        

label michcit1:
    j "No es necesario, además, si salimos ambos parecerá que intentamos irnos sin pagar la cuenta"

    j "Solo será un momento, ¿Vale?"

    g "Tienes razón, esperaré entonces"

    jump michcit

label michcit:
    j "Vuelvo enseguida "

    "Eso logra calmar un poco la inquietud que tenías sobre él,"

    "te percatas de que ha dejado su celular sobre la mesa, así que decides guardarlo en tu bolso, por seguridad."

    "Sin embargo; apenas sale del restaurante, un hombre te aborda y se sienta en la mesa contigo."

    "En el lugar que antes era ocupado por John, es un hombre elegante y de buena apariencia,"

    "pero te extraña la confianza con la que ha decidido sentarse delante a ti."

    g "Disculpe, ese asiento está ocupado"

    m "Lo sé, pero no por mucho tiempo"

    "Esas palabras, y la frialdad de su voz, solamente logran asustarte,"

    "las cosas no están bien y parece que la actitud de John simplemente era un presagio de que esto pasaría."

    m "No pretendo quitarle mucho de su tiempo, solamente me gustaría hacerle un par de preguntas acerca de, su acompañante."

    m "Empezando con la duda ¿sabe realmente qué tipo de persona o quién es en realidad?"

    m "Porque a mi parecer, no sabe en la clase de problemas que se está metiendo y espero que sea así, que no lo sepas"

    g "Señor, me está asustando mucho"

    m "Esto será rápido"

    "De repente, escuchas disparos provenientes de fuera del restaurante, sabes que es él y está en problemas"

    "Las personas al rededor comienzan a alterarse y a gritar"

    g "¡JOHN!"

    m "Será mejor que te olvides de él ahora, ¿tienes algún tipo de información, algo que te haya dicho?"

    m "No lo sé, alguna locación, algún nombre, un número."

    "Comienza a sonar el celular de John, el cual está en tu bolsa."

    m "Incluso su celular. Asumo que será suyo, ya que el tuyo se encuentra aquí."

    m "Por qué mejor no me lo entregas y te ahorras algunos problemas."

    menu:
        "Darle el celular":
            jump Jseva1
        "Negarse":
            jump Jseva2

label Jseva1:
    "Sacas el celular de tu bolso, y se lo entregas."

    g "Toma, solo, no me lastimes por favor."

    "Recibe el celular, y lo guarda en su saco."

    m "No es necesario, gracias por cooperar, me alegra no tener que matar a alguien hoy."

    "Comienza a levantarse de la mesa para así retirarse, se pone de pie y da la media vuelta."

    "Pero apenas voltea, se escucha un sonido de disparo y cae desplomado de espalda sobre la mesa..."

    "con un agujero entre cejas, revelando así la figura de john, cubierto de sangre."

    j "¿Dónde está?"

    g "Lo... lo metió en su saco"

    "Toma el celular que aquel hombre guardó antes de morir, metiéndolo ahora en el suyo."

    j "Gracias." 

    j "Lo siento, no quería ponerte en esta situación."

    "Simplemente se retira del restaurante sin más explicación."

    return

label Jseva2:
    m "Huh, debiste haber hecho esto más fácil"

    "No le ha gustado para nada esa respuesta, puedes ver la frialdad de su mirada mientras saca una pistola de su saco, apuntándote directamente a la cara."

    m "No tenía ganas de matar a alguien hoy, pero que más remedio."

    "Mientras carga su arma, al fondo se ve una sombra que, cada vez de hace más nítida."

    "Es john, con la cara manchada por chorros de sangre, pero no la de él."

    "La expresión de aquel hombre cambia drásticamente."

    "Pasa de una confianza y arrogancia, a tener una expresión de sorpresa y miedo, de alguien que sabe lo que está a punto de pasar"

    "John se encuentra justo detrás de él, apuntándole con una pistola."

    "Sin decir una sola palabra y también, sin dejarlo decirlas, procede a darle un disparo certero en la cabeza."

    "El hombre se desploma sobre la mesa."

    j "Gracias."

    j "Lo siento, no quería ponerte en esta situación."

    "John extendió su mano con la palma abierta, dando a entender que quería de vuelta su celular, a lo cual haces caso."

    "Lo toma, y procede a irse del restaurante sin más explicación."

    return

    
