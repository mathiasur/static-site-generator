from textnode import TextNode, TextType
from htmlnode import *
from leafnode import *
from parentnode import *
from utils import *


def main():
    

    
    node = TextNode("This is text with a `code asd block` word", TextType.TEXT)
    new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
    
    print(new_nodes)

main()
