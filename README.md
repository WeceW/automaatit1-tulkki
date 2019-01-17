# automaatit1-tulkki
Tampereen yliopiston Automaatit I -kurssin (syksy 2018) harjoitustyö - Tulkki lauselogiikalle

1. Käyttäjä antaa syötteeksi lauselogiikan lauseen (proposition) φ. Lisäksi käyttäjä antaa syötteenä joko totuusarvot lauseessa φ esiintyville lausemuuttujille (propositiomuuttujille) tai tiedon, että käyttäjä tiedustelee, onko lause φ tautologia.
2. Sovellus muodostaa syötteestä eli merkkijonosta (tai merkkijonoista) lauselogiikan sanoja (token). (Leksikaaliseksi analyysiksi, lexer).  
3. Sovellus tarkistaa syötteen oikeellisuuden (parser) ja muodostaa edellisen vaiheen tokeneista lauseenjäsennyspuun (parse tree). 
4. Sovellus tulkkaa käyttäjän antamien totuusarvojen perusteella, onko lause φ tosi (tai tautologiatestipyynnön perusteella, onko se tautologia).
