import unittest
from htmlnode import HTMLNode 

class TestHTMLNode(unittest.TestCase):

    def test_init(self):
        node = HTMLNode(tag='div', value='Hello World')
        self.assertEqual(node.tag, 'div')
        self.assertEqual(node.value, 'Hello World')
        self.assertEqual(node.children, None)
        self.assertEqual(node.props, None)

    def test_to_html(self):
        class TestDiv(HTMLNode):
            def to_html(self):
                return '<div>Hello World</div>'
        
        node = TestDiv(tag='div', value='Hello World')
        result = node.to_html()
        self.assertIn('<div>Hello World</div>', result)

    def test_props_to_html(self):
        class TestDiv(HTMLNode):
            props = {'style': 'color: blue; '}
        
        node = TestDiv(tag='div', value='Hello World', props={'style': 'color: blue;'})
        result = node.props_to_html()
        self.assertEqual(result, 'style=color: blue; ')

if __name__ == '__main__':
    unittest.main()