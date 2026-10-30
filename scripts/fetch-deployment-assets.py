"""Fetch pinned large tutorial media before publishing to GitHub Pages."""
import concurrent.futures
import hashlib
import json
import pathlib
import urllib.request

ROOT = pathlib.Path(__file__).resolve().parents[1]
ASSETS = json.loads((ROOT / 'deployment-assets.json').read_text())

def fetch(asset):
    target = ROOT / asset['path']
    if target.exists() and hashlib.sha256(target.read_bytes()).hexdigest() == asset['sha256']:
        return
    request = urllib.request.Request(asset['url'], headers={'User-Agent': 'StringTunes-Pages/1.0'})
    with urllib.request.urlopen(request, timeout=90) as response:
        data = response.read()
    if hashlib.sha256(data).hexdigest() != asset['sha256']:
        raise RuntimeError(f"Asset integrity check failed: {asset['path']}")
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_bytes(data)
    print(f"Verified {asset['path']}")

with concurrent.futures.ThreadPoolExecutor(max_workers=3) as executor:
    list(executor.map(fetch, ASSETS))
