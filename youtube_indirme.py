
import streamlit as st
from pytube import YouTube, Playlist



st.title('YouTube Video İndirme Programı')

# Video veya playlist URL'sini al
url = st.text_input('Video veya Playlist URL girin:')

# Sadece ses dosyasını indirme seçeneği
audio_only = st.checkbox('Sadece ses dosyasını indir')

# İndirme işlemini başlatma butonu
if st.button('İndir'):
    if 'playlist' in url:
        # Playlist indirme işlemi
        playlist = Playlist(url)
        for video in playlist.videos:
            if audio_only:
                audio_stream = video.streams.filter(only_audio=True).first()
                audio_stream.download()
            else:
                video.streams.get_highest_resolution().download()
        st.success('Playlist başarıyla indirildi.')
    else:
        # Tek video indirme işlemi
        video = YouTube(url)
        if audio_only:
            audio_stream = video.streams.filter(only_audio=True).first()
            audio_stream.download()
        else:
            video.streams.get_highest_resolution().download()
        st.success('Video başarıyla indirildi.')