import csv

def read_csv(file_path: str) -> list[dict]:
    with open(file_path, mode='r', encoding='utf-8') as file:
        read = csv.DictReader(file)
        return list(read)
    

def process_data(raw_data: list[dict]) -> dict:
    product_categories = dict()
    for product in raw_data:
        category = product['Categoria']
        if category not in product_categories:
            product_categories[category] = []
        product_categories[category].append(product)
    return product_categories


def calculate_category_sales(processed_data: dict) -> dict:
    sales_by_category = dict()
    for category, products in processed_data.items():
        sales_total = sum(int(product['Quantidade']) * int(product['Venda']) for product in products)
        sales_by_category[category] = sales_total
    return sales_by_category


def main():
    file_path: str = 'Data/vendas.csv'
    raw = read_csv(file_path)
    product_categories = process_data(raw)
    sales_by_category = calculate_category_sales(product_categories)
    for category, total in sales_by_category.items():
        print(f'{category}:\t R$ {total:>8.2f}')


if __name__ == '__main__':
    main()
