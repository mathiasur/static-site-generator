from textnode import TextNode, TextType
from htmlnode import *
from leafnode import *
from parentnode import *
from utils import *


def main():
    
    node = TextNode("This is text with a `code block` word", TextType.TEXT)
    
    positions = split_nodes_delimiter([node], "`", TextType.CODE)
    
    a = [11,28]
    a.pop(0)
    a.pop(0)
    print(a)

main()
