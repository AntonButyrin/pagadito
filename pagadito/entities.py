from typing import Optional

from pydantic import BaseModel


class TokenModel(BaseModel):
    """Token model for other actions

    Args:
        operation (str): operation unique id, default 'f3f191ce3326905ff4403bb05b0de150'
        uid (str): uid get in account pagadito.com
        wsk (str): wsk get in account pagadito.com
        format_return (str): variants ['json','xml']
    """

    operation: str = 'f3f191ce3326905ff4403bb05b0de150'
    uid: str
    wsk: str
    format_return: str


class OrderModel(BaseModel):
    """Order model for create order and get url invoice

    Args:
        operation (str): operation unique id, default '41216f8caf94aaa598db137e36d4673e'
        token (Optional[str]): get token in TokenModel and it's save in PAGADITO.token
        ern (str): unique id transaction
        amount (Optional[float]): amount all products in details
        details (Optional[dict]): dict products
        currency (str): variants ['USD','GTQ','HNL','NIO','CRC','PAB','DOP']
        custom_params (dict): dict custom params like in account pagadito.com
        format_return (str): variants ['json','xml']
        allow_pending_payments (bool): allow pending payment variants ['True','False']
    """

    operation: str = '41216f8caf94aaa598db137e36d4673e'
    token: Optional[str]
    ern: str
    amount: Optional[float]
    details: Optional[str]
    currency: str
    custom_params: dict
    format_return: str
    allow_pending_payments: bool


class ProductModel(BaseModel):
    """Product model for OrderModel

    Args:
        quantity (int): quantity product
        description (str): description product
        price (Optional[float]): price product
        url_product (Optional[str]): url to product or None
    """

    quantity: int
    description: str
    price: Optional[float]
    url_product: Optional[str] = None


class StatusModel(BaseModel):
    """Status model for getting status

    Args:
        operation (str): operation unique id, default '0b50820c65b0de71ce78f6221a5cf876'
        token (Optional[str]): token from second self.connect()
        token_trans (Optional[str]): token from first self.connect()
        format_return (str): variants ['json','xml']
    """

    operation: str = '0b50820c65b0de71ce78f6221a5cf876'
    token: Optional[str]
    token_trans: Optional[str]
    format_return: str
