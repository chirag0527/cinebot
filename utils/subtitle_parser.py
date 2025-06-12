import requests
import pysrt
import tempfile
from config import OPENSUB_API_KEY

def donwload_subtitle(url: str):
    HEADERS = {
    "User-Agent": "Cinebot v1.0",
    "Api-Key": OPENSUB_API_KEY
}
    response = requests.get(url, headers=HEADERS)
    with tempfile.NamedTemporaryFile(delete=False, suffix=".srt") as temp_file:
        temp_file.write(response.content)
        return temp_file.name

def parse_subtitle(subtitle_file: str):
    subtitle_file = pysrt.open(subtitle_file, encoding="utf-8")
    subs = []
    for subtitle in subtitle_file:
        subs.append({
            "index": subtitle.index,
            "start": str(subtitle.start),
            "end": str(subtitle.end),
            "text": subtitle.text
        })
    return subs

if __name__=="__main__":
    sub_file = donwload_subtitle("https://www.opensubtitles.com/download/C6DD999D450439448736816BDB279D39A76217DD403AEF57FDD1EE74B3C74BFFCBE58F89D6E71F1BD20F00BFBD7D9EF14411CBDCEC78D085788AD02BCA9DF2B7DB42EB377005A4C821C17EB6207D19196234F4BC8373700A67B79675A7B902197FAABF75E0E402B3357EEC9D49B3DD86031F3530EA5A724838914C61B61DBBCEF4E573F1C78D062FDFCC9432F3EFAE27D7B1EB43641E8E2AC3586634672DACB024D0FB1B426F824704BE64A17D4E3968D2F0A83A1F34B00FEE1FFF3F458C32F47AD56F2874DF9DEC119B3995C34A0F41F9420747D99DF2E4074C33B10B531EF8AE00846464790EF98FCE9A82F2A3E2500AA1DB5E6849DD1D3C434F8C973DD0A0FC6FC4DC11F2901BBDC47FEA8FEAAEC5F1BB6CB757B6DD1CA44E7E1286BCDAC099F296DB2D9D4E43ADB2007BFF3D151C72CB27C83355D2CD5E3D911924A97D76/subfile/Interstellar.2014.2014.1080p.BluRay.x264.YIFY.eng.srt.srt")
    print(parse_subtitle(sub_file))