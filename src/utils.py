from textnode import *


def text_node_to_html_node(text_node: TextNode):
    if not isinstance(text_node.text_type, TextType):
        raise ValueError

    if text_node.text_type == TextType.IMAGE:
        return LeafNode(
            "img", "", {"src": f"{text_node.url}", "alt": f"{text_node.text}"}
        )

    return LeafNode(text_node.text_type.value, text_node.text)


# node = TextNode("This is text with a `code block` word", TextType.TEXT)
# new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)

# [
#     TextNode("This is text with a ", TextType.TEXT),
#     TextNode("code block", TextType.CODE),
#     TextNode(" word", TextType.TEXT),
# ]


# seguir con esto
def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    node_values = []
    delimiter_positions = []

    for node in old_nodes:
        node_values.append(node.text)

    index = 0
    for text in node_values:
        tokens = text.split(delimiter)
        for token in tokens[:-1]:
            index += len(token)
            delimiter_positions.append(index)
            index += len(delimiter)
            
        if len(delimiter_positions) > 1:
            if len(delimiter_positions) % 2 != 0:
                delimiter_positions = delimiter_positions[:-1]
        else:
            new_nodes.append(TextNode(text, TextType.TEXT))
            continue
                
        # continuar aca
            

    return delimiter_positions


# este es un `pedazo de codigo` [11,28]
