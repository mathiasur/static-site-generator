from textnode import TextNode, TextType
from htmlnode import *
from leafnode import *
from parentnode import *
from utils import *
import re


def main():

    node = TextNode("asdasdadasdsa", TextType.IMAGE, "image.jpg")
    node2 = text_node_to_html_node(node)
    
    print(node2.to_html())


if __name__ == "__main__":
    main()
