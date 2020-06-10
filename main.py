import dontreadme
import random
import discord

client = discord.Client()
msg_id = None
msg_user = None


@client.event
async def on_ready():
    await client.change_presence(activity=discord.Game(name='E! help│Que o universo abençoe o meu caro Mestre Yoda.'))
    print('ENZOTRON OPERANDO!')
    print(client.user.name)
    print(client.user.id)
    print('-----------------')

@client.event
async def on_message(message):
    if message.content == 'E! moeda':
        v1 = random.randint(1, 2)
        if v1 == 1:
            await message.channel.send('Cara!')
        if v1 == 2:
            await message.channel.send('Coroa!')
    if message.content == ('E!'):
        await message.channel.send('Enzotron v0.4 BOT ativo e operante!')
    if message.content == ('Enzo é corno'):
        await message.add_reaction('😡')
        v2 = random.randint(1, 3)
        if v2 == 1:
            await message.channel.send('Corno é você! Seu viadinho.')
        if v2 == 2:
            await message.channel.send('Cala a boca, gay!:rage::rage::rage:')
        if v2 == 3:
            await message.channel.send('Eu vou chorar assim..:sob::sob:')
    if message.content == ('E! esqueleto'):
        v6 = random.randint(1, 3)
        if v6 == 1:
            await message.channel.send('OTAKU FEDIDO', file=discord.File('esqueleto.gif'))
        if v6 == 2:
            await message.channel.send('MORRAAAAA!!!', file=discord.File('esqueleto2.gif'))
        if v6 == 3:
            await message.channel.send('BWAHAHAHAHA!!', file=discord.File('esqueleto3.gif'))
    if message.content.startswith('E! roll'):
        v3 = message.content.split( )
        v12 = int(v3[2])
        v13 = random.randint(1, v12)
        await message.channel.send(f':game_die:{v13}')
    if message.content == ('E! help'):
        await message.channel.send(20 * '=+=')
        await message.channel.send('COMANDOS ÚTEIS DO ENZOTRON v0.3.5 \n E! roll (n° de lados) --> Joga um dado \n E! moeda --> Cara ou coroa \n E! bebida --> Para encher a cara \n E! esqueleto --> Um GIF divertido de ódio à Otakus \n E! arte --> Para apreciar uma bela obra \n Emath+ (n°1) (n°2) --> Para somar dois números \n Emath- (n°1) (n°2) --> Para fazer uma subtração \n E! gandalf --> Para se divertir com um fantástico GIF \n E! hey --> Para dar um oi ao Enzotron')
        await message.channel.send(20 * '=+=')
    if message.content == ('E! bebida'):
        v4 = random.randint(1, 2)
        if v4 == 1:
            await message.channel.send('Eu não posso beber...')
            v5 = random.randint(1, 2)
            if v5 == 1:
                await message.channel.send('Então não vou te dar nada!')
            if v5 == 2:
                await message.channel.send('Mas aqui está! :beer::beer: ')
        if v4 == 2:
            await message.channel.send('Toma aqui! :beer:')
            v5 = random.randint(1, 2)
            if v5 == 1:
                await message.channel.send('Mas não exagere...')
            if v5 == 2:
                await message.channel.send('Seu bêbado de merda!')
    if message.content == ('E! arte'):
        v7 = random.randint(1, 3)
        if v7 == 1:
            await message.channel.send(':regional_indicator_c: :regional_indicator_u:')
        if v7 == 2:
            await message.channel.send(':regional_indicator_b: :regional_indicator_u: :regional_indicator_c: :regional_indicator_e: :regional_indicator_t: :regional_indicator_a:')
        if v7 == 3:
            await message.channel.send(':regional_indicator_p: :regional_indicator_a: :regional_indicator_u:')
    if message.content.startswith('Emath+'):
        n1 = message.content.split( )
        n2 = float(n1[1])
        n3 = float(n1[2])
        await message.channel.send(f'A soma de {n2} e {n3} é {n2+n3}')
    if message.content.startswith('Emath-'):
        n4 = message.content.split( )
        n5 = float(n4[1])
        n6 = float(n4[2])
        await message.channel.send(f'{n5} menos {n6} é {n5-n6}')
    if message.content == ('E! gandalf'):
        await message.channel.send('PAN PANANANA PAN PANANANA PAN PA PAN PA PAN', file=discord.File('gandalf.gif'))
    if message.content == ('E!aster 1'):
        await message.channel.send(':regional_indicator_h: :regional_indicator_e: :regional_indicator_n: :regional_indicator_r: :regional_indicator_i: :regional_indicator_q: :regional_indicator_u: :regional_indicator_e:   :regional_indicator_m: :regional_indicator_e:   :regional_indicator_d: :regional_indicator_e:   :regional_indicator_s: :regional_indicator_e: :regional_indicator_m: :regional_indicator_e: :regional_indicator_n: :regional_indicator_t: :regional_indicator_e: :regional_indicator_s:    :regional_indicator_d: :regional_indicator_e:   :regional_indicator_c: :regional_indicator_a: :regional_indicator_c: :regional_indicator_a: :regional_indicator_u:')
    if message.content.startswith('E! hey'):
        channel = message.channel
        await channel.send('Diga oi!')

        def check(m):
            return m.content == 'oi' and m.channel == channel

        msg = await client.wait_for('message', check=check)
        await channel.send('OLÁ, {.author}!'.format(msg))
client.run(dontreadme.token)
