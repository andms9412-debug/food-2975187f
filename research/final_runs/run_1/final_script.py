"""Collect public-source IG single-photo food-post layout references (Bing/DDG)."""
from playwright.sync_api import sync_playwright
import time, os
SHOTS=os.path.join(os.path.dirname(__file__),"screenshots"); os.makedirs(SHOTS,exist_ok=True)
LOG=os.path.join(os.path.dirname(__file__),"final_script_log.txt")
UA="Mozilla/5.0 (X11; Linux x86_64; rv:121.0) Gecko/20100101 Firefox/121.0"
TARGETS=[
 ("bing_en","https://www.bing.com/images/search?q=instagram+cafe+food+post+layout"),
 ("bing_zh","https://www.bing.com/images/search?q=%E7%BE%8E%E9%A3%9F+IG+%E8%B2%BC%E6%96%87+%E6%8E%92%E7%89%88+%E7%AF%84%E6%9C%AC"),
 ("ddg","https://duckduckgo.com/?q=instagram+food+post+template+single+photo&iax=images&ia=images"),
 ("pin","https://www.pinterest.com/search/pins/?q=instagram%20food%20post%20template"),
 ("bing_single","https://www.bing.com/images/search?q=minimal+aesthetic+cafe+instagram+post+single+photo+handwritten"),
]
def main():
    log=open(LOG,"w",encoding="utf-8")
    with sync_playwright() as p:
        b=p.firefox.launch(headless=True)
        ctx=b.new_context(viewport={"width":1280,"height":1800},user_agent=UA,locale="zh-TW")
        pg=ctx.new_page()
        for i,(name,url) in enumerate(TARGETS,1):
            pg.goto(url,timeout=45000,wait_until="domcontentloaded"); time.sleep(4)
            sp=f"{SHOTS}/final_execution_{i}_{name}.png"; pg.screenshot(path=sp)
            log.write(f"step {i} action: captured {name} -> {url}\n")
        b.close()
    log.write("final datum: 5 public reference grids captured; Google Images blocked (/sorry bot wall)\n")
    log.close(); print("done")
if __name__=="__main__": main()
