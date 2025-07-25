from enum import Enum
import re

from htmlnode import LeafNode

class TextType(Enum):
    TEXT = "Normal text"
    BOLD = "**Bold text**"
    ITALIC = "_Italic text_"
    CODE = "`Code text`"
    LINK = "[anchor text](url)"
    IMAGE = "![alt text](url)"

class TextNode():
    def __init__(self, text, text_type, url=None):
        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__(self, text_node_2):
        if (self.text == text_node_2.text) \
        and (self.text_type == text_node_2.text_type)\
        and (self.url == text_node_2.url):      
            return True

    def __repr__(self):            
        return f"TextNode({self.text}, {self.text_type}, {self.url})"


def text_node_to_html_node(text_node):
        
    match TextType(text_node.text_type):
        case TextType.TEXT:
            return LeafNode(tag=None,value=text_node.text)
        case TextType.BOLD:
            return LeafNode(tag='b',value=text_node.text)
        case TextType.ITALIC:
            return LeafNode(tag='i',value=text_node.text)
        case TextType.CODE:
            return LeafNode(tag='code',value=text_node.text)
        case TextType.LINK:
            return LeafNode("a", text_node.text, {"href": text_node.url})
        case TextType.IMAGE:
            return LeafNode("img", "", {"src": text_node.url, "alt": text_node.text})

        case _: 
            raise Exception('Text node does not have a valid text type.')


