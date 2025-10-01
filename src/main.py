from textnode import TextNode, TextType
from htmlnode import *
from leafnode import *
from parentnode import *
from utils import *
import re


def main():

    text = "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)"
    print(extract_markdown_links(text))
# [("to boot dev", "https://www.boot.dev"), ("to youtube", "https://www.youtube.com/@bootdotdev")]


if __name__ == "__main__":
    main()
