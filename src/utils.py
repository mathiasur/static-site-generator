import re
from textnode import *


def text_node_to_html_node(text_node: TextNode):
    if not isinstance(text_node.text_type, TextType):
        raise ValueError

    if text_node.text_type == TextType.IMAGE:
        return LeafNode(
            "img", " ", {"src": f"{text_node.url}", "alt": f"{text_node.text}"}
        )

    return LeafNode(text_node.text_type.value, text_node.text)


def split_node(node, delimiter, text_type):
    nodes = []
    raw = ""
    special = ""

    stack = []
    for char in node.text:
        if len(stack) == 0 and char == delimiter:
            stack.append(1)
            if raw != "":
                nodes.append(TextNode(raw, TextType.TEXT))
                raw = ""
            continue
        if len(stack) == 1 and char == delimiter:
            stack.pop()
            if special != "":
                nodes.append(TextNode(special, text_type))
                special = ""
            continue
        if len(stack) == 0:
            raw += char
        if len(stack) == 1:
            special += char

    if raw != "":
        nodes.append(TextNode(raw, TextType.TEXT))

    if len(stack) == 1:
        nodes[-1].text_type == TextType.TEXT

    return nodes


def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []

    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
        else:
            new_nodes += split_node(node, delimiter, text_type)

    return new_nodes


def extract_markdown_images(text):
    return re.findall(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)", text)


def extract_markdown_links(text):
    return re.findall(r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)", text)


def split_node_image(old_nodes):
    new_nodes = []
    
    for node in old_nodes:
        if node.text_type == TextType.IMAGE:
            new_nodes.append(node)
        else:
            image = extract_markdown_images(node.text)
            