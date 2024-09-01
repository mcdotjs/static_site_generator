from htmlnode import HTMLNode
import unittest


class TestHTMLNode(unittest.TestCase):
    def test_eq(self):
        node = HTMLNode("h1", "value").__repr__()
        node2 = HTMLNode("h1", "value").__repr__()
        self.assertEqual(node, node2)

    def test_eeeeeqqqq(self):
        node = HTMLNode("h1", "value")
        node2 = HTMLNode("h1", "value").__eq__(node)
        self.assertTrue(node2)

    def test_not_eq(self):
        node = HTMLNode("h1", "value", ["jkljklkjlkj"])
        node2 = HTMLNode("h1", "value", [])
        self.assertNotEqual(node, node2)

    def test_to_html_props(self):
        node = HTMLNode(
            "div",
            "Hello, world!",
            None,
            {"class": "greeting", "href": "https://boot.dev"},
        )
        self.assertEqual(
            node.props_to_html(),
            ' class="greeting" href="https://boot.dev"',
        )

    def test_values(self):
        node = HTMLNode(
            "div",
            "I wish I could read",
        )
        self.assertEqual(
            node.tag,
            "div",
        )
        self.assertEqual(
            node.value,
            "I wish I could read",
        )
        self.assertEqual(
            node.children,
            None,
        )
        self.assertEqual(
            node.props,
            None,
        )

    def test_repr(self):
        node = HTMLNode(
            "p",
            "What a strange world",
            None,
            {"class": "primary"},
        )
        self.assertEqual(
            node.__repr__(),
            "HTMLNode(p, What a strange world, children: None, {'class': 'primary'})",
        )


if __name__ == "__main__":
    unittest.main()
