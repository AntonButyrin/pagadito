# PAGADITO INTEGRATION
## pagadito integrations for python

adapted integration for python
Link to docs:
https://dev.pagadito.com/index.php?mod=docs

## Installation

python 3.8

```sh
git clone https://github.com/AntonButyrin/pagadito
cd pagadito
python setup.py
```

how it's work?

We can:
- connect
- add product to order
- create order
- get status order

CONNECT
```sh
pagadito = PAGADITO(url={url},uid={uid},wsk={wsk},format_return={format_return},ern={ern})
```

ADD PRODUCT
```sh
pagadito.create_product(quantity={quantity}, description={description}, price={price},url_product={url_product})
```

CREATE ORDER
```sh
pagadito.create_order(amount={amount}, currency={currency},allow_pending_payments={allow_pending_payments}, custom_params={})
```

GET STATUS
```sh
pagadito.get_status()
```

for create order and check status you should:
connect -> add product -> create_order -> connect -> get_status
