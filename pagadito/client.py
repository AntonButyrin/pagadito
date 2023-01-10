import json
from typing import Optional

import requests

from pagadito import entities


class PAGADITO:
    """Work with pagadito.com
    """

    def __init__(
        self: 'PAGADITO',
        uid: str,
        wsk: str,
        format_return: str,
        url: str,
        ern: str,
    ):
        """Initial function

        Args:
            url (str): url sandbox or real
            uid (str): uid get in account pagadito.com
            wsk (str): wsk get in account pagadito.com
            ern (str): unique id transaction
            token (Optional[str]): second connect token
            token_trans (Optional[str]): second connect token_trans
            format_return (str): variants ['json','xml']
            products (list): list products
        """

        self.url: str = url
        self.uid: str = uid
        self.wsk: str = wsk
        self.ern: str = ern
        self.token: Optional[str] = None
        self.token_trans: Optional[str] = None
        self.format_return: str = format_return
        self.products: list = []

    def call(
        self: 'PAGADITO',
        data: dict,
        url: str,
        method: str,
    ) -> Optional['requests.models.Response']:
        """Call method to site

        Returns:
            return Response
        """

        if method == 'post':
            return requests.post(
                url=url,
                data=data,
                timeout=1,
            )

    def get_token(
        self: 'PAGADITO',
        data: dict,
        method: str,
    ) -> bool:
        """Get token method

        Returns:
            return bool
        """

        call: Optional['requests.models.Response'] = self.call(
            data=data,
            url=self.url,
            method=method,
        )
        if call:
            value: Optional[str] = json.loads(call.content).get('value', None)
            code: Optional[str] = json.loads(call.content).get('code', None)
            if value and code == "PG1001":
                if self.token_trans:
                    self.token = value
                else:
                    self.token_trans = value
                return True
        return False

    def connect(self: 'PAGADITO') -> bool:
        """Connect method

        Returns:
            return bool
        """

        data: dict = entities.TokenModel(
            uid=self.uid,
            wsk=self.wsk,
            format_return=self.format_return,
        ).dict()
        return self.get_token(
            data=data,
            method='post',
        )

    def create_product(
        self: 'PAGADITO',
        quantity: int,
        description: str,
        price: float,
        url_product: str,
    ):
        """Create product method

        Returns:
            return append method
        """

        product: dict = entities.ProductModel(
            quantity=quantity,
            description=description,
            price=price,
            url_product=url_product,
        ).dict()
        return self.products.append(product)

    def get_status(self) -> Optional[bool]:
        """Get status method

        Returns:
            return Optional[bool]
        """

        data: dict = entities.StatusModel(
            token=self.token,
            token_trans=self.token_trans,
            format_return=self.format_return,
        ).dict()
        call: Optional['requests.models.Response'] = self.call(
            url=self.url, data=data, method='post')
        if call:
            value: Optional[dict] = json.loads(call.content).get('value', None)
            code: Optional[str] = json.loads(call.content).get('code', None)
            if value and code == "PG1003":
                if value:
                    return value.get('status', None)
        return False

    def create_order(
        self: 'PAGADITO',
        amount: Optional[float],
        currency: str,
        allow_pending_payments: bool,
        custom_params: dict = {},
    ) -> Optional[str]:
        """Create order method

        Returns:
            return Optional[bool]
        """

        json_products = json.dumps(self.products)
        data = entities.OrderModel(
            token=self.token_trans,
            ern=self.ern,
            amount=amount,
            details=json_products,
            currency=currency,
            custom_params=custom_params,
            format_return=self.format_return,
            allow_pending_payments=allow_pending_payments,
        ).dict()

        call: Optional['requests.models.Response'] = self.call(
            url=self.url,
            data=data,
            method='post',
        )
        if call:
            value: Optional[str] = json.loads(call.content).get('value', None)
            code: Optional[str] = json.loads(call.content).get('code', None)
            if value and code == "PG1002":
                return value
        return None
