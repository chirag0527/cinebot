import requests
import pysrt
import tempfile

def donwload_subtitle(url: str):
    response = requests.get(url)
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
    sub_file = donwload_subtitle("https://www.opensubtitles.com/download/20F20F0015424E70B13965B56E2011B4DFD90D38EC0A9943EE7594B65657ECFE70B745F3086A87156B8E5083DD6F2D33195AB63D9E8CF6AC0D6D5E71B7BD8FF07B379009B9FCB6F6AE0D6E7E33219AA2FBB11FBA9DBAC1A74B0D4FF142FCFF19545265C2BF7B3308FF0047120B5C9127352527F21B7CB251D6460A3AC87DDCB3124C5F021592A9D0D98A8F81506256609AB955B4C0041BA633D363A88BFC4B5B482D3F72ECB990C30A1922CE9AD0721FA7C7CC80D31A968D20998E96672646ACA51F12D35D7DD0B3E971E07FA1BEFA86694B7F06B30BFC28237EE608D50A1DB2FB1C78279AC31BDF43353A3B4AA072A19F203113D7A9C842208823B89D413BB315D2C5FB6A0AA7DB0B40FE847162257E7683A37DCD3A34CD7DB58EBFAAFC54E2A32AFC37B58AABF3E7B07A9E069B40D9F2092C63C8B8BA20A4D92F4C24C92C71D7C8D210B2371A86/subfile/The.Dark.Knight.2008.IMAX.1080p.BluRay.x265-YAWNTiC%20(SDH).srt")
    print(parse_subtitle(sub_file))