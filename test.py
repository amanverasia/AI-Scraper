import newspaper
import newspaper.cli

newspaper.cli

article = newspaper.article('https://flare.io/')

print(article.authors)
# ['Hannah Brewitt', 'Minute Read', 'Published', 'Am Edt', 'Sun October']

print(article.publish_date)
# 2023-10-29 09:00:15.717000+00:00

print(article.text)
# New England Patriots head coach Bill Belichick, right, embraces Buffalo Bills head coach Sean McDermott ...

print(article.top_image)
# https://media.cnn.com/api/v1/images/stellar/prod/231015223702-06-nfl-season-gallery-1015.jpg?c=16x9&q=w_800,c_fill

print(article.movies)
# []

article.nlp()
print(article.keywords)
# ['broncos', 'game', 'et', 'wide', 'chiefs', 'mahomes', 'patrick', 'denver', 'nfl', 'stadium', 'week', 'quarterback', 'win', 'history', 'images']

print(article.summary)
# Kevin Sabitus/Getty Images Denver Broncos running back Javonte Williams evades Green Bay Packers safety Darnell Savage, bottom.
# Kathryn Riley/Getty Images Kansas City Chiefs quarterback Patrick Mahomes calls a play during the Chiefs' 19-8 Thursday Night Football win over the Denver Broncos on October 12.
# Paul Sancya/AP New York Jets running back Breece Hall carries the ball during a game against the Denver Broncos.
# The Broncos have not beaten the Chiefs since 2015, and have never beaten Chiefs quarterback Patrick Mahomes.
# Australia: NFL+, ESPN, 7Plus Brazil: NFL+, ESPN Canada: NFL+, CTV, TSN, RDS Germany: NFL+, ProSieben MAXX, DAZN Mexico: NFL+, TUDN, ESPN, Fox Sports, Sky Sports UK: NFL+, Sky Sports, ITV, Channel 5 US: NFL+, CBS, NBC, FOX, ESPN, Amazon Prime
