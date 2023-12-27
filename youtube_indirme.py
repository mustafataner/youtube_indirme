import streamlit as st
from pytube import YouTube, Playlist
import os

st.title('YouTube Video İndirme Programı')

# Video veya playlist URL'sini al
url = st.text_input('Video veya Playlist URL girin:')

# Sadece ses dosyasını indirme seçeneği
audio_only = st.checkbox('Sadece ses dosyasını indir')

if st.button('İndir'):
    if 'playlist' in url:
        # Playlist indirme işlemi
        playlist = Playlist(url)
        for video in playlist.videos:
            if audio_only:
                audio_stream = video.streams.filter(only_audio=True).first()
                file_path = audio_stream.download()
            else:
                video_stream = video.streams.get_highest_resolution()
                file_path = video_stream.download()
        # Playlist indirildiğinde son video/audio bilgisi döndürülür
        st.success('Playlist başarıyla indirildi.')
    else:
        # Tek video indirme işlemi
        video = YouTube(url)
        if audio_only:
            audio_stream = video.streams.filter(only_audio=True).first()
            file_path = audio_stream.download()
        else:
            video_stream = video.streams.get_highest_resolution()
            file_path = video_stream.download()
        st.success('Video başarıyla indirildi.')

    # İndirilen dosya için bir indirme butonu oluştur
    if os.path.exists(file_path):
        file_name = os.path.basename(file_path)
        file_type = "video/mp4" if not audio_only else "audio/mpeg"
        with open(file_path, "rb") as file:
            st.download_button(
                    label="Dosyayı İndir",
                    data=file,
                    file_name=file_name,
                    mime=file_type
                )
    else:
        st.error('Dosya bulunamadı.')
