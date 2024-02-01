from typing import Dict, List, Optional, Tuple

from haystack.nodes.base import BaseComponent
from ionic.models.components import Query as SDKQuery, QueryAPIRequest
from ionic.models.operations import QueryResponse, QuerySecurity


class IonicShoppingTool(BaseComponent):
    """Ionic Shopping tool spec

    This tool can be used to build e-commerce experiences with LLMs.
    """

    outgoing_edges = 1

    def __init__(self, api_key: Optional[str] = None) -> None:
        """Ionic API Key

        Learn more about attribution with Ionic API Keys
        https://docs.ioniccommerce.com/guides/attribution
        """
        super().__init__()
        from ionic import Ionic as IonicSDK

        if api_key:
            self.client = IonicSDK(api_key_header=api_key)
        else:
            self.client = IonicSDK()

    def run(
        self,
        query: str,
        num_results: Optional[int] = 5,
        min_price: Optional[int] = None,
        max_price: Optional[int] = None,
        **kwargs,
    ) -> Tuple[Dict, str]:
        """
        Use this function to search for products and to get product recommendations

        Args:
            :param query: (str): A precise query of a product name or product category
            :param num_results: (Optional[int]) Defaults to 5. The number of product results to return.
            :param min_price: (Option[int]) The minimum price in cents the requester is willing to pay
            :param max_price: (Option[int]) The maximum price in cents the requester is willing to pay
            :param **kwargs:
        """
        request = QueryAPIRequest(
            query=SDKQuery(
                query=query,
                num_results=num_results,
                min_price=min_price,
                max_price=max_price,
            )
        )
        response: QueryResponse = self.client.query(
            request=request,
            security=QuerySecurity(),
        )

        output = {
            "results": [
                product
                for result in response.query_api_response.results
                for product in result.products
            ]
        }
        return output, "output_1"

    def run_batch(self, queries: List[str], **kwargs):
        pass
