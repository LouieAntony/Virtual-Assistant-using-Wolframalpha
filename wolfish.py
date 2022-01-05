import wolframalpha
client = wolframalpha.Client('YU2J97-HUWHG68W7R')

while True:
    query=str(input('Query: '))
    res=client.query(query)
    output=next(res.results).text
    print(output)