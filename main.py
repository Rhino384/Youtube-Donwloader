import pytube

url = input('#> Digite o link do video: ')
print('Baixando...')

yt = pytube.YouTube(url)
video = yt.streams.first()
video.download()

print(f'Download concluido, qualidade max {yt.title}')