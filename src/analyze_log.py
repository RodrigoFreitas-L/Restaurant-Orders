import csv


def handler_maria(csv):
    maria = dict()
    for row in csv:
        if row[0] == "maria":
            if row[1] not in maria:
                maria[row[1]] = 1
            maria[row[1]] += 1
    return max(maria, key=maria.get)


def handler_joao(csv):
    orders = set()
    days = set()
    joao_days = set()
    joao_orders = set()
    for row in csv:
        orders.add(row[1])
        days.add(row[2])
        if row[0] == "joao":
            joao_orders.add(row[1])
            joao_days.add(row[2])
    new_joao_orders = orders.difference(joao_orders)
    new_joao_days = days.difference(joao_days)
    return new_joao_orders, new_joao_days


def handler_arnaldo(csv):
    arnaldo = 0
    for row in csv:
        if row[0] == "arnaldo" and row[1] == "hamburguer":
            arnaldo += 1
    return arnaldo


def analyze_log(path_to_file):
    if not path_to_file.endswith(".csv"):
        raise FileNotFoundError(f"Extensão inválida: '{path_to_file}'")

    try:
        with open(path_to_file, "r") as f:
            r = list(csv.reader(f))
            joao = handler_joao(r)
            maria = handler_maria(r)
            arnaldo = handler_arnaldo(r)
            with open("data/mkt_campaign.txt", "w") as f:
                f.write(f"{(maria)}\n")
                f.write(f"{str(arnaldo)}\n")
                f.write(f"{str(joao[0])}\n")
                f.write(f"{str(joao[1])}\n")
    except FileNotFoundError:
        raise FileNotFoundError(f"Arquivo inexistente: '{path_to_file}'")


# if __name__ == "__main__":
#     analyze_log("data/orders_1.csv")
