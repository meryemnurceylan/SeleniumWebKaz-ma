import json
from selenium import webdriver
import json
import time

driver_path = "C:\Program Files (x86)\chromedriver.exe"
browser = webdriver.Chrome(driver_path)

browser.get("https://www.8notes.com/piano/classical/sheet_music/")

with open("yeniDosya.py", "a") as f:
    f.write("Cekilen Veriler \n\n")

for j in range(1,21):


    sarki_sarkici_adi = browser.find_element("xpath", " // *[ @ id = \"centercontent\"] / div[2] / table / tbody / tr[" + str(j) + "]")
    y = sarki_sarkici_adi.text
    k =json.dumps(y)

    with open("yeniDosya.py", "a") as f:
        f.write(f"Sarki ve sarkicinin adi: " + k)

    tikla = browser.find_element("xpath","//*[@id=\"centercontent\"]/div[2]/table/tbody/tr[" + str(j) + "]")
    tikla.click()

    portre= browser.find_element("xpath","//*[@id=\"score\"]")
    z = portre.get_attribute('src')
    portre_json = json.dumps(z)

    with open("yeniDosya.py", "a") as f:
        f.write(f"\nPortre resminin indirme bagintisi: " + portre_json)

    midi = browser.find_element("xpath","// *[ @ id = \"midi_container\"] / div / div / ul / li[3] / a")
    x = midi.get_attribute('href')
    midi_json = json.dumps(x)

    with open("yeniDosya.py", "a") as f:
        f.write(f"\nMidi indirme bagintisi: " + midi_json)

    about=browser.find_element("xpath","// *[ @ id = \"infobox\"]")
    t = about.text
    about_json = json.dumps(t)

    with open("yeniDosya.py", "a") as f:
            f.write(f"\nHakkinda: " + about_json)

    dif = browser.find_element("xpath","//*[@id=\"infobox\"]/table[2]/tbody/tr[8]/td[2]")
    w = dif.text
    dif_json = json.dumps(w)

    with open("yeniDosya.py", "a") as f:
            f.write(f"\nZorluluk Hk: " + dif_json)
            f.write(f"\n\n")

    browser.execute_script("window.history.go(-1)")
    j = j + 1

