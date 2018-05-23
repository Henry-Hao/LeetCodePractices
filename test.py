# Enter your code here. Read input from STDIN. Print output to STDOUT
def handle_product_collection(products,collection,discount):
    before = 0
    after = 0
    for product in products:
        before += product['price']
        if product['collection'] != collection:
            p = product['price']
        else:
            p = product['price'] - discount
            if p < 0:
                p = 0  
        after += p
    
    return before,after
    
    
    
def handle_product_price(products,price,discount):
    before = 0
    after = 0
    for product in products:
        before += product['price']
        if product['price'] < price:
            p = product['price']
        else:
            p = product['price'] - discount
            if p < 0:
                p = 0  
        after += p
    
    return before,after
    
def handle_cart_price(products,price,discount):
    before = 0
    after = 0
    for product in products:
        before += product['price']
    
    after = before if before < price else before - discount
    return before,after

    
if __name__ == '__main__':
    import json, requests
    discount_json = json.loads(input())
    id = discount_json['id']
    before = 0
    after = 0
    page = 1
    url = 'https://backend-challenge-fall-2018.herokuapp.com/carts.json'

    while True:
        r = requests.get(url,'?id='+str(id)+'&page='+str(page))
        r.json()
        products_json = json.loads(r.text)
        if discount_json['discount_type'] == 'product':
            if discount_json['collection'] is not None:
                rs = handle_product_collection(products_json,discount_json['collection'],discount_json['discount_value'])
            elif discount_json['product_value'] is not None: 
                rs = handle_product_price(products_json,discount_json['product_value'],discount_json['discount_value'])
        elif discount_json['discount_type' == 'cart']:
            rs = handle_cart_price(products_json,discount_json['cart_value'],discount_json['discount_value'])
        before += rs[0]
        after += rs[1]
        
        if products_json['current_page'] * products_json['per_page'] >= products_json['total']:
            break
        page += 1
        
    print(json.dumps({'total_amount':before,'before,total_after_discount':after}))
               