def predict_salary(payment_from, payment_to):
    if payment_from and payment_to:
        return int((payment_from + payment_to) / 2)
    elif not payment_to:
        return int(payment_from * 1.2)
    elif not payment_from:
        return int(payment_to * 0.8)
    else:
        None