from abc import ABC, abstractmethod

class Renderer(ABC):
    @abstractmethod
    def render_header(self, title: str) -> str:
        pass

    @abstractmethod
    def render_content(self, content: str) -> str:
        pass

    @abstractmethod
    def render_product(self, product: dict) -> str:
        pass


class HTMLRenderer(Renderer):
    def render_header(self, title: str) -> str:
        return f"<h1>{title}</h1>"

    def render_content(self, content: str) -> str:
        return f"<div>{content}</div>"

    def render_product(self, product: dict) -> str:
        return f"""
        <div>
            <h2>{product['name']}</h2>
            <p>{product['description']}</p>
            <img src="{product['image']}" alt="{product['name']}">
            <p>ID: {product['id']}</p>
        </div>
        """


class JsonRenderer(Renderer):
    def render_header(self, title: str) -> str:
        return f'{{"header": "{title}"}}'

    def render_content(self, content: str) -> str:
        return f'{{"content": "{content}"}}'

    def render_product(self, product: dict) -> str:
        return f'{{"product": {{"name": "{product["name"]}", "description": "{product["description"]}", "image": "{product["image"]}", "id": "{product["id"]}"}}}}'


class XmlRenderer(Renderer):
    def render_header(self, title: str) -> str:
        return f"<header>{title}</header>"

    def render_content(self, content: str) -> str:
        return f"<content>{content}</content>"

    def render_product(self, product: dict) -> str:
        return f"""
        <product>
            <name>{product['name']}</name>
            <description>{product['description']}</description>
            <image>{product['image']}</image>
            <id>{product['id']}</id>
        </product>
        """


class Page(ABC):
    def __init__(self, renderer: Renderer):
        self.renderer = renderer

    @abstractmethod
    def render(self) -> str:
        pass


class SimplePage(Page):
    def __init__(self, title: str, content: str, renderer: Renderer):
        super().__init__(renderer)
        self.title = title
        self.content = content

    def render(self) -> str:
        return f"{self.renderer.render_header(self.title)}\n{self.renderer.render_content(self.content)}"


class ProductPage(Page):
    def __init__(self, product: dict, renderer: Renderer):
        super().__init__(renderer)
        self.product = product

    def render(self) -> str:
        return self.renderer.render_product(self.product)

if __name__ == "__main__":
    simple_page = SimplePage("Welcome", "This is a simple page", HTMLRenderer())
    print("HTML Simple Page:")
    print(simple_page.render())

    product = {
        "name": "Laptop",
        "description": "A high-end gaming laptop",
        "image": "laptop.png",
        "id": "1234"
    }
    product_page = ProductPage(product, JsonRenderer())
    print("\nJSON Product Page:")
    print(product_page.render())

    simple_page.renderer = XmlRenderer()
    print("\nXML Simple Page:")
    print(simple_page.render())

    product_page.renderer = HTMLRenderer()
    print("\nHTML Product Page:")
    print(product_page.render())
