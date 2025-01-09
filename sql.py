import psycopg2

print("\nEstabelecendo Conexão. Informe os parametros necessarios:\n")

loop = True

while loop:

    dbname = input("Nome do Database: ")
    user = input("Nome do Usuario: ")
    password = input("Senha do Servidor: ")
    host = input("Nome do Host: ")

    try:

        conn = psycopg2.connect(
            dbname=dbname,
            user=user,
            password=password,
            host=host
        )

    except:

        print("Ocorreu algum erro ao conectar com as informacoes concebidas. Tente novamente:\n\n")

    else:

        loop = False

cur = conn.cursor()

loop = True

while loop:

    query = input("Digite seu query. Se voce for passar algum parametro, em vez de digitar o valor parametro, digite '%s' (sem as aspas):\n")

    params = query.count("%s")

    if params > 0:

        paramtuple = []
        for i in range(0,params):
            par = input(f'Passe o parametro #{i+1}: ')
            paramtuple.append(par)
        paramtuple = tuple(paramtuple)

    if params < 1:

        try:

            cur.execute(str(query))

        except:

            print("Este query nao foi processado corretamente. Tente novamente:\n")

            conn.close()

            conn = psycopg2.connect(
            dbname=dbname,
            user=user,
            password=password,
            host=host
            )

            cur = conn.cursor()

        else:

            loop = False

    else:

        try:

            cur.execute(str(query), paramtuple)

        except:

            print("Este query nao foi processado corretamente. Tente novamente:\n")

            conn.close()

            conn = psycopg2.connect(
            dbname=dbname,
            user=user,
            password=password,
            host=host
            )

            cur = conn.cursor()

        else:

            loop = False

if (str(query).lower()).startswith("select"):
    result = cur.fetchall()
else:
    conn.commit()
    result = ["Processo Completo."]

for i in result:
	print(i)

cur.close()