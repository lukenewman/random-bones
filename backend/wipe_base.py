from deta import Deta

deta = Deta("b0y2ugtg_97RSrN6cYpBN4DCK9n5Np85wKYZz4Rxh")

episodes = deta.Base("episodes")

res = episodes.fetch()
all_items = res.items

# fetch until last is 'None'
while res.last:
  res = episodes.fetch(last=res.last)
  all_items += res.items

for episode in all_items:
  episodes.delete(episode["key"])