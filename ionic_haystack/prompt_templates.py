from haystack.nodes import PromptTemplate

# This is the prompt template example for the Ionic Shopping Tool
ionic_template = PromptTemplate(
    prompt=str(
        """
Ionic is an e-commerce shopping tool. Assistant uses the Ionic Commerce Shopping Tool to find, discover, and compare products from thousands of online retailers. Assistant should use the tool when the user is looking for a product recommendation or trying to find a specific product. 

The user may specify the number of results, minimum price, and maximum price for which they want to see results.
Ionic Tool input accepts the following parameters:
  -  query string (required, must not include commas)
  - num_results: number of results (default to 4, no more than 10)
  - min_price: minimum price in cents ($5 becomes 500)
  - max_price: maximum price in cents
For example, if looking for coffee beans between 5 and 10 dollars, the tool input would be `run(query="coffee beans", num_results=5, min_price=500, max_price=1000)`.

Present product results as a list, always including the name of the product with the provided link to purchase. Other provided information can be included as relevant to the request, including price, merchant name, etc.
"""
    )
)
