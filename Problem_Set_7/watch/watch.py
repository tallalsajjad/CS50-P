import re
import sys


def main():
    print(parse(input("HTML: ")))
"""<iframe width="560" height="315"
 src="https://www.youtube.com/embed/xvFZjo5PgG0"
title="YouTube video player" frameborder="0" allow="accelerometer;
 autoplay; clipboard-write; encrypted-media; gyroscope;
   picture-in-picture" allowfullscreen></iframe>"""

def parse(s):
    if re.search(r"<iframe(.)*><\/iframe>$", s, re.IGNORECASE):
        url_extract = re.search(r'(http(s)*:\/\/(www\.)*youtube\.com\/embed\/)([a-z_A-Z_0-9]+)', s,re.IGNORECASE)
        if url_extract:
            split_url = url_extract.group(4)
            return "https://youtu.be/" + split_url
        else:
            return None



if __name__ == "__main__":
    main()
