from htmlnode import HTMLNode


class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)

    def to_html(self):
        if not self.tag:
            raise ValueError("No tag provided")
        if not self.children:
            raise ValueError("Children is missing")
        
        children = "".join(list(map(lambda child: child.to_html(), self.children)))
        
        if not self.props:
            return f"<{self.tag}>{children}</{self.tag}>"
        return f"<{self.tag} {self.props_to_html()}>{children}</{self.tag}>"
