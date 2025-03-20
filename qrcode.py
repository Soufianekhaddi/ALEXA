import segno

vcard_data = """BEGIN:VCARD
VERSION:3.0
FN:KHADDI SOUFIANE
N:KHADDI;SOUFIANE;;;
TITLE:CYBER SECURITY Engineer
ORG:EMSI (Ecole Marocaine des Sciences de l'Ingenieur)
ROLE:Étudiant en Cybersécurité
TEL;TYPE=CELL:+2120771709584
EMAIL;TYPE=WORK:Sfnkhaddi@gmail.com
URL;TYPE=LINKEDIN:https://www.linkedin.com/in/soufiane-khaddi/
ADR;TYPE=WORK:;;OULFA AZHARI;CASABLANCA;;;MAROC
END:VCARD"""

qrcode = segno.make_qr(vcard_data)


qrcode.save(
    "YASSINE.png",
    scale=3,
)