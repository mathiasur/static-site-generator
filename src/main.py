from textnode import TextNode, TextType
from htmlnode import *
from leafnode import *
from parentnode import *
from utils import *


def main():
    
    node = TextNode("`This is text` `with` a code block word", TextType.TEXT)
    node2 = TextNode("`This is another text` with a code block word", TextType.TEXT)
    
    positions = split_nodes_delimiter([node, node2], "`", TextType.CODE)
    
    for position in positions:
        print(position)
    



if __name__ == "__main__":
    main()
