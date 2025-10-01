import unittest

from textnode import TextNode, TextType
from utils import split_nodes_delimiter

class TestNodeDelimiter(unittest.TestCase):

    def test_split_nodes_delimiter(self):
            node = TextNode("This is text with a `code block` word", TextType.TEXT)
            new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
            self.assertEqual(
                new_nodes,
                [
                    TextNode("This is text with a ", TextType.TEXT),
                    TextNode("code block", TextType.CODE),
                    TextNode(" word", TextType.TEXT),
                ],
            )
            
    def test_split_nodes_delimiter_2(self):
        node = TextNode("This is text `with` a `code block` word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        self.assertEqual(
            new_nodes,
            [
                TextNode("This is text ", TextType.TEXT),
                TextNode("with", TextType.CODE),
                TextNode(" a ", TextType.TEXT),
                TextNode("code block", TextType.CODE),
                TextNode(" word", TextType.TEXT),
            ],
        )
        
    def test_split_nodes_delimiter_3(self):
        node = TextNode("`This is text` with a code block word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        self.assertEqual(
            new_nodes,
            [
                TextNode("This is text", TextType.CODE),
                TextNode(" with a code block word", TextType.TEXT),
            ],
        )
        
    def test_split_nodes_delimiter_4(self):
        node = TextNode("`This is text` `with` a code block word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        self.assertEqual(
            new_nodes,
            [
                TextNode("This is text", TextType.CODE),
                TextNode(" ", TextType.TEXT),
                TextNode("with", TextType.CODE),
                TextNode(" a code block word", TextType.TEXT),
            ],
        )
        
    def test_split_nodes_delimiter_5(self):
        node = TextNode("`This is text with a code block word`", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        self.assertEqual(
            new_nodes,
            [
                TextNode("This is text with a code block word", TextType.CODE),
            ],
        )
        
    def test_split_nodes_delimiter_6(self):
        node1 = TextNode("`This is text` `with` a code block word", TextType.TEXT)
        node2 = TextNode("`This is another text` with a code block word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node1, node2], "`", TextType.CODE)
        self.assertEqual(
            new_nodes,
            [
                TextNode("This is text", TextType.CODE),
                TextNode(" ", TextType.TEXT),
                TextNode("with", TextType.CODE),
                TextNode(" a code block word", TextType.TEXT),
                TextNode("This is another text", TextType.CODE),
                TextNode(" with a code block word", TextType.TEXT),
            ],
        )
        
if __name__ == "__main__":
    unittest.main()
