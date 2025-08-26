import requests

# Hardcoded original wallpaper URL
original_url = "https://initiate.alphacoders.com/download/images3/1349491/jpeg"

# Set headers to mimic a browser
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36",
    "Referer": "https://wall.alphacoders.com/"  # optional, sometimes required
}

# File name to save
filename = "original_1349491.jpeg"

# Download
r = requests.get(original_url, headers=headers, stream=True)
if r.status_code == 200:
    with open(filename, "wb") as f:
        for chunk in r.iter_content(1024):
            f.write(chunk)
    print(f"Saved {filename}")
else:
    print(f"Failed to download: status code {r.status_code}")
