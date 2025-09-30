from textnode import *

def text_node_to_html_node(text_node: TextNode):
    if not isinstance(text_node.text_type, TextType):
        raise ValueError
    
    if text_node.text_type == TextType.IMAGE:
        return LeafNode("img", "", {"src": f"{text_node.url}", "alt": f"{text_node.text}"})
    
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
    tokens = []
    raw_text_types = []
    other_types = []
    
    for node in old_nodes:
        tokens += node.text.split()
    
    other = False
    
    for token in tokens:
        if token[0] == delimiter or other is True:
            other = True
            other_types.append(token)
        else:
            raw_text_types.append(token)
        if token[-1] == delimiter:
            other = False
            
    return other_types