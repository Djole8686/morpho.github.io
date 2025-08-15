
import qrcode
from qrcode.image.svg import SvgImage
from pathlib import Path

BASE_URL = "https://djole8686.github.io/morpho.github.io"
dynasties = ["romanov", "habsburg", "ottoman", "bourbon", "tudor"]
here = Path(__file__).resolve().parent
qrdir = here / "qr_codes"
qrdir.mkdir(parents=True, exist_ok=True)

for slug in dynasties:
    url = f"{BASE_URL}/{slug}.html"
    img = qrcode.make(url)
    img.save(qrdir / f"qr_{slug}.png")
    svg_img = qrcode.make(url, image_factory=SvgImage)
    with open(qrdir / f"qr_{slug}.svg", "wb") as f:
        svg_img.save(f)
print("Gotovo.")
