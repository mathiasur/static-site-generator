from textnode import TextNode, TextType
from htmlnode import *
from leafnode import *
from parentnode import *
from utils import *
import re


def main():

    node = TextNode("asdasdadasdsa", TextType.IMAGE, "image.jpg")
    node2 = text_node_to_html_node(node)
    
    print(extract_markdown_images("This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)"))


if __name__ == "__main__":
    main()
