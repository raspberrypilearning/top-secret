## Skapa en webbsida

<div style="display: flex; flex-wrap: wrap">
<div style="flex-basis: 200px; flex-grow: 1; margin-right: 15px;">
I det här steget skapar du en webbsida som webbservern, som körs på din Raspberry Pi Pico W, kan skicka till en klientwebbläsare. Du ska dock testa webbsidan på din dator först, för att se till att den visas som den ska. I nästa steg kan du lägga till koden i ditt Python-skript, så att din Raspberry Pi Pico W kan leverera webbsidan.
</div>
<div>
![Skärmdump från Chrome som visar en webbsida med två knappar för att tända och släcka en lysdiod, och lite text.](images/index.png)
</div>
</div>

En webbsida kan vara så enkel som lite text, formaterad på ett sådant sätt att en webbläsare renderar den och ger viss interaktivitet. Även om Thonny inte är designad för att skriva HTML, kan den användas för detta ändamål. Du kan dock använda din favorit-textredigerare om du vill, vare sig det är VSCode, TextEdit eller Notepad.

--- task ---

Skapa en ny fil i din textredigerare eller i Thonny. Du kan kalla det vad du vill, men `index.html` är standardnamnet för den första sidan som en användare interagerar med. Se till att du lägger till filtillägget `.html`. Om du använder Thonny, se till att spara till **This computer**.

--- /task ---

--- task ---

Det finns en del standard HTML-kod som du måste inkludera till att börja med.

--- code ---
---
language: html
filename: index.html
line_numbers: true
line_number_start: 
line_highlights: 
---
<!DOCTYPE html>
<html>
<body>
</body>
</html>

--- /code ---

--- /task ---

--- task ---

Därefter kan du skapa en knapp som kommer att användas för att slå på eller av den inbyggda lysdioden.

--- code ---
---
language: html
filename: index.html
line_numbers: true
line_number_start: 
line_highlights: 4-6
---
<!DOCTYPE html>
<html>
<body>
<form action="./lighton">
<input type="submit" value="Light on" />
</form>
</body>
</html>

--- /code ---

--- /task ---

--- task ---

Spara din fil och hitta den sedan i din filhanterare. När du dubbelklickar på filen bör den öppnas i din standardwebbläsare. Så här ser webbsidan ut i Google Chrome.

![Google Chrome visar en sida med en enda knapp märkt Light on.](images/button.png)

--- /task ---

--- task ---

Lägg till en andra knapp för att stänga av lysdioden.

--- code ---
---
language: html
filename: index.html
line_numbers: true
line_number_start: 
line_highlights: 7-9
---
<!DOCTYPE html>
<html>
<body>
<form action="./lighton">
<input type="submit" value="Light on" />
</form>
<form action="./lightoff">
<input type="submit" value="Light off" />
</form>
</body>
</html>

--- /code ---

--- /task ---

--- task ---

För att avsluta webbsidan kan du lägga till lite extra data, såsom status för lysdioden och temperaturen på din Raspberry Pi Pico W.

--- code ---
---
language: html
filename: index.html
line_numbers: true
line_number_start: 
line_highlights: 10-11
---
<!DOCTYPE html>
<html>
<body>
<form action="./lighton">
<input type="submit" value="Light on" />
</form>
<form action="./lightoff">
<input type="submit" value="Light off" />
</form>
<p>LED is {state}</p>
<p>Temperature is {temperature}</p>
</body>
</html>

--- /code ---

Din webbsida bör se ut så här:

![Webbsida i Google Chrome som visar två knappar och text som visar lysdiodens status och Picos temperatur.](images/button_and_state.png)

--- /task ---

Nu när du har en fungerande webbsida kan du lägga till den här koden i ditt Python-skript. Du måste byta tillbaka till din Python-kod i Thonny först.

--- task ---

Skapa en ny funktion som heter `webpage`, som har två parametrar. Dessa är `temperatur` och `state`.

--- code ---
---
language: python
filename: web_server.py
line_numbers: true
line_number_start: 34
line_highlights: 
---
def webpage(temperature, state):
    #Template HTML
--- /code ---

--- /task ---

--- task ---

Du kan nu lagra all din HTML-kod som du har skrivit och testat i en variabel. Att använda **fstrings** för texten innebär att platshållarna du har i HTML-koden för `temperatur` och `tillstånd` kan infogas i din sträng.

--- code ---
---
language: python
filename: web_server.py
line_numbers: true
line_number_start: 34
line_highlights: 36-49
---
def webpage(temperature, state):
    #Template HTML
    html = f"""
            <!DOCTYPE html>
            <html>
            <form action="./lighton">
            <input type="submit" value="Light on" />
            </form>
            <form action="./lightoff">
            <input type="submit" value="Light off" />
            </form>
            <p>LED is {state}</p>
            <p>Temperature is {temperature}</p>
            </body>
            </html>
            """
--- /code ---

--- /task ---

--- task ---

Slutligen kan du returnera `html`-strängen från din funktion.

--- code ---
---
language: python
filename: web_server.py
line_numbers: true
line_number_start: 34
line_highlights: 50
---
def webpage(temperature, state):
    #Template HTML
    html = f"""
            <!DOCTYPE html>
            <html>
            <form action="./lighton">
            <input type="submit" value="Light on" />
            </form>
            <form action="./lightoff">
            <input type="submit" value="Light off" />
            </form>
            <p>LED is {state}</p>
            <p>Temperature is {temperature}</p>
            </body>
            </html>
            """
    return str(html)
--- /code ---

--- /task ---

--- save ---

Du kan inte testa den här koden ännu, eftersom ditt program ännu inte levererar HTML. Det kommer att åtgärdas i nästa steg.

Den enkla HTML-koden du just har skrivit kommer att lagras i ditt MicroPython-skript och visas i webbläsaren på alla datorer som ansluter till den över ditt nätverk, precis som en webbsida som lagras på vilken annan server som helst i världen. En viktig skillnad är att endast enheter anslutna till ditt WiFi-nätverk kan komma åt webbsidan eller styra din Raspberry Pi Pico W. Den här sidan är en mycket enkel demonstration av vad som är möjligt. För att lära dig mer om HTML-kodning och skapa webbplatser, se några av våra andra projekt på den här webbplatsen!
