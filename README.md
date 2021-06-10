# Tj-bot

A Discord bot written in Python to remind your friend serving in the Finnish military how many mornings they have left and wish them good mornings. The bot speaks Finnish.

Discord-botti, joka kertoo päivän tj-luvun ja toivottaa aamuja intissä olevalle kaverillesi.

## Komennot

Bottia käytetään antamalla sille komentoja chatin kautta. Huomaa, että botin käyttämät komennot alkavat huutomerkillä "!".

| Komento      | Selitys                     |
| ------------ | --------------------------- |
| !aamuja      | Toivottaa aamuja            |
| !tj          | Tänään jäljellä             |
| !lisätietoja | Yksityiskohtaisempaa tietoa |

## Asennusohjeet

Aloita luomalla sovellus ja siihen botti [Discordin sivuilla](https://discord.com/developers/applications). Generoi token ja ota se talteen myöhempää käyttöä varten. Valitse botille myös tarvittavat käyttöoikeudet. Ylläpitäjän (administrator) oikeuksia ei tarvita, sillä tj-bot vain lukee viestejä ja reagoi komentoihin. Lisää myös tämän sivun kautta botti omalle Discord-palvelimellesi. Oletetaan, että Git ja Python ovat asennettuina Linuxille.

```bash
# Kloonaa repositorio
$ git clone https://github.com/rvrauhala/tj-bot

# Siirry kansioon
$ cd tj-bot

# Luo virtuaaliympäristö ja aktivoi se
$ python -m venv venv
$ source venv/bin/activate

# Asenna riippuvuudet
$ pip install -r requirements.txt

# Luo .env-tiedosto ja lisää bottisi salainen token
# Korvaa {token} bottisi tokenilla, jonka saat Discordin Developer portal -sivulta
$ echo "DISCORD_TOKEN={token}" > .env

# Käynnistä botti
$ python bot.py
```