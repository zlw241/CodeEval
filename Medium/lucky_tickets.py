

def generate_tickets(ticket_length):
    ticket_str = "%0{}d".format(ticket_length)
    max_ticket = int('9'*ticket_length)
    formatted_tickets = [ticket_str % i for i in range(0,max_ticket+1)]
    return formatted_tickets

def is_lucky_ticket(ticket):
    first_half, second_half = [int(i) for i in ticket[:len(ticket)//2]], [int(i) for i in ticket[len(ticket)//2:]]
    first_half_sum = sum(first_half)
    second_half_sum = sum(second_half)
    if first_half_sum == second_half_sum:
        return True
    return False

def count_lucky_tickets(ticket_length):
    all_tickets = generate_tickets(ticket_length)
    lucky_tickets = [i for i in all_tickets if is_lucky_ticket(i)]
    return len(lucky_tickets)


print(count_lucky_tickets(4))






